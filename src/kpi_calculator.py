# src/kpi_calculator.py
import pandas as pd
from src.config import COSTO_POR_KM, COSTO_POR_HORA

def calculate_kpis(df):
    """
    Calcula KPIs clave para el negocio de transporte
    """
    print("📊 Calculando KPIs...")
    
    kpis = {}
    
    # 1. Costo total
    kpis['costo_total_combustible'] = df['costo_combustible'].sum()
    kpis['costo_total_peajes'] = df['costo_peajes'].sum()
    kpis['costo_total_personal'] = df['costo_personal'].sum()
    kpis['costo_total'] = df[['costo_combustible', 'costo_peajes', 'costo_personal']].sum().sum()
    
    # 2. Eficiencia
    kpis['total_km'] = df['km_recorridos'].sum()
    kpis['total_horas'] = df['horas_viaje'].sum()
    kpis['costo_por_km'] = kpis['costo_total'] / kpis['total_km']
    kpis['costo_por_hora'] = kpis['costo_total'] / kpis['total_horas']
    
    # 3. Por ruta
    kpis['kpis_por_ruta'] = df.groupby('origen_archivo').agg({
        'km_recorridos': 'sum',
        'costo_combustible': 'sum',
        'costo_peajes': 'sum',
        'costo_personal': 'sum',
        'horas_viaje': 'sum'
    }).reset_index()
    kpis['kpis_por_ruta']['costo_total'] = kpis['kpis_por_ruta'][['costo_combustible', 'costo_peajes', 'costo_personal']].sum(axis=1)
    
    # 4. Top clientes
    kpis['top_clientes'] = df.groupby('cliente').agg({
        'costo_combustible': 'sum',
        'costo_peajes': 'sum',
        'costo_personal': 'sum',
        'km_recorridos': 'sum'
    }).sort_values('costo_combustible', ascending=False).head(5)
    kpis['top_clientes']['costo_total'] = kpis['top_clientes'][['costo_combustible', 'costo_peajes', 'costo_personal']].sum(axis=1)
    
    # 5. Tendencia mensual
    kpis['tendencia_mensual'] = df.groupby('mes').agg({
        'costo_combustible': 'sum',
        'costo_peajes': 'sum',
        'costo_personal': 'sum',
        'km_recorridos': 'sum'
    }).reset_index()
    kpis['tendencia_mensual']['costo_total'] = kpis['tendencia_mensual'][['costo_combustible', 'costo_peajes', 'costo_personal']].sum(axis=1)
    
    # 6. Totales por cliente
    kpis['totales_por_cliente'] = df.groupby('cliente').agg({
        'km_recorridos': 'sum',
        'costo_combustible': 'sum',
        'costo_peajes': 'sum',
        'costo_personal': 'sum',
        'carga_toneladas': 'sum'
    }).reset_index()
    kpis['totales_por_cliente']['costo_total'] = kpis['totales_por_cliente'][['costo_combustible', 'costo_peajes', 'costo_personal']].sum(axis=1)
    
    print("   ✅ KPIs calculados")
    return kpis

def get_recommendations(kpis):
    """
    Genera recomendaciones basadas en los KPIs
    """
    recommendations = []
    
    if 'kpis_por_ruta' in kpis and not kpis['kpis_por_ruta'].empty:
        ruta_mas_costosa = kpis['kpis_por_ruta'].loc[kpis['kpis_por_ruta']['costo_total'].idxmax()]
        nombre_ruta = ruta_mas_costosa['origen_archivo'].replace('.xlsx', '')
        recommendations.append(f"La ruta más costosa es '{nombre_ruta}' (${ruta_mas_costosa['costo_total']:,.2f}). Considerar optimización de rutas o renegociación de costos.")
    
    if 'costo_por_km' in kpis and kpis['costo_por_km'] > COSTO_POR_KM * 1.2:
        recommendations.append(
        f"El costo por km (${kpis['costo_por_km']:,.2f}) supera el benchmark "
        f"(${COSTO_POR_KM:,.2f} ARS). Revisar rutas, combustible o eficiencia de flota."
    )
    
    if 'top_clientes' in kpis and not kpis['top_clientes'].empty:
        top_cliente = kpis['top_clientes'].index[0]
        recommendations.append(f"Cliente principal: {top_cliente}. Ofrecer descuentos por volumen para asegurar contrato a largo plazo.")
    
    if 'totales_por_cliente' in kpis and not kpis['totales_por_cliente'].empty:
        mejor_cliente = kpis['totales_por_cliente'].loc[kpis['totales_por_cliente']['costo_total'].idxmax()]
        recommendations.append(f"Cliente con mayor facturación: {mejor_cliente['cliente']} (${mejor_cliente['costo_total']:,.2f}). Priorizar su servicio.")
    
    return recommendations