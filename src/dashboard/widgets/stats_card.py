from datetime import datetime

import dash_bootstrap_components as dbc
from dash import html

from .constants import Constants
from .widget_interface import WidgetInterface


class StatsCardWidget(WidgetInterface):
    def __init__(
        self, data_manager, data_type, start_date, end_date, name="Stats Card", goal=0
    ):
        super().__init__(
            data_manager, data_type, start_date, end_date, name=name, goal=goal
        )

    def render(self):
        # Get the data first
        data = self.data_manager.get_data(
            self.data_type, self.start_date, self.end_date
        )
        values = data[self.data_type]
        dateTimes = data["Time"]

        # Compute the stats
        body = None
        if self.intraday:  # Intra-day statistics
            total = sum(values)
            max_index = max(range(len(values)), key=values.__getitem__)
            max_value = values[max_index]
            max_time = dateTimes[max_index]
            active_intervals = [v for v in values if v != 0]
            avg_interval = sum(active_intervals) / len(active_intervals)

            # Generate the card body
            body = html.Div(
                [
                    html.H3(f"Total {self.data_type}", style={"text-align": "center"}),
                    html.H4(
                        f"{total:.3f}".rstrip("0").rstrip(".")
                        + f" {Constants.UNITS[self.data_type]}",
                        style={"text-align": "center"},
                        id="total",
                    ),
                    html.H3(
                        f"Average Active 15 Minute Interval",
                        style={"text-align": "center"},
                    ),
                    html.H4(
                        f"{avg_interval:.3f}".rstrip("0").rstrip(".")
                        + f" {Constants.UNITS[self.data_type]}",
                        style={"text-align": "center"},
                        id="average",
                    ),
                    html.H3(f"Peak 15 Minute Interval", style={"text-align": "center"}),
                    html.H4(
                        f"{max_value:.3f}".rstrip("0").rstrip(".")
                        + f" {Constants.UNITS[self.data_type]}",
                        style={"text-align": "center"},
                        id="max-value",
                    ),
                    html.H4(max_time, style={"text-align": "center"}, id="max-time"),
                ]
            )
        else:
            total = sum(float(x) for x in values)
            avg = total / len(values)
            max_index = max(range(len(values)), key=values.__getitem__)
            max_value = float(values[max_index])
            max_date = datetime.strptime(dateTimes[max_index], "%Y-%m-%d")

            # Generate the card body
            body = html.Div(
                [
                    html.H3(f"Total {self.data_type}", style={"text-align": "center"}),
                    html.H4(
                        f"{total:.3f}".rstrip("0").rstrip(".")
                        + f" {Constants.UNITS[self.data_type]}",
                        style={"text-align": "center"},
                        id="total",
                    ),
                    html.H3(
                        f"Average {self.data_type}", style={"text-align": "center"}
                    ),
                    html.H4(
                        f"{avg:.3f}".rstrip("0").rstrip(".")
                        + f" {Constants.UNITS[self.data_type]}",
                        style={"text-align": "center"},
                        id="average",
                    ),
                    html.H3(
                        f"Max {self.data_type} Per Day", style={"text-align": "center"}
                    ),
                    html.H4(
                        f"{max_value:.3f}".rstrip("0").rstrip(".")
                        + f" {Constants.UNITS[self.data_type]}",
                        style={"text-align": "center"},
                        id="max-value",
                    ),
                    html.H4(
                        max_date.strftime("%b %d %Y"),
                        style={"text-align": "center"},
                        id="max-date",
                    ),
                ]
            )

        stats_card = dbc.Card(
            children=[dbc.CardHeader(html.H4(self.name)), dbc.CardBody(body)]
        )

        return html.Div(
            style={
                "width": "50%",
                "padding": "1.5em",
                "float": "left",
                "display": "inline-block",
            },
            children=[stats_card],
        )
