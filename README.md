# 🚛 Automatización de Reportes Logísticos

## 📋 Descripción
Este proyecto automatiza la generación de reportes logísticos a partir de múltiples archivos Excel, calculando KPIs clave en **pesos argentinos**.

## 🎯 Objetivos
- Consolidar datos desde múltiples archivos Excel
- Calcular KPIs de transporte (costos, eficiencia, rutas, clientes)
- Generar un reporte profesional en Excel con formato automático
- Proporcionar recomendaciones basadas en los datos

## 🛠️ Tecnologías
- **Python 3.13**
- **Pandas** - Procesamiento de datos
- **OpenPyXL** - Generación de reportes en Excel
- **NumPy** - Cálculos numéricos

## 📊 Resultados (en Pesos Argentinos)
| Métrica | Resultado |
|---------|-----------|
| Ruta más costosa | Ruta Norte ($55,647,720.04) |
| Costo por km | $1,916.06 |
| Cliente principal | Cliente C |
| Mayor facturación | Cliente C ($43,911,928.21) |

## 📂 Estructura
proyecto_2_automatizacion_reportes/
├── data/
│ ├── input/ # Archivos Excel de entrada
│ └── output/ # Reporte generado
├── scripts/
│ └── generar_datos_ejemplo.py
├── src/
│ ├── config.py
│ ├── excel_processor.py
│ ├── kpi_calculator.py
│ └── report_builder.py
├── main.py
└── requirements.txt


## 👤 Autor
**Santiago Malerba**
- GitHub: [santimaleb](https://github.com/santimaleb)
- LinkedIn: [www.linkedin.com/in/santiago-joaquin-malerba-777aa123a]
