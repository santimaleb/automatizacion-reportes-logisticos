# scripts/generar_datos_ejemplo.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.config import DATA_INPUT_DIR

def generate_sample_data():
    """
    Genera 3 archivos Excel de ejemplo para simular rutas de transporte
    """
    np.random.seed(42)
    
    rutas = [
        {'nombre': 'Ruta Norte', 'ciudades': ['Buenos Aires', 'Rosario', 'Córdoba']},
        {'nombre': 'Ruta Sur', 'ciudades': ['Buenos Aires', 'Mar del Plata', 'Bahía Blanca']},
        {'nombre': 'Ruta Oeste', 'ciudades': ['Buenos Aires', 'Mendoza', 'San Juan']}
    ]
    
    for ruta in rutas:
        data = []
        fecha_inicio = datetime(2024, 1, 1)
        
        for i in range(100):  # 100 registros por ruta
            fecha = fecha_inicio + timedelta(days=np.random.randint(0, 90))
            ciudad_origen = np.random.choice(ruta['ciudades'])
            ciudad_destino = np.random.choice([c for c in ruta['ciudades'] if c != ciudad_origen])
            
            km = np.random.randint(50, 500)
            horas = km / 60 + np.random.normal(0, 0.5)
            horas = max(1, horas)
            
            costo_combustible = km * 1.2 + np.random.normal(0, 10)
            costo_peajes = np.random.randint(0, 30)
            costo_personal = horas * 20 + np.random.normal(0, 5)
            
            registro = {
                'fecha': fecha,
                'ciudad_origen': ciudad_origen,
                'ciudad_destino': ciudad_destino,
                'km_recorridos': round(km, 2),
                'horas_viaje': round(horas, 2),
                'costo_combustible': round(costo_combustible, 2),
                'costo_peajes': costo_peajes,
                'costo_personal': round(costo_personal, 2),
                'carga_toneladas': round(np.random.uniform(0.5, 5), 2),
                'cliente': np.random.choice(['Cliente A', 'Cliente B', 'Cliente C', 'Cliente D'])
            }
            data.append(registro)
        
        df = pd.DataFrame(data)
        filepath = os.path.join(DATA_INPUT_DIR, f"{ruta['nombre'].replace(' ', '_')}.xlsx")
        df.to_excel(filepath, index=False)
        print(f"✅ Datos generados: {filepath}")

if __name__ == "__main__":
    generate_sample_data()