import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash import dcc, html

from .widget_interface import WidgetInterface


class ScatterPlotWidget(WidgetInterface):
    def __init__(self, data_manager, data_type, start_date, end_date, name, goal):
        super().__init__(data_manager, data_type, start_date, end_date, name, goal)

    def render(self):
        # Get the data first
        data = self.data_manager.get_data(
            self.data_type, self.start_date, self.end_date
        )
        y = data[self.data_type]
        x = data["Time"]

        # Create the chart
        fig = go.Figure(data=go.Scatter(x=x, y=y, mode="markers"))

        fig.update_layout(title=str(self.data_type) + " Progress")
        fig.update_xaxes(title_text="Time")
        fig.update_yaxes(title_text=str(self.data_type))

        return html.Div(
            style={"width": "50%", "padding": "1.5em", "display": "inline-block"},
            children=[
                dbc.Card("Widget: " + self.name, body=True),
                dcc.Graph(figure=fig),
            ],
        )
