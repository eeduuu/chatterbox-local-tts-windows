# 03 - Preparar el entorno

En este paso prepararemos Ubuntu para Chatterbox.

Instalaremos:

- herramientas básicas de Linux;
- Git y Git LFS;
- FFmpeg;
- Miniforge;
- un entorno aislado llamado `chatterbox`;
- Python 3.11;
- PyTorch 2.6.0 para CPU.

Todavía no instalaremos el modelo de Chatterbox. Eso se hará en el siguiente paso.

---

# 1. Entrar en Ubuntu

Abre PowerShell y ejecuta:

```powershell
wsl -d Ubuntu-22.04
```

Cuando estés dentro de Ubuntu verás algo parecido a:

```text
usuario@PC:~$
```

Aunque estés utilizando una ventana que abriste desde PowerShell, a partir de este momento los comandos se están ejecutando dentro de Ubuntu.

Todos los comandos de este archivo deben ejecutarse ahí.

---

# 2. Actualizar la lista de paquetes

Ejecuta:

```bash
sudo apt update
```

Ubuntu puede pedir la contraseña que creaste durante la instalación.

Mientras escribes la contraseña no aparecerán caracteres en pantalla.

Es normal.

---

# 3. Instalar las herramientas necesarias

Ejecuta:

```bash
sudo apt install -y git git-lfs wget curl unzip ffmpeg libsndfile1 build-essential
```

Esto instala:

- `git`: descarga de repositorios;
- `git-lfs`: descarga de archivos grandes almacenados con Git LFS;
- `wget` y `curl`: descargas desde terminal;
- `unzip`: extracción de archivos;
- `ffmpeg`: manejo y conversión de audio;
- `libsndfile1`: lectura y escritura de audio desde Python;
- `build-essential`: herramientas necesarias para compilar algunas dependencias.

---

# 4. Activar Git LFS

Ejecuta:

```bash
git lfs install
```

Debería aparecer un mensaje parecido a:

```text
Git LFS initialized.
```

Puedes comprobarlo con:

```bash
git lfs version
```

---

# 5. Comprobar FFmpeg

Ejecuta:

```bash
ffmpeg -version
```

Si aparece información sobre la versión de FFmpeg, está correctamente instalado.

Pulsa:

```text
q
```

solo si algún comando deja una pantalla de información abierta.

Normalmente no será necesario.

---

# 6. Descargar Miniforge

Utilizaremos Miniforge para mantener Chatterbox aislado del resto de Python del sistema.

Ve a tu carpeta personal:

```bash
cd ~
```

Descarga el instalador oficial:

```bash
wget -O Miniforge3.sh "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
```

En un PC x86-64 normal con Ubuntu debería descargar el instalador de Linux correspondiente.

---

# 7. Instalar Miniforge

Instálalo exactamente en:

```text
~/miniforge3
```

Ejecuta:

```bash
bash Miniforge3.sh -b -p "$HOME/miniforge3"
```

Esta ruta es importante porque los scripts incluidos en este repositorio esperan encontrar Miniforge en:

```text
$HOME/miniforge3
```

Cuando termine, elimina únicamente el instalador descargado:

```bash
rm Miniforge3.sh
```

No elimines la carpeta:

```text
~/miniforge3
```

---

# 8. Activar Conda

Ejecuta:

```bash
source "$HOME/miniforge3/etc/profile.d/conda.sh"
```

Después inicializa Conda para Bash:

```bash
conda init bash
```

Recarga la configuración de la terminal:

```bash
source ~/.bashrc
```

Comprueba que Conda funciona:

```bash
conda --version
```

Debería mostrar una versión de Conda.

---

# 9. Crear el entorno de Chatterbox

Crea un entorno independiente con Python 3.11:

```bash
conda create -n chatterbox python=3.11 -y
```

El nombre:

```text
chatterbox
```

es importante.

El lanzador que instalaremos más adelante espera encontrar el entorno en:

```text
~/miniforge3/envs/chatterbox
```

No utilices otro nombre salvo que después quieras modificar los scripts.

---

# 10. Activar el entorno

Ejecuta:

```bash
conda activate chatterbox
```

La terminal debería cambiar de algo parecido a:

```text
usuario@PC:~$
```

a:

```text
(chatterbox) usuario@PC:~$
```

Mientras aparezca:

```text
(chatterbox)
```

los comandos de Python se ejecutarán dentro del entorno correcto.

---

# 11. Comprobar Python

Ejecuta:

```bash
python --version
```

Debe aparecer:

```text
Python 3.11.x
```

El último número puede cambiar.

No es necesario que coincida exactamente con una versión concreta mientras sea Python 3.11.

Comprueba también qué Python se está utilizando:

```bash
which python
```

La ruta debe ser parecida a:

```text
/home/usuario/miniforge3/envs/chatterbox/bin/python
```

No debe apuntar al Python general de Ubuntu.

---

# 12. Preparar pip y setuptools

Ejecuta:

```bash
python -m pip install --upgrade pip wheel
```

Después instala una versión de `setuptools` anterior a la 81:

```bash
python -m pip install "setuptools<81"
```

Este límite es intencionado.

Algunas versiones de Perth utilizadas por Chatterbox dependen todavía de `pkg_resources`.

Con versiones recientes de `setuptools` puede aparecer un error al inicializar Perth.

Mantener:

```text
setuptools < 81
```

evita ese problema en esta instalación.

---

# 13. Instalar PyTorch para CPU

Esta guía está diseñada para funcionar sin CUDA.

Instala PyTorch 2.6.0 y Torchaudio 2.6.0 utilizando específicamente los paquetes para CPU:

```bash
python -m pip install torch==2.6.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cpu
```

La descarga puede tardar.

No cierres la terminal mientras se instala.

---

# 14. Comprobar PyTorch

Ejecuta:

```bash
python -c "import torch; print('PyTorch:', torch.__version__); print('CUDA disponible:', torch.cuda.is_available())"
```

Deberías obtener algo parecido a:

```text
PyTorch: 2.6.0+cpu
CUDA disponible: False
```

Lo importante es que PyTorch funcione.

En esta guía:

```text
CUDA disponible: False
```

es completamente normal.

Estamos utilizando CPU.

---

# 15. Comprobar Torchaudio

Ejecuta:

```bash
python -c "import torchaudio; print('Torchaudio:', torchaudio.__version__)"
```

Debería mostrar una versión 2.6.0.

---

# 16. Comprobación completa del entorno

Ejecuta:

```bash
python -c "import sys, torch, torchaudio; print('Python:', sys.version.split()[0]); print('Torch:', torch.__version__); print('Torchaudio:', torchaudio.__version__); print('CUDA:', torch.cuda.is_available())"
```

El resultado debe ser parecido a:

```text
Python: 3.11.x
Torch: 2.6.0+cpu
Torchaudio: 2.6.0+cpu
CUDA: False
```

Las versiones pueden mostrar o no el sufijo:

```text
+cpu
```

según el paquete instalado.

---

# 17. Estado correcto antes de continuar

Tu terminal debería mostrar:

```text
(chatterbox) usuario@PC:~$
```

Y debes tener:

```text
~/miniforge3/
```

con el entorno:

```text
~/miniforge3/envs/chatterbox/
```

No borres ninguna de estas carpetas.

---

# Abrir nuevamente el entorno otro día

Si cierras la terminal y vuelves más adelante, entra primero en Ubuntu:

```powershell
wsl -d Ubuntu-22.04
```

Normalmente Conda ya estará disponible porque ejecutamos:

```bash
conda init bash
```

Activa el entorno con:

```bash
conda activate chatterbox
```

Debes volver a ver:

```text
(chatterbox)
```

antes del nombre de usuario.

---

# Error: `conda: command not found`

Si después de instalar Miniforge aparece:

```text
conda: command not found
```

ejecuta:

```bash
source "$HOME/miniforge3/etc/profile.d/conda.sh"
```

y después:

```bash
conda init bash
```

Recarga la terminal:

```bash
source ~/.bashrc
```

Comprueba otra vez:

```bash
conda --version
```

---

# Error: el entorno no está activo

Si no aparece:

```text
(chatterbox)
```

al principio de la terminal, ejecuta:

```bash
conda activate chatterbox
```

Antes de instalar Chatterbox debes estar dentro de ese entorno.

---

# Error: el entorno `chatterbox` ya existe

Si ejecutas:

```bash
conda create -n chatterbox python=3.11 -y
```

y Conda indica que el entorno ya existe, no lo vuelvas a crear.

Actívalo:

```bash
conda activate chatterbox
```

y comprueba:

```bash
python --version
```

Si muestra Python 3.11 puedes continuar.

---

# Error relacionado con `pkg_resources`

Si más adelante aparece un aviso parecido a:

```text
pkg_resources is deprecated
```

pero el programa continúa funcionando, el aviso por sí solo no es un error.

Si Perth falla al cargarse, comprueba dentro del entorno:

```bash
python -m pip show setuptools
```

y vuelve a aplicar:

```bash
python -m pip install "setuptools<81"
```

Este problema se explica también en:

```text
08_ERRORES_Y_SOLUCIONES.md
```

---

# No instales CUDA para esta guía

No instales:

```text
CUDA Toolkit
cuDNN
NVIDIA drivers adicionales
```

solo para seguir este tutorial.

No son necesarios para la configuración CPU que estamos preparando.

---

# No instales Chatterbox todavía

Al terminar este archivo debes tener preparado el entorno, pero todavía no es necesario ejecutar:

```text
pip install chatterbox-tts
```

La instalación de Chatterbox y del modelo específico de español de España se hará en el siguiente paso para mantener la instalación ordenada.

---

# Comprobación final

Antes de continuar deben funcionar todos estos comandos:

```bash
git --version
```

```bash
git lfs version
```

```bash
ffmpeg -version
```

```bash
conda --version
```

```bash
python --version
```

```bash
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

Y la terminal debe comenzar con:

```text
(chatterbox)
```

---

# Siguiente paso

Continúa con:

```text
04_INSTALAR_CHATTERBOX.md
```
