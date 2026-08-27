# src/config.py
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_INPUT_DIR = os.path.join(BASE_DIR, 'data', 'input')
DATA_OUTPUT_DIR = os.path.join(BASE_DIR, 'data', 'output')

os.makedirs(DATA_INPUT_DIR, exist_ok=True)
os.makedirs(DATA_OUTPUT_DIR, exist_ok=True)

# ============================================
# BENCHMARKS EN PESOS ARGENTINOS
# ============================================
COSTO_POR_KM = 1400      # ARS por kilómetro (costo promedio)
COSTO_POR_HORA = 30000   # ARS por hora (costo promedio)