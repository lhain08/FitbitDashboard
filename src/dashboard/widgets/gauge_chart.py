import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash import dcc, html

from .widget_interface import WidgetInterface


class GaugeChartWidget(WidgetInterface):
    def __init__(self, data_manager, data_type, start_date, end_date, name, goal):
        super().__init__(data_manager, data_type, start_date, end_date, name, goal)

    def render(self):
        # Get the data first
        data = self.data_manager.get_data(
            self.data_type, self.start_date, self.end_date
        )
        data[self.data_type]
        data["Time"]

        # Create the chart
        if self.goal == 0:
            fig = go.Figure(
                data=go.Indicator(
                    mode="gauge+number+delta",
                    value=150,
                    domain={"x": [0, 1], "y": [0, 1]},
                    delta={"reference": 50},
                    title={"text": str(self.data_type)},
                    gauge_bar_thickness=0.8,
                    gauge={
                        "axis": {"range": [None, 300]},
                        "threshold": {
                            "line": {"color": "red", "width": 4},
                            "thickness": 0.75,
                            "value": 250,
                        },
                    },
                )
            )

        if self.goal != 0:
            fig = go.Figure(
                data=go.Indicator(
                    mode="gauge+number+delta",
                    value=0,
                    domain={"x": [0, 1], "y": [0, 1]},
                    delta={"reference": 0},
                    title={"text": str(self.data_type)},
                    gauge_bar_thickness=0.8,
                    gauge={
                        "axis": {"range": [None, self.goal + 50]},
                        "threshold": {
                            "line": {"color": "red", "width": 4},
                            "thickness": 0.75,
                            "value": self.goal,
                        },
                    },
                )
            )

        return html.Div(
            style={"width": "50%", "padding": "1.5em", "display": "inline-block"},
            children=[
                dbc.Card("Widget: " + self.name, body=True),
                dcc.Graph(figure=fig),
            ],
        )
