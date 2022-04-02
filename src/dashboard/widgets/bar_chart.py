import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html

from .widget_interface import WidgetInterface


class BarChartWidget(WidgetInterface):
    def __init(self, data_manager, data_type, time_period):
        super().__init__(data_manager, data_type, time_period)

    def render(self):
        # Get the data first
        data = self.data_manager.get_data(self.data_type, self.time_period)
        y = data[self.data_type]
        x = data['Time']

        # Create the chart
        fig = go.Figure([go.Bar(x=x, y=y)])

        return html.Div([
            dcc.Graph(figure=fig)
        ])
