# CS2 Font Modifications / CS2自定义字体

Custom software to modify CS2 global in-game fonts with built-in fonts.

<div align="center">
  <img src="https://img.shields.io/badge/Platform-Windows-pink" alt="Platform Windows" />
  <img src="https://img.shields.io/badge/Game-Counter--Strike%202-pink" alt="Game Counter‑Strike 2" />
  <img src="https://img.shields.io/badge/License-MIT-pink" alt="License MIT" />
  <img src="https://img.shields.io/github/stars/xmlans/CS2-Font-Modifications?style=social&color=ff69b4" alt="GitHub Stars" />
</div>

---

If you live in Chinese mainland use quark url for download: https://pan.quark.cn/s/2ca962008d7b <br>
[English](./README.md) | [中文](./README_CN.md) | [Español](./README_ES.md)

<br>

This installer comes bundled with a default English font and a Chinese fallback font. You can also specify any custom font you want—just one click and it replaces your game UI font instantly!

## Features v2.0

- **Multi-language Support**: Interface in English, Chinese, and Spanish
- **One-Click Installation**: Quick and easy font replacement
- **Built-in Fonts**: Includes optimized default fonts
- **Custom Fonts**: Support for any .ttf/.otf font file
- **Smart Detection**: Automatic CS2 installation path detection
- **Safe Verification**: Verifies installation before completing

## Download

<div align="center">
  <h3><a href="https://github.com/xmlans/CS2-Font-Modifications/releases/download/v/cs2change.exe">Download for Windows</a></h3>
</div>

## How to Use

1. Download the `cs2change.exe` file
2. Run the program
3. Select your preferred language (English/中文/Español)
4. Press Enter to use default font, or enter path to your custom font
5. Enter CS2 installation path (must end with "Counter-Strike Global Offensive")
6. Wait for installation to complete!

## Preview

<p align="center">
  <img src="demo.png" alt="Renderings" />
</p>

## Requirements

- Windows
- Counter-Strike 2 installed
- Python 3.6+ (for source code usage)
- fontTools (for source code usage)

## Source Code Usage

If you want to run the Python script directly:

```bash
pip install fonttools
python cs2change.py
```

## Building from Source

To build the executable yourself:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the build script:
   ```bash
   python build_exe.py
   ```

For detailed build instructions, see [BUILD.md](BUILD.md)

## Optimizations in v2.0

1. **Object-Oriented Architecture**: Refactored code into clean `FontModifier` class
2. **Better Error Handling**: Robust error handling with informative messages
3. **Improved Font Compatibility**: Support for multiple font name formats (nameID 1, 4, 6)
4. **Multiple File Format Support**: Support for both .ttf and .otf files
5. **Graceful Interruption**: Proper handling of Ctrl+C and exceptions
6. **Installation Verification**: Verifies font files and configuration after installation
7. **Enhanced Cleanup**: Removes old font files (.ttf, .otf, .uifont)

## Troubleshooting

### Program can't find CS2
- Ensure CS2 is installed
- Path must end exactly with "Counter-Strike Global Offensive"
- Example: `C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive`

### Font doesn't change in game
- Restart CS2 after installation
- Verify files were copied correctly
- Try running the program as administrator

### Font parsing error
- Ensure font file is not corrupted
- Only .ttf and .otf fonts are supported
- Try a different font

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

Developed by Star Dream Studio

## Contributing

Contributions are welcome! Feel free to submit a Pull Request.

## Disclaimer

This is an unofficial font mod. Use at your own risk. Always backup your game files before modifying.
