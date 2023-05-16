import plotly.graph_objs as go
from .models import MeasurementData


def create_graph(data: MeasurementData):
    # Daten aus MeasurementData extrahieren
    x_data = [entry[0] for entry in data.data]
    y_data = [entry[1] for entry in data.data]

    # Plotly Graph-Objekt erstellen
    graph = go.Figure(
        data=go.Scatter(
            x=x_data,
            y=y_data,
            mode="lines",
            marker=dict(color="blue"),
            name="Line Plot",
        ),
        layout=go.Layout(
            title="Mein Plotly Graph",
            xaxis=dict(title="X-Achse"),
            yaxis=dict(title="Y-Achse"),
            showlegend=True,
        ),
    )

    return graph.to_html()
