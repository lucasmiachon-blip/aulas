@echo off
echo ================================================
echo Instalador de FFmpeg
echo ================================================
echo.

echo Verificando se FFmpeg ja esta instalado...
ffmpeg -version >nul 2>&1
if %errorlevel% == 0 (
    echo FFmpeg ja esta instalado!
    pause
    exit /b 0
)

echo FFmpeg nao encontrado. Instalando via winget...
echo.

winget install --id=Gyan.FFmpeg -e --accept-package-agreements --accept-source-agreements

if %errorlevel% == 0 (
    echo.
    echo ================================================
    echo Instalacao concluida!
    echo.
    echo IMPORTANTE: Feche e reabra o terminal para usar o FFmpeg.
    echo ================================================
) else (
    echo.
    echo ================================================
    echo Erro na instalacao.
    echo.
    echo Tente instalar manualmente:
    echo 1. Baixe em: https://ffmpeg.org/download.html
    echo 2. Extraia e adicione ao PATH
    echo ================================================
)

pause


