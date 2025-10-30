@echo off
REM Quick build script for Windows
echo CS2 Font Modifier - Build Script
echo ================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Please install Python 3.6 or higher
    pause
    exit /b 1
)

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Run build script
echo.
echo Running build script...
python build_exe.py

pause
