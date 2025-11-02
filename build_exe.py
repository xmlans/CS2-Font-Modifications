#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build script for CS2 Font Modifier
Creates executable with PyInstaller including all necessary fonts
"""

import os
import sys
import subprocess
import shutil

def check_pyinstaller():
    """Check if PyInstaller is installed"""
    try:
        import PyInstaller
        print(f"✓ PyInstaller {PyInstaller.__version__} found")
        return True
    except ImportError:
        print("❌ PyInstaller not found")
        print("\nPlease install PyInstaller:")
        print("  pip install pyinstaller")
        return False

def check_dependencies():
    """Check if all dependencies are installed"""
    dependencies = ['fonttools']
    missing = []

    for dep in dependencies:
        try:
            __import__(dep.replace('-', '_'))
            print(f"✓ {dep} found")
        except ImportError:
            print(f"❌ {dep} not found")
            missing.append(dep)

    if missing:
        print(f"\nPlease install missing dependencies:")
        print(f"  pip install {' '.join(missing)}")
        return False
    return True

def check_font_files():
    """Check if required font files exist"""
    required_fonts = {
        'cs2en.otf': 'English font (primary)',
        'cs2sc.ttf': 'Chinese font (fallback)'
    }

    missing = []
    for font, description in required_fonts.items():
        if os.path.isfile(font):
            size = os.path.getsize(font) / 1024
            print(f"✓ {font} ({description}) - {size:.1f} KB")
        else:
            print(f"❌ {font} ({description}) - NOT FOUND")
            missing.append(font)

    # Check for default font (cs2.otf or cs2en.otf)
    if not os.path.isfile('cs2.otf'):
        if os.path.isfile('cs2en.otf'):
            print("  Note: cs2.otf not found, will use cs2en.otf as default")
        else:
            print("❌ No default font found (cs2.otf or cs2en.otf)")
            missing.append('cs2.otf or cs2en.otf')

    if missing:
        print(f"\n❌ Missing font files: {', '.join(missing)}")
        return False
    return True

def clean_build():
    """Clean previous build artifacts"""
    dirs_to_clean = ['build', 'dist', '__pycache__']
    files_to_clean = ['cs2change.spec']

    print("\nCleaning previous build artifacts...")
    for d in dirs_to_clean:
        if os.path.exists(d):
            shutil.rmtree(d)
            print(f"  Removed {d}/")

    for f in files_to_clean:
        if os.path.exists(f):
            os.remove(f)
            print(f"  Removed {f}")

def build_exe():
    """Build executable with PyInstaller"""
    print("\n" + "="*60)
    print("Building CS2 Font Modifier v2.0 executable...")
    print("="*60 + "\n")

    # Determine data files to include
    data_files = [
        ('cs2sc.ttf', '.'),  # Chinese fallback font
    ]

    # Add default font (prefer cs2en.otf, fallback to cs2.otf)
    if os.path.isfile('cs2en.otf'):
        data_files.append(('cs2en.otf', '.'))
        # Also add as cs2.otf for compatibility
        print("Will package cs2en.otf as both cs2en.otf and cs2.otf")
        # Copy cs2en.otf to cs2.otf temporarily
        if not os.path.isfile('cs2.otf'):
            shutil.copy2('cs2en.otf', 'cs2.otf')
        data_files.append(('cs2.otf', '.'))
    elif os.path.isfile('cs2.otf'):
        data_files.append(('cs2.otf', '.'))

    # Build PyInstaller command
    cmd = [
        'pyinstaller',
        '--onefile',                    # Single executable
        '--console',                    # Console window (required for input())
        '--name=cs2change',             # Output name
        '--icon=NONE',                  # No icon (you can add one later)
        '--clean',                      # Clean cache
    ]

    # Add data files
    for src, dst in data_files:
        cmd.append(f'--add-data={src}{os.pathsep}{dst}')

    # Add the main script
    cmd.append('cs2change.py')

    print("PyInstaller command:")
    print(" ".join(cmd))
    print()

    # Run PyInstaller
    try:
        result = subprocess.run(cmd, check=True)
        print("\n" + "="*60)
        print("✓ Build successful!")
        print("="*60)
        print(f"\nExecutable location: dist/cs2change.exe")
        print(f"Size: {os.path.getsize('dist/cs2change.exe') / (1024*1024):.2f} MB")
        return True
    except subprocess.CalledProcessError as e:
        print("\n" + "="*60)
        print("❌ Build failed!")
        print("="*60)
        print(f"\nError: {e}")
        return False

def main():
    """Main build process"""
    print("CS2 Font Modifier - Build Script v2.0")
    print("="*60 + "\n")

    # Check prerequisites
    print("Checking prerequisites...\n")

    if not check_pyinstaller():
        sys.exit(1)

    if not check_dependencies():
        sys.exit(1)

    if not check_font_files():
        sys.exit(1)

    print("\n✓ All prerequisites met!\n")

    # Confirm build
    response = input("Proceed with build? (y/n): ").strip().lower()
    if response != 'y':
        print("Build cancelled.")
        sys.exit(0)

    # Clean previous builds
    clean_build()

    # Build executable
    if build_exe():
        print("\n" + "="*60)
        print("Next steps:")
        print("="*60)
        print("1. Test the executable: dist/cs2change.exe")
        print("2. Upload to GitHub releases")
        print("3. Update download links in README files")
        print("\nNote: The exe file includes cs2en.otf and cs2sc.ttf")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
