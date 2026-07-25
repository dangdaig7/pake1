@echo off
REM ============================================
REM AB1 - Build Script
REM Creates AB1.exe from AB1.py
REM ============================================

echo.
echo ============================================
echo AB1 - Building Application
echo ============================================
echo.

echo Step 1: Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo OK: Python found

echo.
echo Step 2: Installing PyInstaller...
pip install PyInstaller -q
if errorlevel 1 (
    echo ERROR: Failed to install PyInstaller
    pause
    exit /b 1
)
echo OK: PyInstaller ready

echo.
echo Step 3: Building AB1.exe...
echo This may take 1-2 minutes, please wait...
echo.

python -m PyInstaller --onefile --windowed --name=AB1 AB1.py

if errorlevel 1 (
    echo ERROR: Build failed
    pause
    exit /b 1
)

echo.
echo ============================================
echo SUCCESS!
echo ============================================
echo.
echo File: dist\AB1.exe
echo Size: ~60 MB
echo.
echo FEATURES:
echo  + No login required
echo  + No license key
echo  + No account needed
echo  + Unlimited usage
echo  + Complete offline
echo.
echo Run: dist\AB1.exe
echo.
pause
