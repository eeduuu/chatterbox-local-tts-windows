# 02 - Instalar WSL2 y Ubuntu 22.04

En este paso instalaremos **WSL2** y **Ubuntu 22.04**.

Chatterbox se ejecutará dentro de Ubuntu, aunque después lo utilizaremos desde Windows mediante el lanzador incluido en el repositorio.

---

# 1. Abrir PowerShell como administrador

En Windows:

1. Abre el menú Inicio.
2. Busca:

```text
PowerShell
```

3. Haz clic derecho sobre **Windows PowerShell**.
4. Pulsa:

```text
Ejecutar como administrador
```

Acepta el aviso de Windows.

---

# 2. Comprobar las distribuciones disponibles

Ejecuta:

```powershell
wsl --list --online
```

Debería aparecer una lista de distribuciones disponibles.

Busca:

```text
Ubuntu-22.04
```

Si aparece, continúa.

---

# 3. Instalar Ubuntu 22.04

Ejecuta:

```powershell
wsl --install -d Ubuntu-22.04
```

Windows instalará:

- WSL;
- los componentes necesarios de virtualización;
- WSL2;
- Ubuntu 22.04.

La descarga puede tardar varios minutos.

---

# 4. Reiniciar Windows

Si Windows solicita reiniciar el equipo, hazlo.

Después del reinicio, Ubuntu puede abrirse automáticamente.

Si no se abre, busca en el menú Inicio:

```text
Ubuntu 22.04
```

y ejecútalo.

---

# 5. Crear el usuario de Ubuntu

La primera vez que Ubuntu arranque terminará de preparar sus archivos.

Después pedirá crear un usuario Linux.

Aparecerá algo parecido a:

```text
Enter new UNIX username:
```

Escribe el nombre que quieras utilizar.

Por ejemplo:

```text
usuario
```

No es necesario que coincida con tu usuario de Windows.

Después pedirá una contraseña:

```text
New password:
```

Escribe una contraseña y pulsa ENTER.

Ubuntu no muestra:

```text
****
```

ni ningún otro carácter mientras escribes la contraseña.

Es normal.

Vuelve a escribirla cuando lo solicite.

Guarda esta contraseña porque puede pedirse más adelante al utilizar `sudo`.

---

# 6. Comprobar que Ubuntu funciona

Cuando termine deberías ver una línea parecida a:

```text
usuario@PC:~$
```

Eso significa que estás dentro de Ubuntu.

Ejecuta:

```bash
pwd
```

Debería mostrar una ruta similar a:

```text
/home/usuario
```

El nombre dependerá del usuario que hayas creado.

---

# 7. Salir de Ubuntu

Puedes cerrar la ventana o ejecutar:

```bash
exit
```

---

# 8. Comprobar que utiliza WSL2

Abre una ventana normal de PowerShell y ejecuta:

```powershell
wsl --list --verbose
```

Deberías obtener algo similar a:

```text
NAME            STATE           VERSION
Ubuntu-22.04    Stopped         2
```

Lo importante es que:

```text
Ubuntu-22.04
```

aparezca con:

```text
VERSION 2
```

---

# Si aparece VERSION 1

Si Ubuntu aparece utilizando WSL 1, ejecuta:

```powershell
wsl --set-version Ubuntu-22.04 2
```

Espera a que termine.

Después comprueba de nuevo:

```powershell
wsl --list --verbose
```

Debe aparecer:

```text
VERSION 2
```

---

# 9. Actualizar WSL

Ejecuta en PowerShell:

```powershell
wsl --update
```

Cuando termine puedes comprobar el estado con:

```powershell
wsl --status
```

---

# 10. Abrir Ubuntu desde PowerShell

A partir de ahora puedes entrar directamente en Ubuntu ejecutando:

```powershell
wsl -d Ubuntu-22.04
```

Deberías volver a ver:

```text
usuario@PC:~$
```

Los comandos de los siguientes pasos se ejecutarán dentro de esta terminal de Ubuntu salvo que se indique expresamente lo contrario.

---

# Si WSL ya estaba instalado

No es necesario reinstalarlo.

Comprueba primero:

```powershell
wsl --list --verbose
```

Si ya aparece:

```text
Ubuntu-22.04
```

con:

```text
VERSION 2
```

puedes continuar directamente con el siguiente documento.

---

# Si tienes WSL pero no Ubuntu 22.04

Comprueba las distribuciones instaladas:

```powershell
wsl --list --verbose
```

Si `Ubuntu-22.04` no aparece, instálala con:

```powershell
wsl --install -d Ubuntu-22.04
```

No es necesario eliminar otras distribuciones de Linux que tengas instaladas.

---

# Error: la instalación se queda en 0 %

Si:

```powershell
wsl --install -d Ubuntu-22.04
```

se queda bloqueado durante la descarga, prueba:

```powershell
wsl --install --web-download -d Ubuntu-22.04
```

Esta opción descarga la distribución directamente en lugar de depender de Microsoft Store.

---

# Error relacionado con virtualización

Si WSL2 muestra un error indicando que no puede utilizar la plataforma de máquina virtual, comprueba primero que la virtualización está habilitada.

Puedes verlo desde:

```text
Administrador de tareas
→ Rendimiento
→ CPU
```

Busca:

```text
Virtualización: Habilitada
```

Si aparece deshabilitada, puede ser necesario activarla desde la BIOS/UEFI.

Dependiendo del procesador puede aparecer como:

```text
Intel Virtualization Technology
Intel VT-x
AMD-V
SVM Mode
```

No cambies estas opciones si WSL2 ya funciona correctamente.

---

# Error: Ubuntu no aparece después de instalar

Ejecuta:

```powershell
wsl --list --verbose
```

Si `Ubuntu-22.04` aparece en la lista, puedes iniciarla manualmente con:

```powershell
wsl -d Ubuntu-22.04
```

---

# Comprobación final

Antes de continuar debes tener:

```text
WSL instalado
Ubuntu-22.04 instalado
Ubuntu ejecutándose con WSL2
Usuario Linux creado
Contraseña Linux creada
```

La comprobación principal es:

```powershell
wsl --list --verbose
```

y debe mostrar algo equivalente a:

```text
Ubuntu-22.04    Stopped    2
```

El estado puede aparecer como:

```text
Running
```

o:

```text
Stopped
```

Ambos son normales.

Lo importante es:

```text
VERSION 2
```

---

# Siguiente paso

Continúa con:

```text
03_PREPARAR_ENTORNO.md
```
