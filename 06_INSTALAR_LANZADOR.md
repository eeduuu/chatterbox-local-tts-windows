# 06 - Instalar y configurar el lanzador de Windows

En este paso configuraremos la parte que permite utilizar Chatterbox desde Windows mediante doble clic.

Después de terminar, el flujo será:

```text
Doble clic en Generar voz.bat
        ↓
Seleccionar guion .txt
        ↓
Elegir voz
        ↓
WSL ejecuta Chatterbox
        ↓
Se genera un único .wav
        ↓
Se abre automáticamente la carpeta salidas
```

No será necesario:

- abrir Ubuntu manualmente;
- activar Conda manualmente;
- escribir comandos de Python;
- copiar el guion dentro de WSL;
- copiar la voz dentro de WSL.

---

# 1. Qué debe estar instalado antes

No continúes hasta haber completado:

```text
01_REQUISITOS.md
02_INSTALAR_WSL.md
03_PREPARAR_ENTORNO.md
04_INSTALAR_CHATTERBOX.md
05_PREPARAR_VOZ.md
```

En WSL deben existir:

```text
~/miniforge3/
~/miniforge3/envs/chatterbox/
~/ChatterboxES/
~/ChatterboxES/chatterbox/
~/ChatterboxES/hf_cache/
```

La distribución de WSL debe llamarse:

```text
Ubuntu-22.04
```

Los scripts incluidos en este repositorio utilizan ese nombre.

---

# 2. Carpeta del proyecto en Windows

Puedes guardar el repositorio prácticamente donde quieras en Windows.

Por ejemplo:

```text
C:\Herramientas\chatterbox-local-tts-windows
```

No es obligatorio utilizar esa ruta.

También puede estar dentro de una carpeta cuyo nombre contenga espacios.

Los scripts están preparados para trabajar con rutas como:

```text
C:\Mis programas\chatterbox-local-tts-windows
```

No contienen un nombre de usuario de Windows fijo.

---

# 3. Estructura necesaria

La carpeta debe contener:

```text
chatterbox-local-tts-windows/
│
├── Generar voz.bat
├── launcher.ps1
├── generar_guion.py
│
├── voces/
│
└── salidas/
```

Los tres archivos principales son:

```text
Generar voz.bat
launcher.ps1
generar_guion.py
```

No los muevas individualmente a carpetas diferentes.

Los tres deben permanecer juntos en la raíz del repositorio.

---

# 4. Para qué sirve cada archivo

## `Generar voz.bat`

Es el archivo que utilizarás normalmente.

Se ejecuta mediante doble clic desde Windows.

Su función es iniciar:

```text
launcher.ps1
```

sin que tengas que abrir PowerShell manualmente.

---

## `launcher.ps1`

Se encarga de la parte de Windows.

Hace automáticamente lo siguiente:

1. localiza la carpeta donde está el repositorio;
2. abre una ventana para seleccionar el guion `.txt`;
3. comprueba si existe una voz predeterminada;
4. permite elegir otra voz si quieres;
5. convierte las rutas de Windows a rutas compatibles con WSL;
6. localiza el Python del entorno `chatterbox`;
7. ejecuta `generar_guion.py` dentro de Ubuntu 22.04;
8. espera a que termine;
9. abre la carpeta `salidas`.

---

## `generar_guion.py`

Es el generador real.

Se ejecuta dentro de WSL y se encarga de:

- cargar Chatterbox;
- cargar el modelo es-ES;
- preparar la voz de referencia;
- leer el guion;
- ignorar los timestamps;
- dividir internamente textos largos;
- generar cada bloque;
- introducir pequeñas pausas;
- unir todos los bloques;
- crear un único archivo `.wav`;
- eliminar los archivos temporales.

---

# 5. Crear la carpeta `voces`

Si todavía no existe, crea:

```text
voces
```

dentro del repositorio.

Debe quedar así:

```text
chatterbox-local-tts-windows/
└── voces/
```

---

# 6. Configurar una voz predeterminada

Si quieres que el programa te pregunte:

```text
Usar la voz predeterminada?
```

coloca tu referencia dentro de:

```text
voces/
```

con este nombre:

```text
voz_predeterminada.mp3
```

La estructura será:

```text
voces/
└── voz_predeterminada.mp3
```

No subas este archivo a GitHub.

---

# 7. Si tu referencia está en WAV

No necesitas convertirla obligatoriamente a MP3.

Puedes conservar:

```text
mi_voz.wav
```

o cualquier otro nombre y seleccionarla manualmente cuando ejecutes el lanzador.

La detección automática de voz predeterminada utiliza:

```text
voz_predeterminada.mp3
```

Si no existe ese archivo, el lanzador abrirá directamente el selector de voz.

---

# 8. Utilizar varias voces

Puedes guardar varias referencias dentro de:

```text
voces/
```

Por ejemplo:

```text
voces/
├── voz_predeterminada.mp3
├── voz_2.mp3
└── voz_3.wav
```

Cuando ejecutes el lanzador:

- pulsa `Sí` para utilizar `voz_predeterminada.mp3`;
- pulsa `No` para seleccionar otra referencia.

No necesitas reinstalar Chatterbox para cambiar de voz.

---

# 9. Crear la carpeta `salidas`

Si todavía no existe, crea:

```text
salidas
```

Debe quedar:

```text
chatterbox-local-tts-windows/
└── salidas/
```

Los audios terminados aparecerán aquí.

El repositorio puede incluir:

```text
salidas/.gitkeep
```

para conservar la carpeta vacía en GitHub.

Los `.wav` generados no deben subirse al repositorio.

---

# 10. No necesitas una carpeta `guiones`

El lanzador permite seleccionar un archivo `.txt` desde cualquier ubicación del ordenador.

Por tanto, no es obligatorio guardar los guiones dentro del repositorio.

Puedes tenerlos donde normalmente organices tus vídeos.

Por ejemplo:

```text
Documentos/
└── Guiones YouTube/
    └── video_01.txt
```

Al ejecutar el BAT simplemente seleccionas ese archivo.

Esto evita duplicar guiones innecesariamente.

---

# 11. Formato del guion

El archivo debe ser texto plano:

```text
.txt
```

Puede contener timestamps como:

```text
[0:00–0:51]

Texto de la primera parte.

[0:51–1:41]

Texto de la segunda parte.
```

Los timestamps sirven para organizar el guion.

El generador los detecta y no los envía a Chatterbox como texto hablado.

---

# 12. Los timestamps no controlan la duración

Una línea como:

```text
[0:00–0:51]
```

no obliga al modelo a producir exactamente 51 segundos.

El programa utiliza la marca únicamente como separador lógico.

La duración real depende de:

- cantidad de palabras;
- puntuación;
- voz;
- parámetros de generación;
- interpretación del modelo.

---

# 13. Puntuación del guion

La puntuación sí puede afectar de forma importante a la lectura.

Por ejemplo:

```text
Lo sabes. Lo has vivido. Y aun así, ahí vas.
```

puede tener un ritmo diferente a:

```text
Lo sabes... Lo has vivido... Y aun así, ahí vas.
```

No es necesario llenar el guion de puntos suspensivos.

Utiliza puntuación natural para ayudar al modelo a identificar:

- pausas;
- cambios de idea;
- preguntas;
- contrastes;
- remates;
- respiraciones.

---

# 14. Configuración inicial del generador

El archivo:

```text
generar_guion.py
```

incluye inicialmente:

```python
EXAGGERATION = 0.70
CFG_WEIGHT = 0.20
TEMPERATURE = 0.80

BASE_SEED = 12345
```

También utiliza:

```python
TARGET_CHARS = 500
HARD_MAX = 650
```

y pausas aproximadas de:

```python
PAUSA_NORMAL = 0.28
PAUSA_SECCION = 0.70
```

Estos valores sirven como configuración inicial.

No son una configuración universal para todas las voces.

---

# 15. Qué significa el tamaño de bloque

El programa no envía necesariamente un guion de varios minutos completo al modelo.

Agrupa frases en bloques internos.

El objetivo inicial es aproximadamente:

```text
500 caracteres
```

con un límite flexible de:

```text
650 caracteres
```

El programa intenta no cortar una frase por la mitad.

---

# 16. Por qué se utilizan bloques

Durante el uso de Chatterbox se observa que las generaciones muy largas pueden ser menos consistentes.

Dividir internamente ayuda a reducir problemas como:

- cambios extraños de entonación;
- pérdida de naturalidad;
- generaciones demasiado largas;
- comportamiento impredecible al final de un texto.

Después, los bloques se unen automáticamente.

El usuario sigue recibiendo un único `.wav`.

---

# 17. Archivos temporales

Durante una generación se crea temporalmente dentro de WSL:

```text
~/ChatterboxES/temp_generacion/
```

Ahí se almacenan los bloques intermedios.

Cuando la generación termina correctamente, el programa elimina esa carpeta automáticamente.

No necesitas limpiarla manualmente después de cada generación.

---

# 18. Nombre del archivo final

El nombre se obtiene automáticamente del nombre del guion.

Por ejemplo, si seleccionas:

```text
guion_ejemplo.txt
```

se generará:

```text
guion_ejemplo_voz.wav
```

dentro de:

```text
salidas/
```

---

# 19. Primera ejecución

Haz doble clic en:

```text
Generar voz.bat
```

Debe abrirse una ventana para seleccionar el guion.

Selecciona un `.txt`.

---

# 20. Seleccionar la voz

Si existe:

```text
voces/voz_predeterminada.mp3
```

aparecerá una pregunta similar a:

```text
Usar la voz predeterminada?
```

Selecciona:

```text
Sí
```

para utilizarla.

Selecciona:

```text
No
```

para elegir manualmente otro archivo.

Si no existe una voz predeterminada, aparecerá directamente el selector.

---

# 21. Inicio de Chatterbox

Después de seleccionar guion y voz aparecerá una ventana de consola.

Debe mostrar algo parecido a:

```text
========================================
 CHATTERBOX LOCAL TTS
========================================
```

Después aparecerán:

```text
Guion:
...

Voz:
...

Generando...
```

---

# 22. Primera carga

Aunque los modelos ya estén descargados, Chatterbox necesita cargarlos en memoria cada vez que se inicia una generación nueva.

Es normal ver mensajes relacionados con:

```text
Fetching
Loading
PerthNet
Sampling
```

La primera generación después de arrancar puede tardar más.

---

# 23. Progreso de generación

Por cada bloque aparecerá algo parecido a:

```text
[1/5]
Texto del bloque...
```

y después:

```text
Sampling:
```

con una barra de progreso.

No cierres la ventana mientras aparezca ese proceso.

---

# 24. En CPU puede tardar bastante

En una instalación sin GPU NVIDIA es normal que un bloque tarde considerablemente más que su duración final.

Por ejemplo, decenas de segundos de voz pueden necesitar uno o varios minutos de cálculo.

Esto no significa que el programa esté bloqueado.

Mientras:

```text
Sampling
```

continúe avanzando, la generación sigue funcionando.

---

# 25. Final de la generación

Al terminar debe aparecer:

```text
LISTO
```

junto con:

```text
Duración:
```

y la ubicación del archivo.

Después el lanzador abrirá automáticamente:

```text
salidas/
```

---

# 26. Comprobar el WAV

Abre el archivo generado con cualquier reproductor compatible.

Por ejemplo:

```text
guion_ejemplo_voz.wav
```

Comprueba:

- que contiene todo el texto;
- que los timestamps no se pronuncian;
- que no falta ninguna sección;
- que la voz seleccionada es correcta;
- que no hay errores graves de generación.

---

# 27. Las rutas con espacios están soportadas

Una versión anterior del lanzador podía fallar si el proyecto o el guion estaban dentro de una ruta como:

```text
C:\Carpeta personal\Mi proyecto\
```

El lanzador actual pasa los argumentos a WSL por separado.

Por tanto, las rutas con espacios deben funcionar correctamente.

No es necesario renombrar tus carpetas para eliminar espacios.

---

# 28. Por qué no utilizamos un comando Bash construido como texto

El lanzador no crea una cadena larga similar a:

```text
bash -lc "python ruta con espacios..."
```

Ese método puede romper rutas y provocar errores como:

```text
python: can't open file ...
```

o:

```text
$'\r': command not found
```

La versión actual llama a WSL pasando cada argumento por separado.

Esto hace el lanzador más robusto.

---

# 29. WSL utilizado por el lanzador

El lanzador llama específicamente a:

```text
Ubuntu-22.04
```

Por eso el tutorial instala exactamente esa distribución.

Si cambias el nombre de la distribución, tendrás que modificar:

```text
launcher.ps1
```

---

# 30. Python utilizado por el lanzador

El lanzador utiliza directamente:

```text
$HOME/miniforge3/envs/chatterbox/bin/python
```

dentro de WSL.

Esto evita tener que ejecutar manualmente:

```bash
conda activate chatterbox
```

cada vez.

También evita que por accidente se utilice otro Python instalado en Ubuntu.

---

# 31. Ubicación del motor

`generar_guion.py` espera encontrar Chatterbox en:

```text
~/ChatterboxES
```

y específicamente el código es-ES en:

```text
~/ChatterboxES/chatterbox/src
```

También utiliza:

```text
~/ChatterboxES/hf_cache
```

para la caché de modelos.

Por eso estas rutas se mantuvieron constantes durante la instalación.

---

# 32. Mover el repositorio en Windows

Puedes mover la carpeta:

```text
chatterbox-local-tts-windows
```

a otra ubicación de Windows.

Los scripts calculan su propia ubicación.

Por tanto, no contienen una ruta fija como:

```text
C:\Users\usuario\...
```

Después de moverla, ejecuta nuevamente:

```text
Generar voz.bat
```

---

# 33. Mover `ChatterboxES` dentro de WSL

No muevas:

```text
~/ChatterboxES
```

sin modificar antes:

```text
generar_guion.py
```

El generador espera encontrar el motor en esa ruta.

---

# 34. Mover Miniforge

No muevas:

```text
~/miniforge3
```

sin modificar:

```text
launcher.ps1
```

El lanzador busca el Python en:

```text
~/miniforge3/envs/chatterbox/bin/python
```

---

# 35. PowerShell y política de ejecución

`Generar voz.bat` inicia PowerShell utilizando:

```text
-ExecutionPolicy Bypass
```

únicamente para esa ejecución.

No necesitas cambiar permanentemente la política de ejecución de PowerShell para todo Windows.

No es necesario ejecutar:

```powershell
Set-ExecutionPolicy Unrestricted
```

para seguir esta guía.

---

# 36. No es necesario ejecutar el BAT como administrador

Para el uso normal no deberías necesitar:

```text
Ejecutar como administrador
```

Haz simplemente doble clic.

WSL y Chatterbox deben estar instalados previamente.

---

# 37. No cierres WSL manualmente durante una generación

Mientras Chatterbox esté generando audio, no ejecutes:

```powershell
wsl --shutdown
```

ni cierres a la fuerza la consola.

Espera a que aparezca:

```text
LISTO
```

---

# 38. Si cancelas una generación

Si cierras la ventana durante:

```text
Sampling
```

el archivo final puede no generarse.

La próxima ejecución limpiará los temporales anteriores antes de comenzar una generación nueva.

---

# 39. Si ya existe un WAV con el mismo nombre

El generador utiliza el nombre del archivo de guion.

Si vuelves a generar:

```text
video.txt
```

la salida será otra vez:

```text
video_voz.wav
```

La nueva generación puede reemplazar la anterior.

Si quieres conservar varias versiones, cambia el nombre del guion o mueve/renombra el WAV anterior antes de generar de nuevo.

---

# 40. No subas voces ni salidas a GitHub

Antes de publicar el repositorio debe existir un:

```text
.gitignore
```

que ignore como mínimo:

```text
voces/*.mp3
voces/*.wav
salidas/*.wav
```

Lo configuraremos como parte de los archivos finales del repositorio.

---

# 41. Comprobación final

La estructura debería ser similar a:

```text
chatterbox-local-tts-windows/
│
├── Generar voz.bat
├── launcher.ps1
├── generar_guion.py
│
├── voces/
│   ├── README.md
│   └── voz_predeterminada.mp3
│
└── salidas/
    └── .gitkeep
```

El archivo:

```text
voz_predeterminada.mp3
```

solo existe localmente.

No aparecerá en GitHub.

---

# 42. Prueba final del lanzador

Haz doble clic en:

```text
Generar voz.bat
```

Debes poder completar este flujo sin escribir ningún comando:

```text
Seleccionar guion
        ↓
Seleccionar voz
        ↓
Esperar generación
        ↓
Obtener WAV
```

Si funciona, el lanzador está correctamente instalado.

---

# Si falla

No cambies archivos al azar.

Consulta:

```text
08_ERRORES_Y_SOLUCIONES.md
```

y busca el mensaje exacto que aparece en la consola.

Los errores reales encontrados durante la instalación y sus soluciones estarán documentados allí.

---

# Siguiente paso

Continúa con:

```text
07_USO.md
```

Ese documento explica el flujo normal después de terminar completamente la instalación.
