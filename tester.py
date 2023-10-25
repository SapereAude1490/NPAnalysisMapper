# Q: Create a plotly scatter plot of the of a sine wave where I can change the frequency and amplitude of the wave using sliders.

import plotly.graph_objects as go

import numpy as np

from scipy import signal

import dash

import dash_core_components as dcc

import dash_html_components as html

from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id="graph"),
    html.Label([
        "Frequency",
        dcc.Slider(
            id="freq-slider",
            min=1,
            max=10,
            step=0.5,
            value=1,
            marks={i: str(i) for i in range(10)},
        ),
    ]),

    html.Label([
        "Amplitude",
        dcc.Slider(
            id="amp-slider",
            min=1,
            max=10,
            step=0.5,
            value=1,
            marks={i: str(i) for i in range(10)},
        ),
    ]),
])

@app.callback(
    Output("graph", "figure"),
    [Input("freq-slider", "value"),
     Input("amp-slider", "value")])
def display_sine(freq, amp):
    x = np.linspace(0, 10, 1000)
    y = amp * np.sin(freq * x)
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode="lines"))
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)