import streamlit as st
import numpy as np
from fisica import calcular_dinamica_mas
from graficos import crear_graficas_cinematica, crear_graficas_energia
from formulas import mostrar_referencia_matematica, mostrar_calculadora_punto

# Configuración de página
st.set_page_config(page_title="Simulador MAS", layout="wide")

st.title("Simulador de Movimiento Armónico Simple (MAS)")
st.markdown("""
Esta aplicación permite visualizar la cinemática y la conservación de la energía en sistemas con Movimiento Armónico Simple.
Puedes elegir entre un sistema **Masa-Resorte** (energía potencial elástica) o un **Péndulo Simple** (energía potencial gravitacional bajo la aproximación de ángulos pequeños).
""")

# --- BARRA LATERAL (Inputs) ---
st.sidebar.header("Parámetros del Sistema")

sistema = st.sidebar.radio("Selecciona el sistema:", ["Masa-Resorte", "Péndulo Simple"])

m = st.sidebar.number_input("Masa (m) [kg]", min_value=0.1, value=2.0, step=0.1, format="%.2f")
phi = st.sidebar.number_input("Fase inicial (φ) [rad]", min_value=0.0, value=0.0, step=0.1, format="%.2f")


# Parámetros dependientes del sistema
if sistema == "Masa-Resorte":
    k = st.sidebar.number_input("Constante del resorte (k) [N/m]", min_value=0.1, value=18.0, step=1.0, format="%.2f")
    A = st.sidebar.number_input("Amplitud (A) [m]", min_value=0.001, value=0.2, step=0.1, format="%.2f")
    k_eq = k
    tipo_energia = "Elástica"
else:
    g = 9.81
    L = st.sidebar.number_input("Longitud de la cuerda (L) [m]", min_value=0.1, value=2.0, step=0.1, format="%.2f")
    theta_max = st.sidebar.number_input("Ángulo máximo (θ) [grados]", min_value=0.1, value=10.0, step=1.0, format="%.2f")
    
    A = L * np.radians(theta_max) 
    k_eq = m * g / L              
    tipo_energia = "Gravitacional"

t_max = st.sidebar.number_input("Tiempo de simulación [s]", min_value=1, value=10, step=1)
# --- LÓGICA CORE ---
t, x, v, Ec, Ep, Em = calcular_dinamica_mas(m, k_eq, A, phi, t_max=t_max)

st.divider()
theta_val = theta_max if sistema == "Péndulo Simple" else None
mostrar_referencia_matematica(sistema, theta_val)

# --- RENDERIZADO DE UI ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Cinemática del Sistema")
    st.info("Observa el desfase natural entre la posición y la velocidad.\nCuando el objeto pasa por el punto de equilibrio (x=0), su velocidad es máxima.")
    fig_cinematica = crear_graficas_cinematica(t, x, v)
    st.plotly_chart(fig_cinematica, width="stretch")

with col2:
    st.subheader("Análisis de Energías")
    st.info(f"La energía fluye entre cinética y potencial {tipo_energia.lower()}. Nota cómo la línea punteada negra (Energía Mecánica Total) se mantiene constante, demostrando el principio de conservación de la energía.")
    fig_energia = crear_graficas_energia(t, Ec, Ep, Em, tipo_energia)
    st.plotly_chart(fig_energia, width="stretch")

st.divider()

# Preparamos las variables adicionales si el sistema es un péndulo
L_val = L if sistema == "Péndulo Simple" else None
theta_rad_max = np.radians(theta_max) if sistema == "Péndulo Simple" else None

mostrar_calculadora_punto(sistema, m, k_eq, A, phi, L=L_val, theta_max_rad=theta_rad_max)

# --- CRÉDITOS DEL PROYECTO ---
st.sidebar.divider()
st.sidebar.subheader("Integrantes del Grupo:")
st.sidebar.markdown("""
- Espinoza Huaman, Diego Alexhander
- Flores Mucha, Jesus Daniel
- Linares Rojas, Ander Rafael
""")