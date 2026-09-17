import argparse
import os
import random
import re
import shutil
import sys
from pathlib import Path

import numpy as np
import torch
import torchaudio


# ============================================================
# ARGUMENTOS
# ============================================================

parser = argparse.ArgumentParser(
    description="Genera una narracion con Chatterbox TTS a partir de un guion."
)

parser.add_argument(
    "--guion",
    required=True,
    help="Ruta WSL al archivo .txt que contiene el guion.",
)

parser.add_argument(
    "--voz",
    required=True,
    help="Ruta WSL al archivo de voz de referencia.",
)

parser.add_argument(
    "--salida-dir",
    required=True,
    help="Directorio WSL donde se guardara el WAV final.",
)

args = parser.parse_args()

GUION = Path(args.guion)
VOZ = Path(args.voz)
SALIDA_DIR = Path(args.salida_dir)


# ============================================================
# RUTAS DE CHATTERBOX
# ============================================================

ROOT = Path.home() / "ChatterboxES"
CHATTERBOX_SRC = ROOT / "chatterbox" / "src"
HF_CACHE = ROOT / "hf_cache"
TEMP = ROOT / "temp_generacion"

if not ROOT.is_dir():
    raise FileNotFoundError(
        f"No se encuentra la instalacion de Chatterbox: {ROOT}"
    )

if not CHATTERBOX_SRC.is_dir():
    raise FileNotFoundError(
        f"No se encuentra el codigo de Chatterbox es-ES: {CHATTERBOX_SRC}"
    )

HF_CACHE.mkdir(parents=True, exist_ok=True)

os.environ["HF_HOME"] = str(HF_CACHE)

# La version del Space es-ES debe tener prioridad sobre el paquete
# generico instalado en el entorno Python.
sys.path.insert(0, str(CHATTERBOX_SRC))

from chatterbox.tts import ChatterboxTTS


# ============================================================
# CONFIGURACION
# ============================================================

DEVICE = "cpu"

# Parametros iniciales de generacion.
# No son valores universales: pueden ajustarse para cada voz.
EXAGGERATION = 0.70
CFG_WEIGHT = 0.20
TEMPERATURE = 0.80

# Seed base para obtener un comportamiento mas reproducible.
# Cada bloque utiliza una seed diferente derivada de esta.
BASE_SEED = 12345

# Tamano aproximado de los bloques de texto.
TARGET_CHARS = 500
HARD_MAX = 650

# Pausas anadidas al unir bloques.
PAUSA_NORMAL = 0.28
PAUSA_SECCION = 0.70


# ============================================================
# UTILIDADES
# ============================================================

def fijar_seed(seed: int) -> None:
    """Fija las semillas utilizadas durante una generacion."""
    random.seed(seed)
    np.random.seed(seed % (2**32))
    torch.manual_seed(seed)


def es_timestamp(linea: str) -> bool:
    """
    Detecta timestamps utilizados como separadores de seccion.

    Ejemplos admitidos:
        [0:00-0:45]
        [0:00–0:45]
        [0:00—0:45]
        [12:30 - 13:20]
    """
    patron = r"^\s*\[\s*\d{1,3}:\d{2}\s*[-–—]\s*\d{1,3}:\d{2}\s*\]\s*$"
    return bool(re.match(patron, linea))


def normalizar_espacios(texto: str) -> str:
    """Convierte secuencias de espacios en un unico espacio."""
    return re.sub(r"\s+", " ", texto).strip()


def separar_frases(texto: str) -> list[str]:
    """
    Divide un texto utilizando finales normales de frase.

    La funcion no modifica las palabras ni la puntuacion.
    """
    texto = normalizar_espacios(texto)

    if not texto:
        return []

    partes = re.split(r"(?<=[.!?…])\s+", texto)

    return [
        normalizar_espacios(parte)
        for parte in partes
        if normalizar_espacios(parte)
    ]


def dividir_fragmento_largo(texto: str, limite: int) -> list[str]:
    """
    Divide un fragmento excesivamente largo por espacios.

    Se utiliza como mecanismo de seguridad cuando una sola frase
    supera HARD_MAX.
    """
    texto = normalizar_espacios(texto)

    if len(texto) <= limite:
        return [texto]

    palabras = texto.split()
    resultado = []
    actual = []

    for palabra in palabras:
        candidato = " ".join(actual + [palabra])

        if actual and len(candidato) > limite:
            resultado.append(" ".join(actual))
            actual = [palabra]
        else:
            actual.append(palabra)

    if actual:
        resultado.append(" ".join(actual))

    return resultado


def crear_bloques(texto: str) -> list[str]:
    """
    Agrupa frases completas en bloques cercanos a TARGET_CHARS.

    HARD_MAX actua como limite de seguridad para frases o fragmentos
    excepcionalmente largos.
    """
    frases_originales = separar_frases(texto)

    frases = []

    for frase in frases_originales:
        frases.extend(dividir_fragmento_largo(frase, HARD_MAX))

    bloques = []
    actual = ""

    for frase in frases:
        if not actual:
            actual = frase
            continue

        candidato = f"{actual} {frase}"

        if len(candidato) <= TARGET_CHARS:
            actual = candidato
        else:
            bloques.append(actual)
            actual = frase

    if actual:
        bloques.append(actual)

    return bloques


def preparar_guion(texto: str) -> list[dict]:
    """
    Prepara el guion para la generacion.

    - Ignora lineas vacias.
    - Elimina timestamps del texto hablado.
    - Utiliza los timestamps como separadores de seccion.
    - Divide cada seccion en bloques manejables.
    """
    secciones = []
    seccion_actual = []

    for linea in texto.splitlines():
        linea = linea.strip()

        if not linea:
            continue

        if es_timestamp(linea):
            if seccion_actual:
                secciones.append(" ".join(seccion_actual))
                seccion_actual = []
            continue

        seccion_actual.append(linea)

    if seccion_actual:
        secciones.append(" ".join(seccion_actual))

    # Si el texto no contiene timestamps, todo el guion se procesa
    # como una unica seccion.
    if not secciones:
        texto_limpio = normalizar_espacios(texto)

        if texto_limpio:
            secciones = [texto_limpio]

    resultado = []

    for seccion in secciones:
        bloques = crear_bloques(seccion)

        for indice, bloque in enumerate(bloques):
            resultado.append(
                {
                    "texto": bloque,
                    "fin_seccion": indice == len(bloques) - 1,
                }
            )

    return resultado


def normalizar_audio(wav: torch.Tensor) -> torch.Tensor:
    """
    Convierte la salida del modelo al formato esperado por torchaudio:
    [canales, muestras].
    """
    wav = wav.detach().cpu()

    while wav.ndim > 2 and wav.shape[0] == 1:
        wav = wav.squeeze(0)

    if wav.ndim == 1:
        wav = wav.unsqueeze(0)

    if wav.ndim != 2:
        raise RuntimeError(
            f"Formato de audio inesperado: tensor con {wav.ndim} dimensiones."
        )

    return wav


def crear_silencio(
    sample_rate: int,
    segundos: float,
    canales: int,
    dtype: torch.dtype,
) -> torch.Tensor:
    """Crea un fragmento de silencio."""
    muestras = max(0, int(round(sample_rate * segundos)))

    return torch.zeros(
        (canales, muestras),
        dtype=dtype,
    )


# ============================================================
# COMPROBACIONES
# ============================================================

if not GUION.is_file():
    raise FileNotFoundError(
        f"No encuentro el guion: {GUION}"
    )

if not VOZ.is_file():
    raise FileNotFoundError(
        f"No encuentro la voz de referencia: {VOZ}"
    )

SALIDA_DIR.mkdir(parents=True, exist_ok=True)

SALIDA = SALIDA_DIR / f"{GUION.stem}_voz.wav"


# ============================================================
# LEER GUION
# ============================================================

try:
    texto_guion = GUION.read_text(encoding="utf-8-sig")
except UnicodeDecodeError as exc:
    raise RuntimeError(
        "No se pudo leer el guion como UTF-8. "
        "Guarda el archivo .txt utilizando codificacion UTF-8."
    ) from exc

bloques = preparar_guion(texto_guion)

if not bloques:
    raise RuntimeError(
        "El guion esta vacio o no contiene texto que pueda generarse."
    )


# ============================================================
# INFORMACION
# ============================================================

print()
print("========================================")
print(" CHATTERBOX - GENERADOR")
print("========================================")
print()
print(f"Guion: {GUION}")
print(f"Voz: {VOZ}")
print(f"Salida: {SALIDA}")
print(f"Bloques: {len(bloques)}")
print()
print("Configuracion:")
print(f"  Device:        {DEVICE}")
print(f"  Exaggeration:  {EXAGGERATION}")
print(f"  CFG:           {CFG_WEIGHT}")
print(f"  Temperature:   {TEMPERATURE}")
print(f"  Seed base:     {BASE_SEED}")
print()


# ============================================================
# CARGAR MODELO
# ============================================================

print("Cargando Chatterbox...")
print()

modelo = ChatterboxTTS.from_pretrained(DEVICE)

sample_rate = int(modelo.sr)

print()
print(f"Sample rate: {sample_rate} Hz")
print("Preparando voz de referencia...")
print()

modelo.prepare_conditionals(
    str(VOZ),
    exaggeration=EXAGGERATION,
)


# ============================================================
# PREPARAR TEMPORALES
# ============================================================

if TEMP.exists():
    shutil.rmtree(TEMP)

TEMP.mkdir(parents=True, exist_ok=True)

archivos_temporales = []


# ============================================================
# GENERAR BLOQUES
# ============================================================

for indice, bloque in enumerate(bloques, start=1):
    texto = bloque["texto"]
    seed = BASE_SEED + indice - 1

    print()
    print("========================================")
    print(f" [{indice}/{len(bloques)}]")
    print("========================================")
    print()
    print(texto)
    print()
    print(f"Seed: {seed}")
    print()

    fijar_seed(seed)

    wav = modelo.generate(
        texto,
        language_id="es",
        exaggeration=EXAGGERATION,
        cfg_weight=CFG_WEIGHT,
        temperature=TEMPERATURE,
    )

    wav = normalizar_audio(wav)

    archivo_temp = TEMP / f"bloque_{indice:04d}.wav"

    torchaudio.save(
        str(archivo_temp),
        wav,
        sample_rate,
    )

    archivos_temporales.append(archivo_temp)

    del wav


# ============================================================
# UNIR BLOQUES
# ============================================================

print()
print("Uniendo bloques...")
print()

fragmentos = []

for indice, archivo in enumerate(archivos_temporales):
    audio, sr = torchaudio.load(str(archivo))

    if sr != sample_rate:
        raise RuntimeError(
            f"Sample rate inesperado en {archivo.name}: "
            f"{sr} Hz en lugar de {sample_rate} Hz."
        )

    fragmentos.append(audio)

    # No se anade silencio despues del ultimo bloque.
    if indice == len(archivos_temporales) - 1:
        continue

    if bloques[indice]["fin_seccion"]:
        segundos_pausa = PAUSA_SECCION
    else:
        segundos_pausa = PAUSA_NORMAL

    silencio = crear_silencio(
        sample_rate=sample_rate,
        segundos=segundos_pausa,
        canales=audio.shape[0],
        dtype=audio.dtype,
    )

    fragmentos.append(silencio)


if not fragmentos:
    raise RuntimeError(
        "No se genero ningun fragmento de audio."
    )

audio_final = torch.cat(fragmentos, dim=1)


# ============================================================
# GUARDAR RESULTADO
# ============================================================

torchaudio.save(
    str(SALIDA),
    audio_final,
    sample_rate,
)

duracion = audio_final.shape[1] / sample_rate


# ============================================================
# LIMPIEZA
# ============================================================

shutil.rmtree(TEMP, ignore_errors=True)


# ============================================================
# RESULTADO
# ============================================================

print()
print("========================================")
print(" LISTO")
print("========================================")
print()
print(f"Archivo: {SALIDA}")
print(f"Duracion: {duracion:.2f} segundos")
print()
