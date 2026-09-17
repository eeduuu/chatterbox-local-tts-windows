@echo off
setlocal

chcp 65001 >nul
title Chatterbox Local TTS

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0launcher.ps1"

set "EXITCODE=%ERRORLEVEL%"

if not "%EXITCODE%"=="0" (
    echo.
    echo Ha ocurrido un error.
    echo.
    pause
)

exit /b %EXITCODE%
