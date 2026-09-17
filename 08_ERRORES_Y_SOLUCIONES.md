# 08 - Errores y soluciones

Este documento reúne los problemas más importantes que pueden aparecer durante la instalación o el uso de esta configuración.

Está centrado en errores reales encontrados durante la preparación del proyecto y en avisos que pueden parecer errores aunque no impidan utilizar Chatterbox.

Antes de cambiar archivos o reinstalar componentes, busca aquí el mensaje que aparece en la consola.

---

# 1. `conda: command not found`

## Síntoma

Al ejecutar:

```bash
conda activate chatterbox
```

aparece:

```text
conda: command not found
```

## Solución

Carga manualmente Conda:

```bash
source "$HOME/miniforge3/etc/profile.d/conda.sh"
```

Después:

```bash
conda init bash
```

Recarga la configuración:

```bash
source ~/.bashrc
```

Comprueba:

```bash
conda --version
```

Y activa el entorno:

```bash
conda activate chatterbox
```

---

# 2. No aparece `(chatterbox)` en la terminal

## Síntoma

La terminal muestra algo parecido a:

```text
usuario@PC:~$
```

en lugar de:

```text
(chatterbox) usuario@PC:~$
```

## Solución

Ejecuta:

```bash
conda activate chatterbox
```

Antes de instalar paquetes manualmente dentro de Ubuntu, comprueba siempre que aparece:

```text
(chatterbox)
```

---

# 3. Python incorrecto

## Síntoma

Chatterbox no encuentra paquetes que supuestamente están instalados o aparece un error relacionado con módulos ausentes.

Comprueba:

```bash
which python
```

## Resultado correcto

La ruta debe ser parecida a:

```text
/home/usuario/miniforge3/envs/chatterbox/bin/python
```

## Solución

Activa el entorno:

```bash
conda activate chatterbox
```

y vuelve a comprobar:

```bash
which python
```

---

# 4. `ModuleNotFoundError` relacionado con Chatterbox

## Síntoma

Aparece algo parecido a:

```text
ModuleNotFoundError: No module named 'chatterbox'
```

## Primero comprueba

Activa el entorno:

```bash
conda activate chatterbox
```

Después:

```bash
python -m pip show chatterbox-tts
```

Si no aparece el paquete, instálalo:

```bash
python -m pip install chatterbox-tts
```

Después vuelve a aplicar:

```bash
python -m pip install "setuptools<81"
```

---

# 5. Se importa la versión equivocada de Chatterbox

Esta instalación utiliza el código específico del Space de español de España almacenado en:

```text
~/ChatterboxES/chatterbox/src
```

El generador incluido en este repositorio añade esa ruta automáticamente.

Si haces una prueba manual, utiliza:

```bash
cd ~/ChatterboxES
```

y:

```bash
PYTHONPATH="$PWD/chatterbox/src" python -c "from chatterbox.tts import ChatterboxTTS; print('OK')"
```

Debe mostrar:

```text
OK
```

---

# 6. Error de Perth: `NoneType object is not callable`

## Síntoma

Durante la carga aparece un error relacionado con:

```text
PerthImplicitWatermarker
```

y termina con algo parecido a:

```text
TypeError: 'NoneType' object is not callable
```

## Solución

Activa el entorno:

```bash
conda activate chatterbox
```

Después instala una versión compatible de `setuptools`:

```bash
python -m pip install "setuptools<81"
```

Comprueba:

```bash
python -m pip show setuptools
```

Después vuelve a cargar Chatterbox.

---

# 7. Aviso `pkg_resources is deprecated`

## Síntoma

Puede aparecer algo similar a:

```text
UserWarning: pkg_resources is deprecated as an API
```

## ¿Es un error?

No, siempre que el proceso continúe.

Puede aparecer antes de que Perth termine cargando.

Un funcionamiento correcto puede mostrar después algo parecido a:

```text
loaded PerthNet (Implicit)
```

No necesitas hacer nada si la generación continúa.

---

# 8. Aviso `LoRACompatibleLinear is deprecated`

## Síntoma

Puede aparecer:

```text
FutureWarning: LoRACompatibleLinear is deprecated
```

## ¿Es un error?

No.

Es un aviso de una dependencia interna.

Si después Chatterbox continúa cargando y comienza:

```text
Sampling:
```

puedes ignorarlo.

---

# 9. Aviso relacionado con `torch.backends.cuda.sdp_kernel()`

## Síntoma

Durante la generación puede aparecer:

```text
FutureWarning: torch.backends.cuda.sdp_kernel() is deprecated
```

## ¿Significa que está intentando utilizar CUDA?

No necesariamente.

Esta instalación utiliza PyTorch para CPU.

Compruébalo con:

```bash
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

En esta guía el resultado esperado es:

```text
False
```

para CUDA.

Si la generación continúa, el aviso puede ignorarse.

---

# 10. `Warning: You are sending unauthenticated requests to the HF Hub`

## Síntoma

Durante la carga o descarga del modelo aparece:

```text
Warning: You are sending unauthenticated requests to the HF Hub
```

## ¿Es un error?

No.

Los modelos utilizados son públicos y pueden descargarse sin iniciar sesión.

Un token de Hugging Face puede aumentar algunos límites de descarga, pero no es obligatorio para esta instalación.

Si los archivos continúan descargándose, no hagas nada.

---

# 11. `Fetching files` aparece cada vez

## Síntoma

Cada vez que inicia Chatterbox aparece algo parecido a:

```text
Fetching 3 files
```

aunque el modelo ya se haya descargado.

## ¿Está descargando varios GB otra vez?

Normalmente no.

Hugging Face comprueba los archivos almacenados en caché.

Si ya están descargados correctamente, la comprobación puede terminar casi inmediatamente.

La caché utilizada por este proyecto está en:

```text
~/ChatterboxES/hf_cache
```

No elimines esa carpeta salvo que quieras volver a descargar los modelos.

---

# 12. La primera carga tarda mucho

La primera ejecución necesita descargar varios archivos grandes.

Puede parecer que el programa está detenido durante algunos momentos.

Es normal ver:

```text
Fetching
Downloading
Reconstruction complete
```

o barras de progreso.

No cierres la terminal mientras exista actividad.

---

# 13. `CUDA: False`

## Síntoma

Ejecutas:

```bash
python -c "import torch; print(torch.cuda.is_available())"
```

y aparece:

```text
False
```

## ¿Es un problema?

No.

Esta guía está diseñada específicamente para funcionar mediante:

```text
CPU
```

sin NVIDIA ni CUDA.

---

# 14. Se instalaron paquetes CUDA por accidente

Si después de instalar dependencias observas que PyTorch ya no es la versión CPU esperada, comprueba:

```bash
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

Para volver a la configuración de esta guía, reinstala PyTorch CPU:

```bash
python -m pip install --force-reinstall torch==2.6.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cpu
```

Después vuelve a aplicar:

```bash
python -m pip install "setuptools<81"
```

Evita instalar directamente el `requirements.txt` del Space si eso reemplaza la configuración CPU.

---

# 15. El BAT se abre y se cierra inmediatamente

Ejecuta:

```text
Generar voz.bat
```

desde una ventana de consola o revisa que el archivo termine mostrando los errores antes de cerrarse.

El BAT incluido en este repositorio contiene una pausa cuando ocurre un error.

Comprueba que existen, juntos:

```text
Generar voz.bat
launcher.ps1
generar_guion.py
```

---

# 16. PowerShell dice que falta el terminador de una cadena

## Síntoma

Puede aparecer algo parecido a:

```text
Falta la cadena en el terminador: ".
```

o:

```text
TerminatorExpectedAtEndOfString
```

## Causa

Normalmente significa que:

```text
launcher.ps1
```

tiene una comilla sin cerrar o fue modificado incorrectamente.

La línea indicada por PowerShell no siempre es la línea donde comenzó el problema.

## Solución

Restaura:

```text
launcher.ps1
```

desde la versión original del repositorio.

No intentes reparar únicamente la última línea indicada si no sabes dónde está la comilla incorrecta.

---

# 17. Error `$'\r': command not found`

## Síntoma

Puede aparecer algo parecido a:

```text
$'\r': command not found
```

## Causa

Este problema puede aparecer cuando un script de Windows con finales de línea CRLF se intenta interpretar directamente mediante Bash.

También puede aparecer en lanzadores que construyen un comando Bash completo como una cadena.

## Solución en este proyecto

La versión actual de:

```text
launcher.ps1
```

no ejecuta el generador mediante una cadena:

```text
bash -lc "..."
```

En su lugar llama directamente a:

```text
wsl.exe
```

pasando cada argumento por separado.

Si ves este error, asegúrate de estar utilizando la versión actual de los scripts del repositorio.

---

# 18. `python: can't open file ...`

## Síntoma

Aparece:

```text
python: can't open file '...'
```

y la ruta parece terminar antes de tiempo.

Por ejemplo, el problema puede aparecer si una carpeta contiene espacios.

## Causa

Una ruta con espacios se ha dividido incorrectamente al pasar de Windows a Bash o Python.

## Solución

Utiliza la versión actual de:

```text
launcher.ps1
```

que pasa los argumentos a WSL de forma separada.

No es necesario eliminar espacios de las carpetas.

---

# 19. El proyecto está dentro de una ruta con espacios

Rutas como:

```text
C:\Mis herramientas\chatterbox-local-tts-windows
```

deben funcionar con el lanzador actual.

Si una ruta con espacios falla, no renombres primero todas tus carpetas.

Comprueba que:

```text
launcher.ps1
```

es la versión actual del repositorio.

---

# 20. Aparecen caracteres como `generaciÃ³n`

## Síntoma

Los caracteres con tilde aparecen incorrectamente:

```text
generaciÃ³n
```

en lugar de:

```text
generación
```

## Causa

Es un problema de codificación de la consola de Windows.

## Solución

El BAT incluido utiliza:

```bat
chcp 65001 >nul
```

para utilizar UTF-8.

Comprueba que:

```text
Generar voz.bat
```

no haya sido modificado.

Este problema afecta principalmente a cómo se muestra el texto en consola y no a la calidad del audio generado.

---

# 21. PowerShell bloquea `launcher.ps1`

El BAT incluido ejecuta PowerShell utilizando:

```text
-ExecutionPolicy Bypass
```

para esa ejecución concreta.

No es necesario cambiar permanentemente la política de ejecución de Windows.

No ejecutes:

```powershell
Set-ExecutionPolicy Unrestricted
```

solo para este proyecto.

Si has modificado el BAT, restaura la versión incluida en el repositorio.

---

# 22. `wslpath` no convierte una ruta

El lanzador necesita que:

```text
Ubuntu-22.04
```

esté instalada.

Comprueba desde PowerShell:

```powershell
wsl --list --verbose
```

Debe aparecer:

```text
Ubuntu-22.04
```

Si utilizas una distribución con otro nombre, el lanzador no la encontrará automáticamente.

---

# 23. El lanzador no encuentra Ubuntu

## Síntoma

Puede aparecer un error indicando que:

```text
Ubuntu-22.04
```

no existe.

## Comprobación

En PowerShell:

```powershell
wsl --list --verbose
```

## Solución

La guía utiliza específicamente:

```text
Ubuntu-22.04
```

Si no está instalada, sigue:

```text
02_INSTALAR_WSL.md
```

Si deliberadamente utilizas otra distribución, tendrás que modificar el nombre en:

```text
launcher.ps1
```

---

# 24. El lanzador no encuentra Python

El lanzador espera encontrar:

```text
~/miniforge3/envs/chatterbox/bin/python
```

Comprueba dentro de Ubuntu:

```bash
ls ~/miniforge3/envs/chatterbox/bin/python
```

Si existe, debería mostrar esa misma ruta.

Si no existe, revisa:

```text
03_PREPARAR_ENTORNO.md
```

---

# 25. El lanzador no encuentra `ChatterboxES`

El generador espera:

```text
~/ChatterboxES
```

Comprueba:

```bash
ls ~/ChatterboxES
```

También debe existir:

```bash
ls ~/ChatterboxES/chatterbox/src/chatterbox
```

Si la carpeta fue movida o renombrada, restaura la ubicación o modifica conscientemente:

```text
generar_guion.py
```

---

# 26. No encuentra `hf_cache`

La carpeta esperada es:

```text
~/ChatterboxES/hf_cache
```

Puedes crearla con:

```bash
mkdir -p ~/ChatterboxES/hf_cache
```

La próxima carga descargará cualquier archivo que falte.

---

# 27. No aparece la pregunta de voz predeterminada

La voz automática debe llamarse:

```text
voz_predeterminada.mp3
```

y estar en:

```text
voces/
```

La estructura debe ser:

```text
chatterbox-local-tts-windows/
└── voces/
    └── voz_predeterminada.mp3
```

Si no existe, el lanzador abrirá directamente el selector de archivos.

Eso es comportamiento normal.

---

# 28. La voz seleccionada no existe o fue movida

Si seleccionas una referencia y después la eliminas o mueves antes de que comience Python, puede aparecer un error indicando que el archivo no existe.

Vuelve a ejecutar:

```text
Generar voz.bat
```

y selecciona una referencia válida.

---

# 29. El guion no se encuentra

Si el guion fue movido, eliminado o está en una unidad que dejó de estar disponible, el generador puede mostrar:

```text
No encuentro el guion
```

Vuelve a ejecutar el BAT y selecciona nuevamente el `.txt`.

---

# 30. `El guion está vacío`

## Síntoma

El generador termina con:

```text
El guion está vacío.
```

## Comprueba

Abre el `.txt` y verifica que contiene texto hablado.

Un archivo con únicamente:

```text
timestamps
líneas vacías
```

no contiene contenido que Chatterbox pueda generar.

---

# 31. Los timestamps se pronuncian

El generador detecta líneas con un formato similar a:

```text
[0:00–0:45]
```

o:

```text
[0:00-0:45]
```

Si escribes la marca con otro formato, puede no reconocerse.

Utiliza:

```text
[minuto:segundo–minuto:segundo]
```

por ejemplo:

```text
[1:30–2:15]
```

---

# 32. El audio dura menos que los timestamps

No es un error.

Los timestamps no controlan la duración del modelo.

Por ejemplo:

```text
[0:00–0:45]
```

no significa que Chatterbox deba producir exactamente:

```text
45 segundos
```

La duración depende del texto y de la interpretación.

No intentes solucionar una gran diferencia estirando agresivamente el WAV.

---

# 33. La voz habla demasiado rápido

Prueba primero a mejorar:

- puntuación;
- comas;
- puntos;
- pausas naturales;
- longitud de las frases.

También puedes experimentar con:

```text
CFG_WEIGHT
```

pero cambiar parámetros puede modificar otras características de la voz.

Haz pruebas cortas antes de generar un guion completo.

---

# 34. Ralentizar el WAV hace que suene mal

Si intentas aumentar mucho la duración de un audio después de generarlo, puede perder:

- naturalidad;
- ritmo;
- claridad;
- calidad de voz.

Pequeños ajustes pueden ser aceptables.

Grandes diferencias de duración deben resolverse preferentemente mediante:

- guion;
- puntuación;
- edición;
- cantidad de texto.

---

# 35. Una prueba corta suena mejor que un guion largo

Esto puede ocurrir.

Una generación de pocos segundos puede mantener mejor:

- voz;
- ritmo;
- timbre;
- entonación.

Las narraciones largas son más difíciles.

Por eso:

```text
generar_guion.py
```

divide internamente el texto en bloques y después los une.

No es necesario generar todo el guion en una sola llamada.

---

# 36. La voz cambia ligeramente entre bloques

Puede ocurrir incluso utilizando la misma referencia.

La generación es probabilística y cada bloque se genera por separado.

Puedes intentar:

- utilizar una referencia más limpia;
- revisar la puntuación;
- evitar bloques demasiado pequeños;
- evitar bloques demasiado largos;
- mantener una configuración estable.

No existe una garantía de identidad perfecta entre todas las generaciones.

---

# 37. Algunas partes suenan extrañas

Si una parte tiene:

- entonación rara;
- pronunciación extraña;
- cambio de timbre;
- ritmo incorrecto;

primero revisa el texto exacto de esa parte.

La puntuación puede influir considerablemente.

Si el problema no es constante, una nueva generación puede producir un resultado diferente.

---

# 38. Los bloques son demasiado pequeños

El generador utiliza inicialmente:

```python
TARGET_CHARS = 500
HARD_MAX = 650
```

No reduzcas esos valores demasiado sin necesidad.

Generar frases individualmente puede provocar más diferencias entre fragmentos.

---

# 39. Los bloques son demasiado largos

Tampoco aumentes los valores indefinidamente.

Los bloques muy largos pueden provocar:

- degradación;
- ritmo irregular;
- cambios de voz;
- comportamientos inesperados.

La configuración incluida busca un equilibrio razonable.

---

# 40. El programa parece congelado durante `Sampling`

Si ves:

```text
Sampling:
```

y el porcentaje continúa avanzando, no está congelado.

En CPU puede tardar varios minutos por bloque.

No cierres la ventana.

---

# 41. `Sampling` llega a una cantidad diferente en cada bloque

Es normal.

Un bloque puede terminar, por ejemplo, antes de:

```text
1000/1000
```

porque el modelo detecta el final de la generación.

Otro bloque puede necesitar más tokens.

La cantidad de tokens no equivale directamente al número de caracteres del texto.

---

# 42. La generación se interrumpió

Si cerraste la ventana o hubo un fallo durante la generación, puede quedar:

```text
~/ChatterboxES/temp_generacion/
```

La próxima ejecución del generador elimina esa carpeta antes de comenzar.

Si quieres comprobarla manualmente:

```bash
ls ~/ChatterboxES/temp_generacion
```

No contiene modelos importantes.

Es solo almacenamiento temporal.

---

# 43. No aparece el WAV final

Comprueba primero si la consola terminó con:

```text
LISTO
```

Si no apareció, revisa el error anterior en la consola.

Si terminó correctamente, comprueba:

```text
salidas/
```

El nombre deriva del nombre del guion:

```text
guion.txt
```

produce:

```text
guion_voz.wav
```

---

# 44. El WAV anterior desapareció

Si generas de nuevo un guion con el mismo nombre, el archivo final puede sobrescribirse.

Antes de generar otra versión, puedes:

- mover el WAV anterior;
- renombrarlo;
- utilizar otro nombre para el guion.

---

# 45. `ffmpeg: command not found`

Aunque el generador final no depende de FFmpeg para unir los bloques, FFmpeg forma parte del entorno recomendado.

Si falta:

```bash
sudo apt update
sudo apt install -y ffmpeg
```

Comprueba:

```bash
ffmpeg -version
```

---

# 46. Problemas leyendo o escribiendo WAV

Comprueba que está instalado:

```bash
sudo apt install -y libsndfile1
```

También comprueba Torchaudio:

```bash
python -c "import torchaudio; print(torchaudio.__version__)"
```

---

# 47. `git lfs` no existe

Instálalo:

```bash
sudo apt update
sudo apt install -y git-lfs
```

Después:

```bash
git lfs install
```

Comprueba:

```bash
git lfs version
```

---

# 48. El clon del Space está incompleto

Si:

```text
~/ChatterboxES
```

no contiene correctamente:

```text
chatterbox/
```

la descarga puede haber fallado.

Comprueba:

```bash
ls ~/ChatterboxES/chatterbox/src/chatterbox
```

Si la instalación está claramente incompleta y todavía no has personalizado nada dentro de `ChatterboxES`, puedes eliminar esa carpeta y repetir el paso de instalación indicado en:

```text
04_INSTALAR_CHATTERBOX.md
```

No elimines:

```text
~/miniforge3
```

por este problema.

---

# 49. No borres todo cuando aparece un error

La mayoría de los problemas no requieren reinstalar desde cero.

Antes de borrar:

```text
~/ChatterboxES
~/miniforge3
Ubuntu-22.04
```

identifica primero qué componente está fallando.

Normalmente basta con reparar:

- una dependencia;
- una ruta;
- el launcher;
- una versión de `setuptools`;
- la referencia de voz.

---

# 50. Orden recomendado para diagnosticar un fallo

Si no sabes qué está ocurriendo, comprueba en este orden.

## 1. WSL

En PowerShell:

```powershell
wsl --list --verbose
```

Debe aparecer:

```text
Ubuntu-22.04
```

con:

```text
VERSION 2
```

## 2. Entorno

Dentro de Ubuntu:

```bash
conda activate chatterbox
```

## 3. Python

```bash
which python
```

Debe apuntar al entorno `chatterbox`.

## 4. PyTorch

```bash
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

## 5. Chatterbox

```bash
python -m pip show chatterbox-tts
```

## 6. Código es-ES

```bash
cd ~/ChatterboxES
```

```bash
PYTHONPATH="$PWD/chatterbox/src" python -c "from chatterbox.tts import ChatterboxTTS; print('OK')"
```

## 7. Perth

```bash
python -c "import perth; print('OK')"
```

## 8. Modelos

Comprueba que existe:

```text
~/ChatterboxES/hf_cache
```

## 9. Lanzador

Restaura desde GitHub:

```text
Generar voz.bat
launcher.ps1
generar_guion.py
```

si alguno fue modificado accidentalmente.

---

# 51. Si el problema no aparece aquí

Antes de pedir ayuda, guarda:

- mensaje exacto del error;
- las últimas líneas de la consola;
- paso del tutorial donde ocurrió;
- versión de Windows;
- resultado de `wsl --list --verbose`;
- resultado de `python --version`;
- resultado de `python -c "import torch; print(torch.__version__)"`.

No publiques:

- voces privadas;
- guiones privados;
- nombres de usuario;
- rutas personales completas;
- tokens;
- credenciales.

Puedes sustituir información personal por valores genéricos antes de compartir el error.

---

# Instalación terminada

Si:

```text
Generar voz.bat
```

permite seleccionar un guion y una voz y finalmente produce:

```text
salidas/nombre_voz.wav
```

la instalación principal está completa.

Los siguientes archivos del repositorio sirven para proteger datos personales y mantener correctamente la estructura del proyecto:

```text
.gitignore
voces/README.md
salidas/.gitkeep
```
