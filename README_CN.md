# CS2 字体修改工具

内置字体，可一键替换 CS2 游戏内全局字体。

<div align="center">
  <img src="https://img.shields.io/badge/Platform-Windows-pink" alt="Platform Windows" />
  <img src="https://img.shields.io/badge/Game-Counter--Strike%202-pink" alt="Game Counter‑Strike 2" />
  <img src="https://img.shields.io/badge/License-MIT-pink" alt="License MIT" />
  <img src="https://img.shields.io/github/stars/xmlans/CS2-Font-Modifications?style=social&color=ff69b4" alt="GitHub Stars" />
</div>

---

来自中国大陆可能无法使用Github下载，所以我们还提供了夸克网盘：https://pan.quark.cn/s/2ca962008d7b <br>
[English](./README.md) | [中文](./README_CN.md) | [Español](./README_ES.md)

<br>

本安装程序内置默认英文字体和中文备用字体，您也可以指定任意自定义字体——一键替换游戏 UI 字体！

## v2.0 新特性

- **多语言支持**：界面支持英语、中文和西班牙语
- **一键安装**：快速简便的字体替换
- **内置字体**：包含优化的默认字体
- **自定义字体**：支持任何 .ttf/.otf 字体文件
- **智能检测**：自动检测 CS2 安装路径
- **安全验证**：完成前验证安装

## 下载

<div align="center">
  <h3><a href="https://github.com/xmlans/CS2-Font-Modifications/releases/download/v/cs2change.exe">Windows 下载</a></h3>
</div>

## 使用方法

1. 下载 `cs2change.exe` 文件
2. 运行程序
3. 选择您偏好的语言（English/中文/Español）
4. 按回车使用默认字体，或输入自定义字体路径
5. 输入 CS2 安装路径（必须以 "Counter-Strike Global Offensive" 结尾）
6. 等待安装完成！

## 预览

<p align="center">
  <img src="demo.png" alt="渲染效果" />
</p>

## 系统要求

- Windows 操作系统
- 已安装 Counter-Strike 2
- Python 3.6+（如果运行源代码）
- fontTools（如果运行源代码）

## 源代码使用

如果您想直接运行 Python 脚本：

```bash
pip install fonttools
python cs2change.py
```

## v2.0 优化内容

1. **面向对象架构**：重构代码为清晰的 `FontModifier` 类
2. **更好的错误处理**：健壮的错误处理和信息提示
3. **改进的字体兼容性**：支持多种字体名称格式（nameID 1, 4, 6）
4. **多文件格式支持**：同时支持 .ttf 和 .otf 文件
5. **优雅中断处理**：正确处理 Ctrl+C 和异常
6. **安装验证**：安装后验证字体文件和配置
7. **增强清理功能**：删除旧字体文件（.ttf, .otf, .uifont）

## 故障排除

### 程序找不到 CS2
- 确保已安装 CS2
- 路径必须准确以 "Counter-Strike Global Offensive" 结尾
- 示例：`C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive`

### 游戏中字体没有改变
- 安装后重启 CS2
- 验证文件是否正确复制
- 尝试以管理员身份运行程序

### 字体解析错误
- 确保字体文件未损坏
- 仅支持 .ttf 和 .otf 字体
- 尝试使用其他字体

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 致谢

由 Star Dream Studio 开发

## 贡献

欢迎贡献！欢迎提交 Pull Request。

## 免责声明

这是一个非官方的字体模组。使用风险自负。修改前请务必备份游戏文件。
