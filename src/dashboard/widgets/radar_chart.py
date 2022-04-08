from datetime import datetime

import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash import dcc, html

from .widget_interface import WidgetInterface


class RadarChartWidget(WidgetInterface):
    def __init__(self, data_manager, data_type, start_date, end_date, name, goal):
        super().__init__(data_manager, data_type, start_date, end_date, name, goal)

    def render(self):
        # Get the data first
        data = self.data_manager.get_data(
            self.data_type, self.start_date, self.end_date
        )
        # Get averages of data by day of week
        days = {
            "Sunday": [0, 0],
            "Monday": [0, 0],
            "Tuesday": [0, 0],
            "Wednesday": [0, 0],
            "Thursday": [0, 0],
            "Friday": [0, 0],
            "Saturday": [0, 0],
        }
        for i in range(len(data[self.data_type])):
            d = datetime.strptime(data["Time"][i], "%Y-%m-%d").strftime("%A")
            days[d][0] += data[self.data_type][i]
            days[d][1] += 1

        r = []
        x = []
        for k, v in days.items():
            r.append(v[0] / v[1])
            x.append(k)

        # Create the chart
        fig = go.Figure([go.Scatterpolar(r=r, theta=x, fill="toself")])

        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True),
            ),
            showlegend=False,
        )

        fig.update_layout(title="Goal Progress")

        return html.Div(
            style={"width": "50%", "padding": "1.5em", "display": "inline-block"},
            children=[
                dbc.Card("Widget: " + self.name, body=True),
                dcc.Graph(figure=fig),
            ],
        )
