import streamlit as st
import numpy as np

def mostrar_referencia_matematica(sistema, theta_max=None):
    """Muestra las ecuaciones dinámicamente según el sistema seleccionado."""
    st.subheader(f"📚 Referencia Matemática: {sistema}")
    
    with st.expander("Ver Formulario Matemático", expanded=True):
        col1, col2 = st.columns(2)
        
        if sistema == "Masa-Resorte":
            with col1:
                st.markdown("**Cinemática**")
                st.latex(r"x(t) = A \cos(\omega t + \phi)")
                st.latex(r"v(t) = -A\omega \sin(\omega t + \phi)")
            with col2:
                st.markdown("**Energías**")
                st.latex(r"E_c = \frac{1}{2} m v^2")
                st.latex(r"E_p = \frac{1}{2} k x^2")
            st.info(r"Frecuencia angular: $\omega = \sqrt{k/m}$")
            
        else: # Péndulo Simple
            with col1:
                st.markdown("**Cinemática (Arco)**")
                st.latex(r"s(t) = s_{max} \cos(\omega t + \phi)")
                st.latex(r"v(t) = -s_{max}\omega \sin(\omega t + \phi)")
            with col2:
                st.markdown("**Energías (Aprox. Lineal)**")
                st.latex(r"E_c = \frac{1}{2} m v^2")
                st.latex(r"E_p = \frac{1}{2} \left(\frac{mg}{L}\right) s^2")
            
            st.info(r"Frecuencia angular: $\omega = \sqrt{g/L}$")
            
            if theta_max is not None:
                if theta_max > 15:
                    st.warning(f"⚠️ Alerta: El ángulo seleccionado ({theta_max}°) es mayor a 15°. "
                               "La aproximación $\sin(\\theta) \\approx \\theta$ pierde validez y el error del modelo MAS aumenta.")
                else:
                    st.success(f"✅ Ángulo de {theta_max}° adecuado para el modelo de oscilador armónico.")

def mostrar_calculadora_punto(sistema, m, k_eq, A, phi, L=None, theta_max_rad=None):
    """Sección interactiva para calcular valores instantáneos y analizar el periodo."""
    st.subheader("⏱️ Calculadora de Estado y Análisis de Periodo")
    
    t_input = st.number_input("Ingresa un tiempo específico (t) [s]:", 
                              min_value=0.0, value=0.0, step=0.1, format="%.2f")
    
    omega = np.sqrt(k_eq / m)
    
    # Cálculos instantáneos lineales
    x_t = A * np.cos(omega * t_input + phi)
    v_t = -A * omega * np.sin(omega * t_input + phi)
    ec_t = 0.5 * m * v_t**2
    ep_t = 0.5 * k_eq * x_t**2
    em_t = ec_t + ep_t
    
    # Renderizado de métricas adaptado al sistema
    c1, c2, c3, c4 = st.columns(4)
    
    if sistema == "Masa-Resorte":
        c1.metric("Posición (x)", f"{x_t:.3f} m")
        c2.metric("Velocidad (v)", f"{v_t:.3f} m/s")
    else: # Péndulo Simple
        # Para el péndulo, x_t representa el arco s. Posición angular theta = s / L
        theta_t_rad = x_t / L
        theta_t_deg = np.degrees(theta_t_rad)
        
        c1.metric("Ángulo (θ)", f"{theta_t_deg:.2f}°")
        c2.metric("Vel. Lineal (v)", f"{v_t:.3f} m/s")
        
    c3.metric("E. Cinética", f"{ec_t:.3f} J")
    c4.metric("E. Potencial", f"{ep_t:.3f} J")
    
    st.write(f"**Energía Mecánica Total (Eₘ):** {em_t:.4f} J")
    