@echo off
title Calculo de Acero en Zapata - Python
:: Cambiar a la carpeta donde reside el script
cd /c/python/ "%~dp0"

echo ====================================================
echo   EJECUTANDO: calc_zapata_central_steel.py
echo ====================================================
echo.

:: Intentamos ejecutar con 'python', que es el estandar en Windows
python calc_zapata_central_steel.py

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Hubo un problema al ejecutar el script.
    echo Asegurate de que Python este en el PATH.
    pause
) else (
    echo.
    echo [OK] Calculo finalizado con exito.
    pause
)


