@echo off
REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python non rilevato, avvio installazione di Python 3.10...
    installers/python-3.10.0-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
    goto :InstallWheel
)

REM Retrieve the installed Python version
for /f "tokens=2 delims= " %%a in ('python --version') do set PYTHON_VERSION=%%a
echo Versione Python rilevata: %PYTHON_VERSION%

REM Check if Python version is 3.10
echo %PYTHON_VERSION% | findstr "3.10" >nul
if %errorlevel% equ 0 (
    echo Python 3.10 rilevato. Procedo con l'installazione della libreria Pygame...
    goto :InstallWheel
)

REM Another Python version is installed
echo Versione Python non compatibile. Creo un ambiente virtuale con Python 3.10...

REM Define the path for the virtual environment
set VENV_PATH="C:\Program Files\Python310_VENV"

REM Create the virtual environment
installers/python-3.10.0-amd64.exe /quiet InstallAllUsers=1 TargetDir=%VENV_PATH% PrependPath=1

REM Use the virtual environment's Python executable
set PYTHON_EXEC=%VENV_PATH%\python.exe

REM Install the wheel in the virtual environment
%PYTHON_EXEC% -m pip install installers/pygame-2.6.1-cp310-cp310-win_amd64.whl --no-index --find-links=.
echo Installazione completata.
goto :End

:InstallWheel
REM Install the Pygame wheel using the default Python installation
pip install installers/pygame-2.6.1-cp310-cp310-win_amd64.whl --no-index --find-links=.
echo Installazione completata.
goto :End

:End
PAUSE
