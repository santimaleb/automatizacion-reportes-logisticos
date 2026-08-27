# main.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.excel_processor import load_all_excel_files, clean_data
from src.kpi_calculator import calculate_kpis, get_recommendations
from src.report_builder import build_excel_report

def main():
    print("\n" + "="*60)
    print(" 🚛 AUTOMATIZACIÓN DE REPORTES LOGÍSTICOS")
    print("="*60 + "\n")
    
    print("📌 EJECUTANDO PROCESO DE REPORTE...")
    
    # 1. Cargar datos
    df = load_all_excel_files()
    if df is None:
        print("❌ No hay datos para procesar. Ejecutá primero 'scripts/generar_datos_ejemplo.py'")
        return
    
    # 2. Limpiar datos
    df_clean = clean_data(df)
    
    # 3. Calcular KPIs
    kpis = calculate_kpis(df_clean)
    
    # 4. Generar recomendaciones
    print("\n💡 GENERANDO RECOMENDACIONES:")
    recommendations = get_recommendations(kpis)
    for i, rec in enumerate(recommendations, 1):
        print(f"   {i}. {rec}")
    
    # 5. Construir reporte
    build_excel_report(df_clean, kpis, recommendations)
    
    print("\n" + "="*60)
    print("✅ PROYECTO COMPLETADO CON ÉXITO!")
    print(f"📂 Revisá la carpeta 'data/output' para ver el reporte generado.")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()