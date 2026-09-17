Add-Type -AssemblyName System.Windows.Forms

$Distro = 'Ubuntu-22.04'

$Base = Split-Path -Parent $MyInvocation.MyCommand.Path

$VocesDir = Join-Path $Base 'voces'
$SalidasDir = Join-Path $Base 'salidas'

$VozDefault = Join-Path $VocesDir 'voz_predeterminada.mp3'
$PythonScript = Join-Path $Base 'generar_guion.py'

function Mostrar-Error {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Mensaje
    )

    [System.Windows.Forms.MessageBox]::Show(
        $Mensaje,
        'Chatterbox Local TTS',
        [System.Windows.Forms.MessageBoxButtons]::OK,
        [System.Windows.Forms.MessageBoxIcon]::Error
    ) | Out-Null
}

# ------------------------------------------------------------
# Comprobaciones basicas
# ------------------------------------------------------------

if (-not (Get-Command wsl.exe -ErrorAction SilentlyContinue)) {
    Mostrar-Error 'No se encuentra WSL. Completa primero la instalacion indicada en la documentacion.'
    exit 1
}

& wsl.exe -d $Distro -- true 2>$null

if ($LASTEXITCODE -ne 0) {
    Mostrar-Error "No se puede iniciar $Distro. Comprueba que Ubuntu 22.04 esta instalado en WSL2."
    exit 1
}

if (-not (Test-Path -LiteralPath $PythonScript -PathType Leaf)) {
    Mostrar-Error 'No se encuentra generar_guion.py en la carpeta del lanzador.'
    exit 1
}

New-Item -ItemType Directory -Force -Path $VocesDir | Out-Null
New-Item -ItemType Directory -Force -Path $SalidasDir | Out-Null

# ------------------------------------------------------------
# Seleccionar guion
# ------------------------------------------------------------

$dlgGuion = New-Object System.Windows.Forms.OpenFileDialog
$dlgGuion.Title = 'Selecciona el guion preparado para TTS'
$dlgGuion.Filter = 'Archivos de texto (*.txt)|*.txt'
$dlgGuion.Multiselect = $false
$dlgGuion.CheckFileExists = $true

if ($dlgGuion.ShowDialog() -ne [System.Windows.Forms.DialogResult]::OK) {
    exit 0
}

$Guion = $dlgGuion.FileName

# ------------------------------------------------------------
# Seleccionar voz
# ------------------------------------------------------------

if (Test-Path -LiteralPath $VozDefault -PathType Leaf) {
    $respuesta = [System.Windows.Forms.MessageBox]::Show(
        'Usar la voz predeterminada?',
        'Chatterbox Local TTS',
        [System.Windows.Forms.MessageBoxButtons]::YesNo,
        [System.Windows.Forms.MessageBoxIcon]::Question
    )

    if ($respuesta -eq [System.Windows.Forms.DialogResult]::Yes) {
        $Voz = $VozDefault
    }
    else {
        $dlgVoz = New-Object System.Windows.Forms.OpenFileDialog
        $dlgVoz.Title = 'Selecciona una voz de referencia'
        $dlgVoz.Filter = 'Audio (*.mp3;*.wav)|*.mp3;*.wav'
        $dlgVoz.Multiselect = $false
        $dlgVoz.CheckFileExists = $true

        if ($dlgVoz.ShowDialog() -ne [System.Windows.Forms.DialogResult]::OK) {
            exit 0
        }

        $Voz = $dlgVoz.FileName
    }
}
else {
    $dlgVoz = New-Object System.Windows.Forms.OpenFileDialog
    $dlgVoz.Title = 'Selecciona una voz de referencia'
    $dlgVoz.Filter = 'Audio (*.mp3;*.wav)|*.mp3;*.wav'
    $dlgVoz.Multiselect = $false
    $dlgVoz.CheckFileExists = $true

    if ($dlgVoz.ShowDialog() -ne [System.Windows.Forms.DialogResult]::OK) {
        exit 0
    }

    $Voz = $dlgVoz.FileName
}

# ------------------------------------------------------------
# Convertir rutas de Windows a rutas WSL
# ------------------------------------------------------------

$WslGuion = (& wsl.exe -d $Distro -- wslpath -a $Guion).Trim()

if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($WslGuion)) {
    Mostrar-Error 'No se pudo convertir la ruta del guion para WSL.'
    exit 1
}

$WslVoz = (& wsl.exe -d $Distro -- wslpath -a $Voz).Trim()

if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($WslVoz)) {
    Mostrar-Error 'No se pudo convertir la ruta de la voz para WSL.'
    exit 1
}

$WslScript = (& wsl.exe -d $Distro -- wslpath -a $PythonScript).Trim()

if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($WslScript)) {
    Mostrar-Error 'No se pudo convertir la ruta de generar_guion.py para WSL.'
    exit 1
}

$WslSalidas = (& wsl.exe -d $Distro -- wslpath -a $SalidasDir).Trim()

if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($WslSalidas)) {
    Mostrar-Error 'No se pudo convertir la ruta de la carpeta salidas para WSL.'
    exit 1
}

# ------------------------------------------------------------
# Localizar Python dentro del entorno de Miniforge
# ------------------------------------------------------------

$WslHome = (& wsl.exe -d $Distro -- printenv HOME).Trim()

if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($WslHome)) {
    Mostrar-Error 'No se pudo localizar la carpeta HOME dentro de Ubuntu.'
    exit 1
}

$WslPython = $WslHome + '/miniforge3/envs/chatterbox/bin/python'

& wsl.exe -d $Distro -- test -x $WslPython

if ($LASTEXITCODE -ne 0) {
    Mostrar-Error 'No se encuentra el entorno Python de Chatterbox. Revisa 03_PREPARAR_ENTORNO.md.'
    exit 1
}

# ------------------------------------------------------------
# Mostrar informacion de la generacion
# ------------------------------------------------------------

Write-Host ''
Write-Host '========================================'
Write-Host ' CHATTERBOX LOCAL TTS'
Write-Host '========================================'
Write-Host ''
Write-Host 'Guion:'
Write-Host $Guion
Write-Host ''
Write-Host 'Voz:'
Write-Host $Voz
Write-Host ''
Write-Host 'Generando...'
Write-Host ''

# ------------------------------------------------------------
# Ejecutar generar_guion.py dentro de WSL
#
# Los argumentos se pasan por separado para soportar
# correctamente rutas de Windows que contienen espacios.
# ------------------------------------------------------------

$ArgumentosWSL = @(
    '-d'
    $Distro
    '--'
    $WslPython
    $WslScript
    '--guion'
    $WslGuion
    '--voz'
    $WslVoz
    '--salida-dir'
    $WslSalidas
)

& wsl.exe @ArgumentosWSL

$CodigoSalida = $LASTEXITCODE

if ($CodigoSalida -ne 0) {
    Write-Host ''
    Write-Host '========================================'
    Write-Host ' LA GENERACION HA FALLADO'
    Write-Host '========================================'
    Write-Host ''
    Write-Host 'Revisa el mensaje de error mostrado arriba.'
    Write-Host ''
    Read-Host 'Pulsa ENTER para cerrar'
    exit $CodigoSalida
}

# ------------------------------------------------------------
# Generacion terminada
# ------------------------------------------------------------

Write-Host ''
Write-Host '========================================'
Write-Host ' GENERACION TERMINADA'
Write-Host '========================================'
Write-Host ''

Start-Process explorer.exe -ArgumentList $SalidasDir

Read-Host 'Pulsa ENTER para cerrar'

exit 0
