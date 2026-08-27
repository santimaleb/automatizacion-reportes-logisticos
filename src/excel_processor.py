# src/excel_processor.py
import pandas as pd
import os
from src.config import DATA_INPUT_DIR
import glob

def load_all_excel_files():
    """
    Carga todos los archivos Excel de la carpeta input
    """
    print("📂 Cargando archivos Excel...")
    
    all_files = glob.glob(os.path.join(DATA_INPUT_DIR, "*.xlsx"))
    all_dfs = []
    
    for file in all_files:
        try:
            df = pd.read_excel(file)
            df['origen_archivo'] = os.path.basename(file)
            all_dfs.append(df)
            print(f"   ✅ Cargado: {os.path.basename(file)} ({len(df)} registros)")
        except Exception as e:
            print(f"   ❌ Error al cargar {file}: {e}")
    
    if all_dfs:
        combined_df = pd.concat(all_dfs, ignore_index=True)
        print(f"\n📊 Total registros consolidados: {len(combined_df)}")
        return combined_df
    else:
        print("⚠️ No se encontraron archivos Excel en la carpeta input")
        return None

def clean_data(df):
    """
    Limpia y prepara los datos
    """
    print("🧹 Limpiando datos...")
    df_clean = df.copy()
    
    if 'fecha' in df_clean.columns:
        df_clean['fecha'] = pd.to_datetime(df_clean['fecha'])
        df_clean['mes'] = df_clean['fecha'].dt.month_name()
        df_clean['año'] = df_clean['fecha'].dt.year
    
    df_clean = df_clean.drop_duplicates()
    
    for col in ['km_recorridos', 'horas_viaje', 'costo_combustible']:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].fillna(df_clean[col].mean())
    
    print(f"   ✅ Datos limpios: {len(df_clean)} registros")
    return df_clean