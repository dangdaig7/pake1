"""
Build script to create .exe file from digital_clock.py
Run this script to generate the executable file

Usage:
    python build_exe.py
"""

import subprocess
import sys
import os
import shutil

def build_exe():
    """Build .exe file using PyInstaller"""
    
    print("=" * 60)
    print("🔨 Digital Clock - Building .exe Installer")
    print("=" * 60)
    
    # Step 1: Check if PyInstaller is installed
    print("\n[1/4] Checking PyInstaller installation...")
    try:
        import PyInstaller
        print("✅ PyInstaller found!")
    except ImportError:
        print("❌ PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstaller installed!")
    
    # Step 2: Build the .exe
    print("\n[2/4] Building .exe file...")
    print("This may take 1-2 minutes...\n")
    
    build_command = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--onefile",  # Create single .exe file
        "--windowed",  # No console window
        "--name=DigitalClock",  # Name of executable
        "--icon=clock_icon.ico",  # Icon (if available)
        "--add-data=.;.",  # Add data files
        "digital_clock.py"
    ]
    
    try:
        subprocess.check_call(build_command)
        print("\n✅ Build completed!")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Build failed with error: {e}")
        return False
    
    # Step 3: Locate the .exe
    print("\n[3/4] Locating the generated .exe file...")
    exe_path = os.path.join("dist", "DigitalClock.exe")
    
    if os.path.exists(exe_path):
        exe_size = os.path.getsize(exe_path) / (1024 * 1024)  # Size in MB
        print(f"✅ Found: {exe_path}")
        print(f"   File size: {exe_size:.2f} MB")
    else:
        print(f"❌ .exe not found at {exe_path}")
        return False
    
    # Step 4: Cleanup
    print("\n[4/4] Cleaning up temporary files...")
    if os.path.exists("build"):
        shutil.rmtree("build")
        print("✅ Removed build folder")
    
    if os.path.exists("DigitalClock.spec"):
        os.remove("DigitalClock.spec")
        print("✅ Removed .spec file")
    
    # Final message
    print("\n" + "=" * 60)
    print("🎉 SUCCESS! Your .exe is ready!")
    print("=" * 60)
    print(f"\n📍 Location: {exe_path}")
    print(f"\n📋 Next steps:")
    print(f"   1. Find 'DigitalClock.exe' in the 'dist' folder")
    print(f"   2. Double-click to run the application")
    print(f"   3. Or create a shortcut on your desktop")
    print(f"   4. Share the .exe with others or install on other computers")
    print("\n✨ No installation required - just run and enjoy!\n")
    
    return True


if __name__ == "__main__":
    success = build_exe()
    sys.exit(0 if success else 1)
