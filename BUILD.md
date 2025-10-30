# Build Instructions for CS2 Font Modifier

This guide explains how to build the executable (.exe) file from the Python source code.

## Prerequisites

1. **Python 3.6 or higher**
   - Download from: https://www.python.org/downloads/
   - Make sure to check "Add Python to PATH" during installation

2. **Required Font Files**
   - `cs2en.otf` - English font (primary)
   - `cs2sc.ttf` - Chinese font (fallback)
   - Both files should be in the same directory as `cs2change.py`

## Quick Build (Windows)

### Option 1: Using build.bat (Easiest)

1. Open Command Prompt in the project directory
2. Run:
   ```bash
   build.bat
   ```
3. The executable will be created in the `dist/` folder

### Option 2: Using build_exe.py

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the build script:
   ```bash
   python build_exe.py
   ```

3. Follow the prompts

## Manual Build with PyInstaller

If you prefer to build manually:

1. Install dependencies:
   ```bash
   pip install pyinstaller fonttools
   ```

2. Run PyInstaller:
   ```bash
   pyinstaller --onefile --windowed --name=cs2change ^
       --add-data="cs2en.otf;." ^
       --add-data="cs2sc.ttf;." ^
       cs2change.py
   ```

   Note: On Linux/Mac, use `:` instead of `;` in --add-data

3. Find the executable in `dist/cs2change.exe`

## Build Options

### Console vs Windowed

- **Windowed mode** (default): No console window, cleaner for end users
  ```bash
  --windowed
  ```

- **Console mode**: Shows console for debugging
  ```bash
  --console
  ```

### Adding an Icon

To add a custom icon to the executable:

1. Get an `.ico` file
2. Add to PyInstaller command:
   ```bash
   --icon=path/to/icon.ico
   ```

## Troubleshooting

### "PyInstaller not found"
```bash
pip install pyinstaller
```

### "fonttools not found"
```bash
pip install fonttools
```

### Font files missing
Ensure `cs2en.otf` and `cs2sc.ttf` are in the project directory.

### Exe too large
The executable will be ~10-12 MB due to:
- Python runtime (~8 MB)
- Font files (~9.4 MB for cs2sc.ttf)
- Dependencies (~2-3 MB)

This is normal for PyInstaller builds.

### Antivirus false positive
PyInstaller executables sometimes trigger antivirus warnings. This is a false positive. You can:
- Add exception in your antivirus
- Build on the target machine
- Code sign the executable (advanced)

## Output

After successful build:
- **Executable**: `dist/cs2change.exe`
- **Size**: ~10-15 MB
- **Includes**: All required fonts and dependencies

## Testing

Before distributing:

1. Test on a clean system without Python installed
2. Verify all language options work (English/中文/Español)
3. Test with custom font files
4. Test installation path validation

## Distribution

1. Upload `dist/cs2change.exe` to GitHub Releases
2. Update download links in README files
3. Include version number in release notes

## Version Information

To update version number:

1. Edit `cs2change.py` line 4:
   ```python
   CS2 Font Modifier v2.0 - Multi-language Support with Built-in Fonts
   ```

2. Update README files with new version

## Build Artifacts

After building, you can safely delete:
- `build/` - Temporary build files
- `*.spec` - PyInstaller spec file
- `__pycache__/` - Python cache

Keep `dist/cs2change.exe` for distribution.

## Automated Builds

For GitHub Actions or CI/CD, see the build script for automation examples.

## Support

If you encounter issues during build:
1. Check Python version: `python --version`
2. Check pip version: `pip --version`
3. Update pip: `pip install --upgrade pip`
4. Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`
