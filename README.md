# Chatterbox Local TTS para Windows

Genera voz localmente en Windows usando **Chatterbox TTS**, WSL2 y el modelo dedicado de **español de España (es-ES)**.

Este repositorio contiene una guía paso a paso y un lanzador sencillo para poder convertir guiones `.txt` en archivos `.wav` sin depender de servicios de pago ni tener que escribir comandos cada vez.

Una vez completada la instalación, el uso habitual consiste simplemente en ejecutar:

```text
Generar voz.bat
```

---

## ¿Qué permite hacer?

- Ejecutar Chatterbox localmente en Windows.
- Utilizar español de España.
- Usar una voz de referencia propia.
- Cambiar fácilmente la voz de referencia.
- Generar narraciones largas a partir de archivos `.txt`.
- Dividir automáticamente textos largos en bloques.
- Unir los bloques automáticamente en un único `.wav`.
- Ejecutar todo mediante doble clic.
- Funcionar sin una GPU NVIDIA.
- Utilizar únicamente CPU si es necesario.

---

## ¿Cómo funciona?

El flujo normal es:

```text
Guion .txt
    ↓
Generar voz.bat
    ↓
Seleccionar guion
    ↓
Seleccionar voz
    ↓
Chatterbox se ejecuta dentro de WSL2
    ↓
Audio .wav en la carpeta salidas
```

Windows se utiliza como interfaz.

Chatterbox y sus modelos se ejecutan dentro de Ubuntu mediante WSL2.

---

## Hardware

Esta guía está pensada especialmente para equipos Windows que quieren ejecutar Chatterbox localmente sin depender de CUDA o de una GPU NVIDIA.

### Recomendado

- Windows 10 u 11 de 64 bits.
- Procesador x64.
- 16 GB de RAM.
- Varios GB de espacio libre.
- Conexión a Internet durante la instalación inicial y la descarga de modelos.

Una GPU NVIDIA no es obligatoria para seguir esta guía.

La instalación ha sido probada utilizando:

- CPU Intel.
- 16 GB de RAM.
- Gráficos integrados.
- Sin CUDA.
- Sin GPU NVIDIA.

En CPU funciona correctamente, pero la generación de textos largos puede tardar varios minutos.

---

## Modelo utilizado

Este proyecto utiliza **Chatterbox TTS**, desarrollado por Resemble AI.

La instalación de esta guía utiliza el modelo dedicado de:

```text
Spanish (Spain) / es-ES
```

Los modelos no están incluidos en este repositorio.

Se descargan durante la instalación y permanecen almacenados localmente en el equipo.

---

## Voz de referencia

Chatterbox puede utilizar un pequeño archivo de audio como referencia de voz.

La estructura prevista es:

```text
voces/
└── voz_predeterminada.mp3
```

También pueden utilizarse archivos `.wav`.

La voz de referencia no debe subirse al repositorio.

El lanzador permite utilizar una voz predeterminada o seleccionar otra voz diferente al generar un audio.

Utiliza únicamente voces propias o voces para las que tengas permiso.

---

## Estructura del repositorio

```text
chatterbox-local-tts-windows/
│
├── README.md
├── 01_REQUISITOS.md
├── 02_INSTALAR_WSL.md
├── 03_PREPARAR_ENTORNO.md
├── 04_INSTALAR_CHATTERBOX.md
├── 05_PREPARAR_VOZ.md
├── 06_INSTALAR_LANZADOR.md
├── 07_USO.md
├── 08_ERRORES_Y_SOLUCIONES.md
│
├── Generar voz.bat
├── launcher.ps1
├── generar_guion.py
├── .gitignore
│
├── voces/
│   └── README.md
│
└── salidas/
    └── .gitkeep
```

---

# Instalación

Si empiezas desde cero, sigue los documentos en este orden.

## 1. Requisitos

```text
01_REQUISITOS.md
```

Explica qué necesitas antes de empezar y qué tipo de hardware puede utilizar esta instalación.

---

## 2. Instalar WSL2

```text
02_INSTALAR_WSL.md
```

Instala WSL2 y Ubuntu 22.04 en Windows.

---

## 3. Preparar el entorno

```text
03_PREPARAR_ENTORNO.md
```

Instala las herramientas necesarias dentro de Ubuntu, Miniforge, Python y el entorno dedicado para Chatterbox.

---

## 4. Instalar Chatterbox

```text
04_INSTALAR_CHATTERBOX.md
```

Instala Chatterbox y descarga el modelo dedicado de español de España.

---

## 5. Preparar una voz

```text
05_PREPARAR_VOZ.md
```

Explica cómo preparar y colocar el archivo de audio que se utilizará como referencia.

---

## 6. Instalar el lanzador

```text
06_INSTALAR_LANZADOR.md
```

Configura:

```text
Generar voz.bat
launcher.ps1
generar_guion.py
```

Estos archivos permiten utilizar Chatterbox desde Windows sin tener que entrar manualmente en Ubuntu cada vez.

---

## 7. Uso diario

```text
07_USO.md
```

Explica cómo generar nuevos audios una vez terminada la instalación.

---

## 8. Errores y soluciones

```text
08_ERRORES_Y_SOLUCIONES.md
```

Incluye soluciones a problemas reales que pueden aparecer durante la instalación o ejecución.

---

# Uso después de instalarlo

Después de completar todos los pasos, no es necesario ejecutar manualmente comandos de Linux para cada narración.

El proceso habitual es:

1. Preparar el guion en un archivo `.txt`.
2. Ejecutar `Generar voz.bat`.
3. Seleccionar el guion.
4. Elegir la voz predeterminada o seleccionar otra.
5. Esperar a que termine Chatterbox.
6. Abrir el `.wav` generado dentro de `salidas`.

---

# Guiones largos

Chatterbox funciona mejor si una narración de varios minutos no se envía al modelo completa en una sola generación.

Por eso `generar_guion.py` divide internamente el texto en bloques de tamaño razonable.

Cada bloque se genera por separado.

Después, el programa une automáticamente todos los bloques.

El resultado para el usuario sigue siendo un único archivo:

```text
salidas/
└── nombre_del_guion_voz.wav
```

Los archivos temporales utilizados durante la generación se eliminan automáticamente al finalizar correctamente.

---

# Configuración de generación

La configuración inicial incluida en `generar_guion.py` es:

```text
Exaggeration: 0.70
CFG:          0.20
Temperature:  0.80
```

Estos valores no son universales.

Dependiendo de la voz de referencia y del tipo de texto puede ser conveniente probar otras configuraciones.

La puntuación del propio guion también afecta de forma importante al resultado.

Comas, puntos, puntos suspensivos, preguntas y otras pausas pueden cambiar el ritmo y la naturalidad de la lectura.

---

# Duración del audio

Los tiempos escritos en un guion no obligan a Chatterbox a producir una duración determinada.

Chatterbox no dispone en esta configuración de un control preciso para indicar:

```text
este bloque debe durar exactamente 50 segundos
```

La duración depende principalmente de:

- cantidad de texto;
- puntuación;
- voz de referencia;
- configuración utilizada;
- interpretación generada por el modelo.

Intentar estirar artificialmente un audio para alcanzar una duración muy diferente puede reducir mucho su naturalidad.

---

# Limitaciones

Esta instalación funciona localmente, pero Chatterbox sigue teniendo algunas limitaciones.

Ten en cuenta que:

- una misma voz puede variar ligeramente entre generaciones;
- los fragmentos largos pueden ser menos consistentes que los cortos;
- algunas partes de una generación pueden sonar mejor que otras;
- la puntuación influye considerablemente en el ritmo;
- no existe una duración exacta garantizada;
- la similitud con la voz original depende de la referencia utilizada;
- en CPU la generación puede ser lenta;
- el resultado no siempre será idéntico entre textos diferentes.

El objetivo de esta configuración es conseguir una narración local, natural y utilizable sin depender de hardware NVIDIA ni de servicios externos de pago.

---

# Privacidad

Los archivos personales no deben formar parte del repositorio.

No deben subirse:

- voces de referencia;
- audios generados;
- modelos descargados;
- cachés;
- archivos temporales;
- rutas personales;
- nombres de usuario;
- configuraciones específicas de un ordenador.

El repositorio debe poder clonarse tanto en otro ordenador propio como en el equipo de cualquier otra persona.

---

# Archivos que no incluye GitHub

Los modelos de Chatterbox ocupan varios GB y no deben almacenarse dentro del repositorio.

Tampoco deben almacenarse voces personales.

El repositorio contiene únicamente:

- documentación;
- scripts;
- configuración;
- estructura necesaria para reproducir la instalación.

Los modelos se descargan siguiendo la guía.

---

# Uso local

Una vez que los modelos necesarios están descargados, la generación de voz se realiza localmente en el equipo.

No es necesario subir el guion ni la voz de referencia a un servicio de síntesis de voz externo para realizar la generación.

---

# Proyecto original

Chatterbox TTS es un proyecto desarrollado por **Resemble AI**.

Este repositorio no incluye ni redistribuye los pesos de los modelos.

Su objetivo es documentar una instalación reproducible para Windows y proporcionar un lanzador sencillo para utilizarla.
