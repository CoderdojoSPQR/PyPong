@echo off
setlocal EnableDelayedExpansion
REM Get the directory of the batch script
set "SCRIPT_DIR=%~dp0"

REM Check if Python is installed and its version
for /f "tokens=2 delims= " %%a in ('python --version 2^>nul') do set "PYTHON_VERSION=%%a"
if "%PYTHON_VERSION%"=="" (
    REM No Python installed
    echo No Python detected. Proceeding with Python 3.10 installation...
    goto :InstallPython
) else (
    REM Check if it's Python 3.10
    echo %PYTHON_VERSION% | findstr "3.10" >nul
    if %errorlevel% equ 0 (
        REM Python 3.10 is already installed
        echo Python 3.10 is already installed. Proceeding with Pygame installation...
        goto :InstallWheel
    ) else (
        REM Different Python version installed
        echo Incompatible Python version detected. Creating virtual environment...
        goto :CreateVirtualEnv
    )
)

:InstallPython
REM Check if Python installer exists
if not exist "%SCRIPT_DIR%installers\python-3.10.0-amd64.exe" (
    echo Python installer not found in %SCRIPT_DIR%installers directory.
    pause
    exit /b 1
)
REM Install Python silently to specific directory
echo Installing Python 3.10...
"%SCRIPT_DIR%installers\python-3.10.0-amd64.exe" /passive InstallAllUsers=1 PrependPath=1 TargetDir=C:\Python310 Include_pip=1 Include_test=0
REM Wait for installation
timeout /t 10 >nul
REM Try multiple ways to verify Python
if exist C:\Python310\python.exe (
    echo Python installed successfully to C:\Python310
    C:\Python310\python.exe --version
) else (
    echo Python installation failed.
    pause
    exit /b 1
)
goto :InstallWheel

:CreateVirtualEnv
REM Create virtual environment in CoderDojo
if not exist "C:\CoderDojo" mkdir "C:\CoderDojo"
REM Install Python 3.10 in the virtual environment
echo Creating virtual environment and installing Python 3.10...
"%SCRIPT_DIR%installers\python-3.10.0-amd64.exe" /passive InstallAllUsers=0 PrependPath=0 TargetDir=C:\CoderDojo\Python310 Include_pip=1 Include_test=0
REM Create virtual environment
C:\CoderDojo\Python310\python.exe -m venv C:\CoderDojo\VENV
REM Activate virtual environment and install Pygame
C:\CoderDojo\VENV\Scripts\python.exe -m pip install "%SCRIPT_DIR%installers\pygame-2.6.1-cp310-cp310-win_amd64.whl" --no-index --find-links=.
goto :End

:InstallWheel
REM After Python installation, verify and install pip if needed
if not exist C:\Python310\Scripts\pip.exe (
    echo Pip not found. Bootstrapping pip using local get-pip.py...
    if not exist "%SCRIPT_DIR%installers\get-pip.py" (
        echo get-pip.py not found in the installers directory.
        pause
        exit /b 1
    )
    C:\Python310\python.exe "%SCRIPT_DIR%installers\get-pip.py"
)

REM Verify pip installation
C:\Python310\python.exe -m pip --version
if %errorlevel% neq 0 (
    echo Pip installation failed using local get-pip.py.
    pause
    exit /b 1
)

REM Install Pygame
C:\Python310\python.exe -m pip install "%SCRIPT_DIR%installers\pygame-2.6.1-cp310-cp310-win_amd64.whl" --no-index --find-links=.
goto :End

:End
echo Installation completed successfully.
pause
exit /b 0
