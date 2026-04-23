import numpy as np

def calcular_dinamica_mas(m, k_eq, A, phi, t_max=10, num_puntos=500):
    """
    Calcula la cinemática y las energías de un Movimiento Armónico Simple.
    """
    t = np.linspace(0, t_max, num_puntos)
    omega = np.sqrt(k_eq / m)
    
    # Cinemática
    x = A * np.cos(omega * t + phi)
    v = -A * omega * np.sin(omega * t + phi)
    
    # Energías
    Ec = 0.5 * m * v**2
    Ep = 0.5 * k_eq * x**2
    Em = Ec + Ep  # Energía mecánica total (debe ser constante)
    
    return t, x, v, Ec, Ep, Em