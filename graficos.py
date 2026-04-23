import plotly.graph_objects as go
from plotly.subplots import make_subplots

def crear_graficas_cinematica(t, x, v):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                        subplot_titles=("Posición vs Tiempo", "Velocidad vs Tiempo"))
    
    fig.add_trace(go.Scatter(x=t, y=x, mode='lines', name='Posición x(t)', line=dict(color='blue')), row=1, col=1)
    fig.add_trace(go.Scatter(x=t, y=v, mode='lines', name='Velocidad v(t)', line=dict(color='red')), row=2, col=1)
    
    fig.update_layout(height=500, margin=dict(l=20, r=20, t=40, b=20), hovermode="x unified")
    fig.update_yaxes(title_text="x (m)", row=1, col=1)
    fig.update_yaxes(title_text="v (m/s)", row=2, col=1)
    fig.update_xaxes(title_text="Tiempo (s)", row=2, col=1)
    
    return fig

def crear_graficas_energia(t, Ec, Ep, Em, tipo_energia="Elástica"):
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x=t, y=Ec, mode='lines', name='E. Cinética (Ec)', line=dict(color='green')))
    fig.add_trace(go.Scatter(x=t, y=Ep, mode='lines', name=f'E. Potencial {tipo_energia} (Ep)', line=dict(color='orange')))
    fig.add_trace(go.Scatter(x=t, y=Em, mode='lines', name='E. Mecánica (Em)', line=dict(color='black', dash='dash')))
    
    fig.update_layout(title="Conservación de la Energía",
                      xaxis_title="Tiempo (s)",
                      yaxis_title="Energía (Joules)",
                      hovermode="x unified",
                      height=400, margin=dict(l=20, r=20, t=40, b=20))
    
    return fig