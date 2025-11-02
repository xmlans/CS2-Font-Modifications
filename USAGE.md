# How to Run CS2 Font Modifier

## For End Users (Using the .exe)

### Method 1: Double-click (Recommended)
1. Double-click `cs2change.exe`
2. A console window will appear
3. Follow the on-screen prompts:
   - Select your language (1=English, 2=中文, 3=Español)
   - Press Enter to use default font, or enter custom font path
   - Enter your CS2 installation path
4. Wait for installation to complete
5. The window will stay open until you press Enter

**Note:** The console window is normal and required for the program to work. Do not close it while the program is running.

### Method 2: Run from Command Prompt
1. Open Command Prompt (cmd.exe)
2. Navigate to the folder containing `cs2change.exe`:
   ```bash
   cd C:\path\to\folder
   ```
3. Run the program:
   ```bash
   cs2change.exe
   ```

## For Developers (Using Python)

### Direct Python Execution
```bash
python cs2change.py
```

### With Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run
python cs2change.py
```

## Troubleshooting

### "RuntimeError: input(): lost sys.stdin"
This error occurs if the executable was built with `--windowed` mode. The program requires console mode.

**Solution:** Download the correct version or rebuild with:
```bash
python build_exe.py
```
Make sure `build_exe.py` uses `--console` not `--windowed`.

### Console window closes immediately
If the console window closes too fast to read:
1. Run from Command Prompt instead of double-clicking
2. Or add `pause` command in a batch file:
   ```batch
   @echo off
   cs2change.exe
   pause
   ```

### Program can't find fonts
The `.exe` should include fonts automatically. If you get font errors:
1. Make sure you're using the official release
2. If building yourself, ensure `cs2en.otf` and `cs2sc.ttf` exist in the build directory

### Anti-virus warning
PyInstaller executables sometimes trigger false positives. This is safe to ignore. You can:
- Add an exception in your antivirus
- Build from source on your own machine
- Check the source code on GitHub

## System Requirements

- Windows 7 or later (64-bit recommended)
- ~15 MB free disk space
- Counter-Strike 2 installed
- Administrator rights (may be needed for copying files)

## Getting the CS2 Installation Path

The path should end with `Counter-Strike Global Offensive`.

**Common locations:**
- Steam default: `C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive`
- Custom Steam library: `D:\SteamLibrary\steamapps\common\Counter-Strike Global Offensive`

**How to find it:**
1. Open Steam
2. Right-click Counter-Strike 2
3. Click Properties
4. Click "Installed Files" tab
5. Click "Browse" button
6. Copy the path from the address bar

## Language Selection

When you start the program, you'll see:
```
Select language / 选择语言 / Seleccionar idioma:
1. English
2. 中文
3. Español
Enter (1-3):
```

Enter `1` for English, `2` for Chinese, or `3` for Spanish.

## Using Custom Fonts

When prompted for font path:
- **Press Enter** to use the default built-in font
- **Enter a path** to use your own font (e.g., `C:\Windows\Fonts\arial.ttf`)

Supported formats: `.ttf` and `.otf`

## After Installation

1. Close CS2 if it's running
2. Launch CS2
3. Your new font will be active!

To restore default CS2 fonts, verify game files in Steam.
