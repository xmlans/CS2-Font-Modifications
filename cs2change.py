#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CS2 Font Modifier v2.0 - Multi-language Support with Built-in Fonts
By Star Dream Studio
"""

import os
import sys
import shutil
import locale
from fontTools.ttLib import TTFont
import xml.etree.ElementTree as ET

# Multi-language translations
TRANSLATIONS = {
    'en': {
        'title': 'CS2 Font Modifier v2.0',
        'select_lang': 'Select language / 选择语言 / Seleccionar idioma:\n1. English\n2. 中文\n3. Español\nEnter (1-3): ',
        'prompt_font': 'Enter custom font file path (leave empty for default cs2.otf): ',
        'using_default': 'Using built-in default font cs2.otf',
        'prompt_install': 'Enter CS2 installation path (ending with "Counter-Strike Global Offensive"): ',
        'path_confirmed': 'Path confirmed',
        'path_error': 'Invalid path, please try again',
        'font_not_found': 'Font file not found: {}',
        'detected_primary': 'Detected primary font name: {}',
        'parse_error': 'Failed to parse primary font: {}',
        'fallback_not_found': 'Fallback font not found: {}',
        'detected_fallback': 'Detected fallback font: {}',
        'parse_fallback_error': 'Failed to parse fallback font: {}',
        'deleted_old': 'Deleted old file: {}',
        'delete_failed': 'Failed to delete {}: {}',
        'copied_primary': 'Copied primary font to: {}',
        'copied_fallback': 'Copied fallback font to: {}',
        'generated_fonts_conf': 'Generated {} (with fallback support)',
        'generated_global_conf': 'Generated {}',
        'verify_success': 'Installation verification passed',
        'verify_fail': 'Font file issue: {}',
        'verify_missing': 'Missing configuration file: {}',
        'exit_prompt': '\nPress Enter to exit...',
        'font_name_error': 'Unable to get font name',
        'invalid_choice': 'Invalid choice, using English as default'
    },
    'zh': {
        'title': 'CS2 字体更换器 v2.0',
        'select_lang': '选择语言 / Select language / Seleccionar idioma:\n1. English\n2. 中文\n3. Español\n请输入 (1-3): ',
        'prompt_font': '请输入自定义字体文件路径（留空使用默认「星梦推荐」cs2.otf）：',
        'using_default': '使用内置默认字体 cs2.otf',
        'prompt_install': '请输入 CS2 安装路径（以 Counter-Strike Global Offensive 结尾）：',
        'path_confirmed': '路径已确认',
        'path_error': '路径好像不对哦，请再试一次',
        'font_not_found': '找不到字体文件：{}',
        'detected_primary': '识别到主字体名称：{}',
        'parse_error': '解析主字体失败：{}',
        'fallback_not_found': '找不到备用字体：{}',
        'detected_fallback': '识别到备用字体：{}',
        'parse_fallback_error': '解析备用字体失败：{}',
        'deleted_old': '已删除旧文件：{}',
        'delete_failed': '删除失败 {}: {}',
        'copied_primary': '已复制主字体到：{}',
        'copied_fallback': '已复制备用字体到：{}',
        'generated_fonts_conf': '已生成 {}（含备用字体）',
        'generated_global_conf': '已生成 {}',
        'verify_success': '安装验证通过',
        'verify_fail': '字体文件有问题：{}',
        'verify_missing': '缺少配置文件：{}',
        'exit_prompt': '\n按回车键退出… (｡･ω･｡)ﾉ♡',
        'font_name_error': '无法获取字体名称',
        'invalid_choice': '无效选择，使用中文作为默认语言'
    },
    'es': {
        'title': 'Modificador de Fuentes CS2 v2.0',
        'select_lang': 'Seleccionar idioma / Select language / 选择语言:\n1. English\n2. 中文\n3. Español\nIngrese (1-3): ',
        'prompt_font': 'Ingrese la ruta del archivo de fuente personalizado (dejar vacío para usar cs2.otf predeterminado): ',
        'using_default': 'Usando fuente predeterminada integrada cs2.otf',
        'prompt_install': 'Ingrese la ruta de instalación de CS2 (debe terminar con "Counter-Strike Global Offensive"): ',
        'path_confirmed': 'Ruta confirmada',
        'path_error': 'Ruta inválida, por favor intente de nuevo',
        'font_not_found': 'Archivo de fuente no encontrado: {}',
        'detected_primary': 'Nombre de fuente principal detectado: {}',
        'parse_error': 'Error al analizar la fuente principal: {}',
        'fallback_not_found': 'Fuente de respaldo no encontrada: {}',
        'detected_fallback': 'Fuente de respaldo detectada: {}',
        'parse_fallback_error': 'Error al analizar la fuente de respaldo: {}',
        'deleted_old': 'Archivo antiguo eliminado: {}',
        'delete_failed': 'Error al eliminar {}: {}',
        'copied_primary': 'Fuente principal copiada a: {}',
        'copied_fallback': 'Fuente de respaldo copiada a: {}',
        'generated_fonts_conf': 'Generado {} (con soporte de respaldo)',
        'generated_global_conf': 'Generado {}',
        'verify_success': 'Verificación de instalación exitosa',
        'verify_fail': 'Problema con el archivo de fuente: {}',
        'verify_missing': 'Archivo de configuración faltante: {}',
        'exit_prompt': '\nPresione Enter para salir...',
        'font_name_error': 'No se puede obtener el nombre de la fuente',
        'invalid_choice': 'Elección inválida, usando inglés como predeterminado'
    }
}


class FontModifier:
    """CS2 Font Modifier with multi-language support"""

    def __init__(self):
        self.lang = self._detect_language()
        self.t = TRANSLATIONS[self.lang]

    def _detect_language(self):
        """Detect system language and prompt user to select"""
        try:
            choice = input(TRANSLATIONS['en']['select_lang']).strip()
            lang_map = {'1': 'en', '2': 'zh', '3': 'es'}
            selected = lang_map.get(choice, None)

            if selected:
                return selected

            # Auto-detect as fallback
            sys_lang = locale.getdefaultlocale()[0]
            if sys_lang:
                if sys_lang.startswith('zh'):
                    return 'zh'
                elif sys_lang.startswith('es'):
                    return 'es'
            return 'en'
        except Exception:
            return 'en'

    def get_font_name(self, font_path):
        """Extract font name from font file with better error handling"""
        try:
            font = TTFont(font_path)
            # Try multiple name IDs for better compatibility
            for nameID in [1, 4, 6]:
                for record in font['name'].names:
                    if record.nameID == nameID and record.platformID == 3:
                        name = record.toUnicode().strip()
                        if name:
                            return name
            raise ValueError(self.t['font_name_error'])
        except Exception as e:
            raise ValueError(f"{self.t['font_name_error']}: {str(e)}")

    def prompt_font_path(self):
        """Prompt user for font file path"""
        base = getattr(sys, '_MEIPASS', os.path.dirname(__file__))

        # Support both .otf and .ttf default fonts
        for ext in ['cs2.otf', 'cs2en.otf', 'cs2.ttf']:
            default = os.path.join(base, ext)
            if os.path.isfile(default):
                break

        choice = input(self.t['prompt_font']).strip().strip('"')
        if choice:
            return choice
        print(self.t['using_default'])
        return default

    def prompt_install_path(self):
        """Prompt user for CS2 installation path with validation"""
        while True:
            path = input(self.t['prompt_install']).strip().strip('"')
            if os.path.isdir(path) and path.endswith("Counter-Strike Global Offensive"):
                print(self.t['path_confirmed'])
                return path
            print(self.t['path_error'])

    def ensure_dirs(self, *paths):
        """Create directories if they don't exist"""
        for p in paths:
            os.makedirs(p, exist_ok=True)

    def clear_old(self, fonts_dir):
        """Remove old font files"""
        if not os.path.exists(fonts_dir):
            return

        for f in os.listdir(fonts_dir):
            if f.lower().endswith(('.ttf', '.otf', '.uifont')):
                try:
                    os.remove(os.path.join(fonts_dir, f))
                    print(self.t['deleted_old'].format(f))
                except Exception as e:
                    print(self.t['delete_failed'].format(f, e))

    def write_fonts_conf(self, dir_path, primary_name, fallback_name):
        """Generate fonts.conf with primary and fallback fonts"""
        root = ET.Element("fontconfig")
        ET.SubElement(root, "dir", prefix="default").text = "../../csgo/panorama/fonts"
        ET.SubElement(root, "fontpattern").text = primary_name
        ET.SubElement(root, "fontpattern").text = fallback_name
        tree = ET.ElementTree(root)
        out = os.path.join(dir_path, "fonts.conf")
        tree.write(out, encoding="utf-8", xml_declaration=True)
        print(self.t['generated_fonts_conf'].format(os.path.basename(out)))

    def write_global_conf(self, dir_path, font_name):
        """Generate global configuration to replace Stratum2 font"""
        root = ET.Element("fontconfig")
        m = ET.SubElement(root, "match", target="font")
        t = ET.SubElement(m, "test", name="family")
        ET.SubElement(t, "string").text = "Stratum2"
        e = ET.SubElement(m, "edit", name="family", mode="assign")
        ET.SubElement(e, "string").text = font_name
        tree = ET.ElementTree(root)
        out = os.path.join(dir_path, "42-repl-global.conf")
        tree.write(out, encoding="utf-8", xml_declaration=True)
        print(self.t['generated_global_conf'].format(os.path.basename(out)))

    def verify(self, fonts_dir, font_name):
        """Verify installation success"""
        ffile = os.path.join(fonts_dir, f"{font_name}.ttf")
        conf = os.path.join(fonts_dir, "fonts.conf")

        if not os.path.isfile(ffile) or os.path.getsize(ffile) == 0:
            return False, self.t['verify_fail'].format(ffile)
        if not os.path.isfile(conf):
            return False, self.t['verify_missing'].format(conf)
        return True, self.t['verify_success']

    def run(self):
        """Main execution flow"""
        print(f"\n{self.t['title']}\n{'='*50}\n")

        # Get font path
        font_path = self.prompt_font_path()
        if not os.path.isfile(font_path):
            sys.exit(self.t['font_not_found'].format(font_path))

        # Parse primary font
        try:
            primary_name = self.get_font_name(font_path)
            print(self.t['detected_primary'].format(primary_name))
        except Exception as e:
            sys.exit(self.t['parse_error'].format(e))

        # Parse fallback font
        base = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
        fallback_path = os.path.join(base, 'cs2sc.ttf')
        if not os.path.isfile(fallback_path):
            sys.exit(self.t['fallback_not_found'].format(fallback_path))

        try:
            fallback_name = self.get_font_name(fallback_path)
            print(self.t['detected_fallback'].format(fallback_name))
        except Exception as e:
            sys.exit(self.t['parse_fallback_error'].format(e))

        # Get installation path
        install = self.prompt_install_path()
        csgo_fonts = os.path.join(install, "game", "csgo", "panorama", "fonts")
        core_conf = os.path.join(install, "game", "core", "panorama", "fonts", "conf.d")
        self.ensure_dirs(csgo_fonts, core_conf)

        # Clear old fonts
        self.clear_old(csgo_fonts)

        # Copy fonts
        dest1 = os.path.join(csgo_fonts, f"{primary_name}.ttf")
        shutil.copy2(font_path, dest1)
        print(self.t['copied_primary'].format(dest1))

        dest2 = os.path.join(csgo_fonts, f"{fallback_name}.ttf")
        shutil.copy2(fallback_path, dest2)
        print(self.t['copied_fallback'].format(dest2))

        # Write configuration files
        self.write_fonts_conf(csgo_fonts, primary_name, fallback_name)
        self.write_global_conf(core_conf, primary_name)

        # Verify installation
        ok, msg = self.verify(csgo_fonts, primary_name)
        print(f"{'✅' if ok else '❌'} {msg}")

        input(self.t['exit_prompt'])


def main():
    """Entry point"""
    try:
        modifier = FontModifier()
        modifier.run()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        input("\nPress Enter to exit...")
        sys.exit(1)


if __name__ == "__main__":
    main()
