# 04 - Instalar Chatterbox y el modelo español de España

En este paso instalaremos Chatterbox dentro del entorno `chatterbox`, descargaremos el código específico del modelo **Spanish (Spain) / es-ES** y comprobaremos que puede cargar correctamente utilizando únicamente CPU.

Al terminar este paso tendremos:

```text
Ubuntu / WSL2
│
├── ~/miniforge3/
│   └── envs/
│       └── chatterbox/
│
└── ~/ChatterboxES/
    ├── chatterbox/
    └── hf_cache/
```

La carpeta:

```text
~/ChatterboxES
```

es importante.

Los scripts del lanzador que utilizaremos más adelante esperan encontrar el motor en esa ubicación.

---

# 1. Entrar en Ubuntu

Abre PowerShell y ejecuta:

```powershell
wsl -d Ubuntu-22.04
```

---

# 2. Activar el entorno `chatterbox`

Ejecuta:

```bash
conda activate chatterbox
```

La terminal debe comenzar con:

```text
(chatterbox)
```

Por ejemplo:

```text
(chatterbox) usuario@PC:~$
```

No continúes hasta que aparezca:

```text
(chatterbox)
```

---

# 3. Comprobar Python

Ejecuta:

```bash
python --version
```

Debe mostrar:

```text
Python 3.11.x
```

Comprueba también:

```bash
which python
```

La ruta debe ser similar a:

```text
/home/usuario/miniforge3/envs/chatterbox/bin/python
```

---

# 4. Comprobar que seguimos utilizando PyTorch para CPU

Ejecuta:

```bash
python -c "import torch; print(torch.__version__); print('CUDA:', torch.cuda.is_available())"
```

El resultado debe ser parecido a:

```text
2.6.0+cpu
CUDA: False
```

En esta instalación:

```text
CUDA: False
```

es correcto.

---

# 5. Instalar el paquete oficial de Chatterbox

Ejecuta:

```bash
python -m pip install chatterbox-tts==0.1.7
```

Este comando instalará Chatterbox y sus dependencias de Python dentro del entorno:

```text
chatterbox
```

Puede tardar varios minutos.

No cierres la terminal mientras se instala.

---

# 6. Volver a asegurar la versión de `setuptools`

Después de instalar Chatterbox ejecuta:

```bash
python -m pip install "setuptools<81"
```

Este paso es importante.

Durante las pruebas de esta instalación, Perth podía fallar al inicializarse con versiones nuevas de `setuptools`.

El error podía terminar en algo relacionado con:

```text
PerthImplicitWatermarker
```

o:

```text
NoneType object is not callable
```

Mantener:

```text
setuptools < 81
```

evita ese problema en esta configuración.

---

# 7. Comprobar que Chatterbox está instalado

Ejecuta:

```bash
python -m pip show chatterbox-tts
```

Debe aparecer información sobre el paquete.

También puedes comprobar que Python encuentra Chatterbox con:

```bash
python -c "import chatterbox; print('Chatterbox instalado')"
```

Debe mostrar:

```text
Chatterbox instalado
```

---

# 8. Volver a la carpeta personal

Ejecuta:

```bash
cd ~
```

Comprueba dónde estás:

```bash
pwd
```

Debe mostrar algo parecido a:

```text
/home/usuario
```

---

# 9. Descargar el código específico para español de España

Esta guía no utiliza únicamente el modelo multilingüe general.

Utiliza el modelo dedicado:

```text
ResembleAI/Chatterbox-Multilingual-es-es
```

optimizado para:

```text
Spanish (Spain)
es-ES
```

El código utilizado por la demo oficial de este modelo se encuentra en el Space:

```text
ResembleAI/Chatterbox-Multilingual-TTS-es-es
```

Clónalo con:

```bash
git clone https://huggingface.co/spaces/ResembleAI/Chatterbox-Multilingual-TTS-es-es ChatterboxES
```

Al terminar debe existir:

```text
~/ChatterboxES
```

---

# 10. Entrar en `ChatterboxES`

Ejecuta:

```bash
cd ~/ChatterboxES
```

Comprueba:

```bash
pwd
```

Debe terminar en:

```text
/ChatterboxES
```

Lista el contenido:

```bash
ls
```

Debe aparecer, entre otros archivos:

```text
chatterbox
app.py
requirements.txt
```

---

# 11. Importante: NO instalar `requirements.txt`

No ejecutes:

```text
pip install -r requirements.txt
```

en esta instalación.

El `requirements.txt` del Space oficial está preparado para el entorno de la demo alojada y puede incluir versiones de PyTorch destinadas a CUDA.

Esta guía utiliza deliberadamente:

```text
PyTorch CPU
```

que ya instalamos en el paso anterior.

Instalar directamente los requisitos del Space podría reemplazar esa configuración y descargar paquetes de GPU que no necesitamos.

Las dependencias necesarias ya se han instalado mediante:

```bash
python -m pip install chatterbox-tts
```

---

# 12. Comprobar el código específico de es-ES

El código que queremos utilizar se encuentra en:

```text
~/ChatterboxES/chatterbox/src
```

Comprueba que existe:

```bash
ls ~/ChatterboxES/chatterbox/src/chatterbox
```

Debe aparecer, entre otros:

```text
tts.py
models
```

---

# 13. Comprobar que estamos importando la versión es-ES

Desde:

```text
~/ChatterboxES
```

ejecuta:

```bash
PYTHONPATH="$PWD/chatterbox/src" python -c "from chatterbox.tts import ChatterboxTTS; print('Import es-ES correcto')"
```

Debe terminar mostrando:

```text
Import es-ES correcto
```

Este detalle es importante.

El prefijo:

```text
PYTHONPATH="$PWD/chatterbox/src"
```

hace que Python utilice el código incluido en el Space específico de español de España antes que la versión genérica instalada como paquete.

Más adelante `generar_guion.py` hará esto automáticamente.

---

# 14. Crear una caché local para los modelos

Ejecuta:

```bash
mkdir -p ~/ChatterboxES/hf_cache
```

Esta carpeta almacenará los modelos descargados:

```text
~/ChatterboxES/hf_cache
```

De esta forma, todo el motor pesado de Chatterbox queda localizado dentro de:

```text
~/ChatterboxES
```

---

# 15. Descargar y cargar el modelo por primera vez

Ahora realizaremos la primera carga.

Este paso descargará varios GB desde Hugging Face.

Ejecuta desde:

```text
~/ChatterboxES
```

el siguiente comando:

```bash
HF_HOME="$HOME/ChatterboxES/hf_cache" PYTHONPATH="$PWD/chatterbox/src" python -c "from chatterbox.tts import ChatterboxTTS; model = ChatterboxTTS.from_pretrained('cpu'); print('Modelo es-ES cargado correctamente'); print('Sample rate:', model.sr)"
```

La primera ejecución puede tardar bastante.

No cierres la terminal aunque durante algunos momentos parezca que no ocurre nada.

---

# 16. Qué está descargando

El modelo específico utilizado es:

```text
ResembleAI/Chatterbox-Multilingual-es-es
```

Entre sus archivos principales se encuentran:

```text
t3_es_es.safetensors
s3gen_v3.pt
```

También necesita algunos componentes compartidos del modelo base:

```text
ResembleAI/chatterbox
```

Por eso la primera carga descarga varios archivos de diferentes tamaños.

Algunos superan 1 GB.

Esto es normal.

---

# 17. Mensajes normales durante la descarga

Puedes ver mensajes parecidos a:

```text
Fetching files
Downloading
Reconstruction complete
```

o barras de progreso.

También puede aparecer:

```text
Warning: You are sending unauthenticated requests to the HF Hub
```

Esto no significa que la instalación haya fallado.

El modelo utilizado en esta guía es público y puede descargarse sin iniciar sesión.

Un token de Hugging Face puede aumentar los límites de descarga, pero no es obligatorio para esta instalación.

---

# 18. Resultado correcto

Cuando termine correctamente debería aparecer:

```text
Modelo es-ES cargado correctamente
```

También puede aparecer un mensaje parecido a:

```text
loaded PerthNet (Implicit)
```

Eso es correcto.

---

# 19. Comprobar Perth

Ejecuta:

```bash
python -c "import perth; print('Perth importado correctamente')"
```

Debe mostrar:

```text
Perth importado correctamente
```

---

# 20. Si aparece un aviso de `pkg_resources`

Puede aparecer un mensaje parecido a:

```text
UserWarning: pkg_resources is deprecated as an API
```

Si después Chatterbox continúa cargando correctamente, este mensaje es solamente un aviso.

No significa que la generación haya fallado.

La instalación mantiene:

```text
setuptools < 81
```

precisamente para conservar compatibilidad con la versión de Perth utilizada.

---

# 21. Si aparece `NoneType object is not callable`

Si durante:

```text
PerthImplicitWatermarker
```

aparece un error similar a:

```text
TypeError: 'NoneType' object is not callable
```

comprueba primero:

```bash
python -m pip show setuptools
```

Después ejecuta nuevamente:

```bash
python -m pip install "setuptools<81"
```

Cierra y vuelve a abrir Ubuntu o reactiva el entorno:

```bash
conda activate chatterbox
```

Vuelve a:

```bash
cd ~/ChatterboxES
```

y repite:

```bash
HF_HOME="$HOME/ChatterboxES/hf_cache" PYTHONPATH="$PWD/chatterbox/src" python -c "from chatterbox.tts import ChatterboxTTS; model = ChatterboxTTS.from_pretrained('cpu'); print('Modelo es-ES cargado correctamente')"
```

---

# 22. Si aparece un aviso de `LoRACompatibleLinear`

Puede aparecer un mensaje parecido a:

```text
FutureWarning: LoRACompatibleLinear is deprecated
```

Si el proceso continúa, no es un error.

Es un aviso de una dependencia interna relacionada con Diffusers.

No necesitas instalar nada adicional para solucionarlo.

---

# 23. Si aparece un aviso relacionado con `torch.backends.cuda`

También pueden aparecer avisos de PyTorch mencionando:

```text
torch.backends.cuda
```

aunque estés utilizando CPU.

Si:

```bash
python -c "import torch; print(torch.cuda.is_available())"
```

continúa mostrando:

```text
False
```

y Chatterbox genera correctamente, esos avisos no significan que la instalación esté intentando utilizar una GPU NVIDIA.

---

# 24. Comprobar que no se ha cambiado PyTorch

Después de instalar todo, ejecuta:

```bash
python -c "import torch; print('Torch:', torch.__version__); print('CUDA:', torch.cuda.is_available())"
```

La configuración de esta guía debe continuar utilizando CPU.

El resultado esperado es similar a:

```text
Torch: 2.6.0+cpu
CUDA: False
```

---

# 25. Comprobar la estructura final

Ejecuta:

```bash
cd ~/ChatterboxES
```

Después:

```bash
ls
```

Debes conservar esta carpeta.

No la elimines después de configurar el lanzador.

Más adelante la carpeta de uso diario estará en Windows, pero:

```text
~/ChatterboxES
```

seguirá siendo el motor que contiene el código específico y la caché de los modelos.

---

# Qué debe conservarse permanentemente

Dentro de WSL debes conservar:

```text
~/miniforge3/
~/ChatterboxES/
```

En particular:

```text
~/miniforge3/envs/chatterbox/
~/ChatterboxES/chatterbox/
~/ChatterboxES/hf_cache/
```

No es necesario copiar estos archivos al repositorio de GitHub.

Los modelos ocupan varios GB y cada usuario los descargará siguiendo esta guía.

---

# No subas el modelo a GitHub

No copies al repositorio:

```text
hf_cache/
t3_es_es.safetensors
s3gen_v3.pt
```

ni otros archivos descargados del modelo.

El repositorio debe contener los scripts y la documentación, no los pesos de Chatterbox.

---

# Por qué utilizamos el modelo es-ES

Chatterbox dispone de modelos multilingües generales, pero esta instalación utiliza específicamente el modelo dedicado:

```text
Spanish (Spain)
```

Su identificador de modelo es:

```text
ResembleAI/Chatterbox-Multilingual-es-es
```

y utiliza como identificador de idioma:

```text
es
```

Los scripts incluidos en este repositorio están preparados para esta configuración.

---

# No hace falta ejecutar la interfaz web

El repositorio del Space contiene:

```text
app.py
```

pero no necesitamos arrancar la interfaz web de Gradio.

No ejecutes:

```text
python app.py
```

para utilizar este tutorial.

Nuestro objetivo es utilizar Chatterbox directamente desde Python y después controlarlo desde Windows mediante:

```text
Generar voz.bat
```

Esto evita depender de una interfaz web local para el uso diario.

---

# Comprobación final

Antes de continuar deben funcionar estas comprobaciones.

## Entorno correcto

```bash
conda activate chatterbox
```

Debe aparecer:

```text
(chatterbox)
```

## Python

```bash
python --version
```

Debe mostrar:

```text
Python 3.11.x
```

## PyTorch CPU

```bash
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

Debe indicar que CUDA no está disponible.

## Código es-ES

Desde:

```text
~/ChatterboxES
```

ejecuta:

```bash
PYTHONPATH="$PWD/chatterbox/src" python -c "from chatterbox.tts import ChatterboxTTS; print('OK')"
```

Debe mostrar:

```text
OK
```

## Modelo

Ejecuta:

```bash
HF_HOME="$HOME/ChatterboxES/hf_cache" PYTHONPATH="$PWD/chatterbox/src" python -c "from chatterbox.tts import ChatterboxTTS; model = ChatterboxTTS.from_pretrained('cpu'); print('Modelo OK')"
```

Debe terminar mostrando:

```text
Modelo OK
```

Si estas comprobaciones funcionan, Chatterbox y el modelo específico de español de España están instalados correctamente.

---

# Siguiente paso

Continúa con:

```text
05_PREPARAR_VOZ.md
```
