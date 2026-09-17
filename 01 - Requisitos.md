# 01 - Requisitos

Antes de instalar nada, comprueba que el equipo cumple estos requisitos.

Esta guía está pensada para ejecutar **Chatterbox TTS localmente en Windows usando WSL2 y CPU**, sin necesidad de una GPU NVIDIA.

---

# Sistema operativo

Necesitas:

- Windows 10 o Windows 11.
- Sistema de 64 bits.
- Arquitectura x86-64.
- WSL2 disponible.
- Permisos de administrador para instalar WSL.

Esta guía utiliza específicamente:

```text
Ubuntu 22.04
```

dentro de WSL2.

No está documentada ni probada en esta guía una instalación sobre Windows ARM64.

---

# Procesador

No es obligatorio utilizar un procesador concreto.

La configuración está orientada a procesadores x86-64 modernos de:

- Intel;
- AMD.

Chatterbox se ejecutará utilizando la CPU.

Cuanto más rápido sea el procesador, menos tardará la generación.

En equipos modestos puede funcionar igualmente, pero una narración de varios minutos puede tardar bastante en generarse.

---

# Memoria RAM

Recomendado:

```text
16 GB de RAM
```

Con menos memoria podría funcionar dependiendo del sistema y de los programas abiertos, pero esta guía no está pensada ni validada específicamente para equipos con poca RAM.

Durante una generación larga es recomendable no tener abiertas aplicaciones innecesariamente pesadas.

---

# Tarjeta gráfica

No necesitas:

```text
GPU NVIDIA
CUDA
```

La instalación de esta guía utiliza:

```text
PyTorch CPU
```

Por tanto, también puede utilizarse en equipos con gráficos integrados.

Tener una GPU NVIDIA compatible podría permitir otras configuraciones más rápidas, pero eso queda fuera del alcance de esta guía.

El objetivo aquí es disponer de una instalación que funcione sin depender de CUDA.

---

# Espacio en disco

Necesitas varios GB libres para:

- Ubuntu mediante WSL2;
- Miniforge;
- entorno de Python;
- PyTorch;
- dependencias;
- código de Chatterbox;
- modelos de voz;
- caché de Hugging Face.

El modelo utilizado descarga varios archivos grandes.

Se recomienda disponer de al menos:

```text
15 GB libres
```

antes de comenzar.

Tener más espacio disponible es aconsejable si vas a mantener varios modelos, voces o audios generados.

---

# Conexión a Internet

Necesitas conexión a Internet durante la instalación para:

- instalar Ubuntu;
- instalar paquetes de Linux;
- descargar Miniforge;
- instalar paquetes de Python;
- clonar Chatterbox;
- descargar los modelos desde Hugging Face.

Una vez descargados los modelos necesarios, la generación de voz puede realizarse localmente.

---

# PowerShell

Necesitas poder abrir:

```text
Windows PowerShell
```

o una terminal equivalente con PowerShell.

Durante la instalación utilizaremos PowerShell para:

- instalar WSL;
- abrir Ubuntu;
- ejecutar algunos comandos iniciales.

Después de terminar la instalación, el uso habitual se hará mediante:

```text
Generar voz.bat
```

y no será necesario escribir comandos manualmente cada vez.

---

# Virtualización

WSL2 necesita virtualización.

En la mayoría de equipos modernos ya está disponible o Windows puede configurar los componentes necesarios durante la instalación de WSL.

Si WSL2 no puede iniciarse y muestra errores relacionados con virtualización, comprueba que la virtualización esté habilitada en la BIOS/UEFI.

Dependiendo del fabricante puede aparecer con nombres como:

```text
Intel Virtualization Technology
Intel VT-x
AMD-V
SVM Mode
```

No cambies opciones de BIOS/UEFI si WSL funciona correctamente.

---

# No necesitas instalar previamente

No necesitas instalar manualmente antes de seguir esta guía:

```text
Python para Windows
Docker Desktop
CUDA
cuDNN
Anaconda
Git para Windows
FFmpeg para Windows
```

Las herramientas necesarias para Chatterbox se instalarán dentro de Ubuntu mediante WSL2.

Si alguna de ellas ya está instalada en Windows, no es necesario eliminarla.

Simplemente no forma parte de esta instalación.

---

# Voz de referencia

Para utilizar clonación de voz necesitarás un archivo de audio.

Formatos recomendados para este proyecto:

```text
.mp3
.wav
```

Conviene utilizar una grabación:

- con una sola persona hablando;
- sin música;
- sin efectos;
- sin ruido fuerte de fondo;
- sin reverberación excesiva;
- con volumen claro;
- con voz natural.

No necesitas una grabación de varios minutos.

Una muestra corta y limpia puede ser suficiente.

La calidad de la referencia influye directamente en el resultado.

Utiliza únicamente una voz propia o una voz para la que tengas permiso.

---

# Editor de texto

Necesitarás editar algunos archivos durante la instalación.

Puedes utilizar:

```text
Visual Studio Code
Bloc de notas
Notepad++
```

Para los archivos `.py` y `.ps1` es recomendable utilizar Visual Studio Code o un editor equivalente porque facilita detectar errores de formato.

Para archivos `.txt`, cualquier editor de texto sirve.

---

# Navegador

Necesitarás un navegador únicamente para tareas como:

- consultar este repositorio;
- descargar archivos si no utilizas Git;
- acceder a GitHub o Hugging Face si fuese necesario.

No necesitas utilizar ninguna interfaz web para generar las voces una vez terminada la instalación.

---

# Rendimiento esperado

Esta guía prioriza:

```text
compatibilidad
funcionamiento local
uso sin NVIDIA
simplicidad
```

No está diseñada para conseguir generación en tiempo real.

En CPU:

- una frase corta puede tardar varios segundos;
- un bloque largo puede tardar uno o varios minutos;
- un guion completo puede tardar bastante más que su duración final.

Esto es normal.

El porcentaje mostrado durante:

```text
Sampling
```

corresponde al proceso de generación y no a la duración final del audio.

---

# Compatibilidad resumida

## Adecuado para esta guía

```text
Windows 10/11
x86-64
WSL2
Ubuntu 22.04
CPU Intel o AMD
16 GB RAM recomendados
sin NVIDIA
sin CUDA
```

## No cubierto por esta guía

```text
macOS
Linux instalado directamente como sistema principal
Windows ARM64
GPU NVIDIA / CUDA
AMD ROCm
Docker
servidores remotos
generación en tiempo real
```

Algunas de estas configuraciones pueden funcionar con Chatterbox, pero requieren una instalación diferente y no forman parte de este tutorial.

---

# Siguiente paso

Si el equipo cumple los requisitos, continúa con:

```text
02_INSTALAR_WSL.md
```
