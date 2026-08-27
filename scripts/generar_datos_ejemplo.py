# scripts/generar_datos_ejemplo.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from src.config import DATA_INPUT_DIR
except ImportError:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_INPUT_DIR = os.path.join(BASE_DIR, 'data', 'input')
    os.makedirs(DATA_INPUT_DIR, exist_ok=True)

def generate_sample_data():
    """
    Genera 3 archivos Excel de ejemplo para simular rutas de transporte
    TODOS LOS COSTOS EN PESOS ARGENTINOS
    """
    np.random.seed(42)
    
    rutas = [
        {'nombre': 'Ruta Norte', 'ciudades': ['Buenos Aires', 'Rosario', 'Córdoba']},
        {'nombre': 'Ruta Sur', 'ciudades': ['Buenos Aires', 'Mar del Plata', 'Bahía Blanca']},
        {'nombre': 'Ruta Oeste', 'ciudades': ['Buenos Aires', 'Mendoza', 'San Juan']}
    ]
    
    print("📂 Generando archivos de ejemplo en:", DATA_INPUT_DIR)
    print("💰 Todos los costos en PESOS ARGENTINOS")
    
    for ruta in rutas:
        data = []
        fecha_inicio = datetime(2024, 1, 1)
        
        for i in range(100):
            fecha = fecha_inicio + timedelta(days=np.random.randint(0, 90))
            ciudad_origen = np.random.choice(ruta['ciudades'])
            ciudad_destino = np.random.choice([c for c in ruta['ciudades'] if c != ciudad_origen])
            
            # Datos de la ruta
            km = np.random.randint(50, 500)
            horas = km / 60 + np.random.normal(0, 0.5)
            horas = max(1, horas)
            
            # ============================================
            # COSTOS EN PESOS ARGENTINOS (valores realistas)
            # ============================================
            # Combustible: ~$1.200 - $1.500 por km (camión)
            costo_combustible = km * np.random.uniform(1200, 1500) + np.random.normal(0, 5000)
            
            # Peajes: ~$5.000 - $30.000 por viaje
            costo_peajes = np.random.randint(5000, 30000)
            
            # Personal: ~$25.000 - $35.000 por hora (chofer + ayudante)
            costo_personal = horas * np.random.uniform(25000, 35000) + np.random.normal(0, 5000)
            
            registro = {
                'fecha': fecha.strftime('%Y-%m-%d'),
                'ciudad_origen': ciudad_origen,
                'ciudad_destino': ciudad_destino,
                'km_recorridos': round(km, 2),
                'horas_viaje': round(horas, 2),
                'costo_combustible': round(costo_combustible, 2),
                'costo_peajes': round(costo_peajes, 2),
                'costo_personal': round(costo_personal, 2),
                'carga_toneladas': round(np.random.uniform(0.5, 5), 2),
                'cliente': np.random.choice(['Cliente A', 'Cliente B', 'Cliente C', 'Cliente D'])
            }
            data.append(registro)
        
        df = pd.DataFrame(data)
        os.makedirs(DATA_INPUT_DIR, exist_ok=True)
        filepath = os.path.join(DATA_INPUT_DIR, f"{ruta['nombre'].replace(' ', '_')}.xlsx")
        df.to_excel(filepath, index=False)
        print(f"   ✅ Datos generados: {filepath}")

    print("\n✅ Todos los archivos generados correctamente!")
    print(f"📂 Carpeta: {DATA_INPUT_DIR}")

if __name__ == "__main__":
    generate_sample_data()