import plotly.graph_objects as go
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

from .widget_interface import WidgetInterface

class BarChartWidget(WidgetInterface):
    def __init__(self, data_manager, data_type, start_date, end_date, name):
        super().__init__(data_manager, data_type, start_date, end_date, name)

    def render(self):
        # Get the data first
        data = self.data_manager.get_data(self.data_type, self.start_date, self.end_date)
        y = data[self.data_type]
        x = data['Time']

        # Create the chart
        fig = go.Figure([go.Bar(x=x, y=y)])

        # To be used in the future
        # fig.update_layout(legend_title_text = "Activity")
        # fig.update_xaxes(title_text="Time")
        # fig.update_yaxes(title_text="Data Type")

        return html.Div(children=[
            dbc.Card("Widget: " + self.name, body=True),
            dcc.Graph(figure=fig)
        ])
