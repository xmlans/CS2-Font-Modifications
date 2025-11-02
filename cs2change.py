#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CS2 字体更换器 v1.0 —— 内置默认字体，免注册表探测
By Star Dream Studio
"""

import os
import sys
import shutil
from fontTools.ttLib import TTFont
import xml.etree.ElementTree as ET

def get_font_name(font_path):
    font = TTFont(font_path)
    for record in font['name'].names:
        if record.nameID == 1 and record.platformID == 3:
            return record.toUnicode().strip()
    raise ValueError("无法获取字体名称")

def prompt_font_path():
    base = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
    default = os.path.join(base, 'cs2.otf')
    choice = input("请输入自定义字体文件路径（留空使用默认「星梦推荐」cs2.otf）：").strip().strip('"')
    if choice:
        return choice
    print("使用内置默认字体 cs2.otf")
    return default

def prompt_install_path():
    while True:
        path = input("请输入 CS2 安装路径（以 Counter-Strike Global Offensive 结尾）：").strip().strip('"')
        if os.path.isdir(path) and path.endswith("Counter-Strike Global Offensive"):
            print("路径已确认")
            return path
        print(" 路径好像不对哦，请再试一次")

def ensure_dirs(*paths):
    for p in paths:
        os.makedirs(p, exist_ok=True)

def clear_old(fonts_dir):
    for f in os.listdir(fonts_dir):
        if f.lower().endswith(('.ttf', '.uifont')):
            try:
                os.remove(os.path.join(fonts_dir, f))
                print(f"已删除旧文件：{f}")
            except Exception as e:
                print(f" 删除失败 {f}: {e}")

def write_fonts_conf(dir_path, primary_name, fallback_name):
    root = ET.Element("fontconfig")
    ET.SubElement(root, "dir", prefix="default").text = "../../csgo/panorama/fonts"
    ET.SubElement(root, "fontpattern").text = primary_name
    ET.SubElement(root, "fontpattern").text = fallback_name
    tree = ET.ElementTree(root)
    out = os.path.join(dir_path, "fonts.conf")
    tree.write(out, encoding="utf-8", xml_declaration=True)
    print(f"已生成 {os.path.basename(out)}（含中文备用）")

def write_global_conf(dir_path, font_name):
    root = ET.Element("fontconfig")
    m = ET.SubElement(root, "match", target="font")
    t = ET.SubElement(m, "test", name="family")
    ET.SubElement(t, "string").text = "Stratum2"
    e = ET.SubElement(m, "edit", name="family", mode="assign")
    ET.SubElement(e, "string").text = font_name
    tree = ET.ElementTree(root)
    out = os.path.join(dir_path, "42-repl-global.conf")
    tree.write(out, encoding="utf-8", xml_declaration=True)
    print(f"已生成 {os.path.basename(out)}，超级可爱～")

def verify(fonts_dir, font_name):
    """安装结果验证"""
    ffile = os.path.join(fonts_dir, f"{font_name}.ttf")
    conf   = os.path.join(fonts_dir, "fonts.conf")
    if not os.path.isfile(ffile) or os.path.getsize(ffile) == 0:
        return False, f"字体文件有问题：{ffile}"
    if not os.path.isfile(conf):
        return False, f"缺少配置文件：{conf}"
    return True, "安装验证通过"

def main():
    font_path = prompt_font_path()
    if not os.path.isfile(font_path):
        sys.exit(f"找不到字体文件：{font_path}")

    try:
        primary_name = get_font_name(font_path)
        print(f"识别到主字体名称：{primary_name}")
    except Exception as e:
        sys.exit(f"解析主字体失败：{e}")

    base = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
    fallback_path = os.path.join(base, 'cs2sc.ttf')
    if not os.path.isfile(fallback_path):
        sys.exit(f"找不到中文备用字体：{fallback_path}")
    try:
        fallback_name = get_font_name(fallback_path)
        print(f"识别到中文备用字体：{fallback_name}")
    except Exception as e:
        sys.exit(f"解析中文备用字体失败：{e}")

    install = prompt_install_path()
    csgo_fonts = os.path.join(install, "game", "csgo", "panorama", "fonts")
    core_conf  = os.path.join(install, "game", "core", "panorama", "fonts", "conf.d")
    ensure_dirs(csgo_fonts, core_conf)


    clear_old(csgo_fonts)
    dest1 = os.path.join(csgo_fonts, f"{primary_name}.ttf")
    shutil.copy2(font_path, dest1)
    print(f"已复制主字体到：{dest1}")
    dest2 = os.path.join(csgo_fonts, f"{fallback_name}.ttf")
    shutil.copy2(fallback_path, dest2)
    print(f"已复制中文备用字体到：{dest2}")

    write_fonts_conf(csgo_fonts, primary_name, fallback_name)
    write_global_conf(core_conf, primary_name)
    ok, msg = verify(csgo_fonts, primary_name)
    print(f"{'✅' if ok else '❌'} {msg}")

    input("\n按回车键退出… (｡･ω･｡)ﾉ♡")

if __name__ == "__main__":
    main()

