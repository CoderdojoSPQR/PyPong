@echo off
REM Controlla che Python sia installato
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Installazione di Python...
    installers/python-3.10.0-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
) else (
    echo Python e' gia' installato.
)   

REM Installa la libreria Pygame
echo Installazione libreria Pygame...
python -m pip install installers/pygame-2.6.1-cp310-cp310-win_amd64.whl --no-index --find-links=.
echo Installazione completata.

PAUSE

installers\pygame-2.6.1-cp310-cp310-win_amd64.whl"