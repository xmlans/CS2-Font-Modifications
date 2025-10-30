# Modificador de Fuentes CS2

Software personalizado para modificar las fuentes globales del juego CS2 con fuentes integradas.

<div align="center">
  <img src="https://img.shields.io/badge/Platform-Windows-pink" alt="Platform Windows" />
  <img src="https://img.shields.io/badge/Game-Counter--Strike%202-pink" alt="Game Counter‑Strike 2" />
  <img src="https://img.shields.io/badge/License-MIT-pink" alt="License MIT" />
  <img src="https://img.shields.io/github/stars/xmlans/CS2-Font-Modifications?style=social&color=ff69b4" alt="GitHub Stars" />
</div>

---

Para usuarios de China continental, use la URL de Quark para descargar: https://pan.quark.cn/s/2ca962008d7b <br>
[English](./README.md) | [中文](./README_CN.md) | [Español](./README_ES.md)

<br>

Este instalador viene con una fuente inglesa predeterminada y una fuente de respaldo china. También puede especificar cualquier fuente personalizada que desee: ¡un solo clic y reemplaza la fuente de la interfaz de usuario del juego al instante!

## Características v2.0

- **Soporte Multilingüe**: Interfaz en inglés, chino y español
- **Instalación con Un Clic**: Reemplazo rápido y sencillo de fuentes
- **Fuentes Integradas**: Incluye fuentes predeterminadas optimizadas
- **Fuentes Personalizadas**: Soporte para cualquier archivo de fuente .ttf/.otf
- **Detección Inteligente**: Detección automática de rutas de instalación de CS2
- **Verificación Segura**: Verifica la instalación antes de completar

## Descargar

<div align="center">
  <h3><a href="https://github.com/xmlans/CS2-Font-Modifications/releases/download/v/cs2change.exe">Descargar para Windows</a></h3>
</div>

## Cómo Usar

1. Descargue el archivo `cs2change.exe`
2. Ejecute el programa
3. Seleccione su idioma preferido (Inglés/中文/Español)
4. Presione Enter para usar la fuente predeterminada, o ingrese la ruta a su fuente personalizada
5. Ingrese la ruta de instalación de CS2 (debe terminar con "Counter-Strike Global Offensive")
6. ¡Espere a que se complete la instalación!

## Vista Previa

<p align="center">
  <img src="demo.png" alt="Renderizado" />
</p>

## Requisitos

- Windows
- Counter-Strike 2 instalado
- Python 3.6+ (para uso del código fuente)
- fontTools (para uso del código fuente)

## Uso del Código Fuente

Si desea ejecutar el script de Python directamente:

```bash
pip install fonttools
python cs2change.py
```

## Optimizaciones en v2.0

1. **Arquitectura Orientada a Objetos**: Código refactorizado en una clase limpia `FontModifier`
2. **Mejor Manejo de Errores**: Manejo robusto de errores con mensajes informativos
3. **Compatibilidad de Fuentes Mejorada**: Soporte para múltiples formatos de nombre de fuente (nameID 1, 4, 6)
4. **Soporte de Formatos de Archivo Múltiples**: Soporte tanto para .ttf como .otf
5. **Interrupción Elegante**: Manejo adecuado de Ctrl+C y excepciones
6. **Verificación de Instalación**: Verifica los archivos de fuentes y configuración después de la instalación
7. **Limpieza Mejorada**: Elimina archivos de fuentes antiguos (.ttf, .otf, .uifont)

## Solución de Problemas

### El programa no puede encontrar CS2
- Asegúrese de que CS2 esté instalado
- La ruta debe terminar exactamente con "Counter-Strike Global Offensive"
- Ejemplo: `C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive`

### La fuente no cambia en el juego
- Reinicie CS2 después de la instalación
- Verifique que los archivos se copiaron correctamente
- Intente ejecutar el programa como administrador

### Error de análisis de fuente
- Asegúrese de que el archivo de fuente no esté corrupto
- Solo se soportan fuentes .ttf y .otf
- Intente con otra fuente

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulte el archivo [LICENSE](LICENSE) para más detalles.

## Créditos

Desarrollado por Star Dream Studio

## Contribuciones

¡Las contribuciones son bienvenidas! No dude en enviar un Pull Request.

## Descargo de Responsabilidad

Este es un mod de fuentes no oficial. Use bajo su propio riesgo. Siempre haga una copia de seguridad de sus archivos de juego antes de modificarlos.
