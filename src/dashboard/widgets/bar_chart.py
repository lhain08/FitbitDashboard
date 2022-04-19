import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
from dash import dcc, html
import datetime

from .widget_interface import WidgetInterface


class BarChartWidget(WidgetInterface):
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
            x = [datetime.datetime.strptime(d, "%H:%M:%S") for d in data["Time"]]
        else:
            x = [datetime.datetime.strptime(d, "%Y-%m-%d") for d in data["Time"]]

        # Create the chart
        fig = go.Figure([go.Bar(x=x, y=y)])

        # Bar charts do not support trendlines so we will get the trend data from a
        # helper figure and copy it over onto our original plot
        if self.trends is not None:
            if self.trends == "Linear":
                scat = px.scatter(
                    x=x,
                    y=y,
                    trendline="ols",
                    trendline_scope="overall",
                    trendline_color_override="red",
                )
            else:
                scat = px.scatter(
                    x=x,
                    y=y,
                    trendline="rolling",
                    trendline_options={"window": int(len(x) / 8)},
                    trendline_color_override="red",
                )
            x_trend = scat["data"][1]["x"]
            y_trend = scat["data"][1]["y"]
            fig.add_trace(go.Scatter(x=x_trend, y=y_trend))

        # To be used in the future
        fig.update_layout(legend_title_text="Activity")
        fig.update_xaxes(title_text="Time")
        fig.update_yaxes(title_text=self.data_type)

        return html.Div(
            style={"width": "50%", "padding": "1.5em", "display": "inline-block"},
            children=[
                dbc.Card(children=[
                    dbc.CardHeader(self.name),
                    dbc.CardBody(dcc.Graph(figure=fig)),
                ])
            ],
        )
