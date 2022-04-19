import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.express as px
import datetime

from .widget_interface import WidgetInterface


class ScatterPlotWidget(WidgetInterface):
    def __init__(
        self, data_manager, data_type, start_date, end_date, name, goal, trends
    ):
        super().__init__(data_manager, data_type, start_date, end_date, name, goal)
        self.trends = trends

    def render(self):
        # Get the data first
        data = self.data_manager.get_data(
            self.data_type, self.start_date, self.end_date
        )
        y = data[self.data_type]
        if self.intraday:
            x = [datetime.datetime.strptime(d, "%H:%M:%S")
                 for d in data["Time"]]
        else:
            x = [datetime.datetime.strptime(d, "%Y-%m-%d")
                 for d in data["Time"]]

        # Create the chart
        if self.trends is None:
            fig = px.scatter(x=x, y=y)
        elif self.trends == "Linear":
            fig = px.scatter(
                x=x,
                y=y,
                trendline="ols",
                trendline_scope="overall",
                trendline_color_override="red",
            )
        elif self.trends == "Rolling Average":
            fig = px.scatter(
                x=x,
                y=y,
                trendline="rolling",
                trendline_options={"window": int(len(x) / 8)},
                trendline_color_override="red",
            )

        fig.update_layout(title=str(self.data_type) + " Progress")
        fig.update_xaxes(title_text="Time")
        fig.update_yaxes(title_text=str(self.data_type))

        return html.Div(
            style={"width": "50%", "padding": "1.5em",
                   "display": "inline-block"},
            children=[
                dbc.Card(children=[
                    dbc.CardHeader(self.name),
                    dbc.CardBody(dcc.Graph(figure=fig)),
                ])
            ],
        )
