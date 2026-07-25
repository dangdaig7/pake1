@echo off
REM ============================================
REM Digital Clock - FREE Edition Builder
REM No Login • No Account • 100% Free
REM ============================================

echo.
echo ============================================
echo BUILDING: Digital Clock - FREE Edition
echo ============================================
echo.
echo Step 1: Install dependencies...
pip install PyInstaller pytz -q

echo Step 2: Building digital_clock_free.exe...
echo Please wait (1-2 minutes)...
echo.

python -m PyInstaller --onefile --windowed --name=DigitalClockFREE digital_clock_free.py

echo.
echo ============================================
echo SUCCESS!
echo ============================================
echo.
echo Your FREE .exe file is ready!
echo Location: dist\DigitalClockFREE.exe
echo.
echo Features:
echo  + No login required
echo  + No license key
echo  + No account needed
echo  + Works offline
echo  + Completely free
echo.
echo Run: dist\DigitalClockFREE.exe
echo.
pause
