import datetime
from datetime import date

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback_context, dcc, html

from .widgets.bar_chart import BarChartWidget
from .widgets.gauge_chart import GaugeChartWidget
from .widgets.line_chart import LineChartWidget
from .widgets.radar_chart import RadarChartWidget
from .widgets.scatter_plot import ScatterPlotWidget
from .widgets.stats_card import StatsCardWidget


class WidgetModal:
    def __init__(self, my_id, trigger, tabs, app, data_manager):
        self.my_id = my_id
        self.trigger = trigger
        self.tabs = tabs
        self.app = app
        self.data_manager = data_manager
        self.chart_types = {
            "Line Chart": LineChartWidget,
            "Bar Chart": BarChartWidget,
            "Stats Card": StatsCardWidget,
            "Scatter Plot": ScatterPlotWidget,
            "Radar Chart": RadarChartWidget,
            "Gauge Chart": GaugeChartWidget,
        }

        dashboard_list = [
            {"label": d.dashid, "value": d.parent_tab.tab_id}
            for d in tabs.dashboards.values()
        ]

        self.content = dbc.Modal(
            [
                dbc.Alert(
                    "Error: Please fill out all fields",
                    id="alert-auto",
                    is_open=False,
                    duration=4000,
                    color="danger",
                ),
                dbc.ModalHeader(dbc.ModalTitle("Create A Widget")),
                dbc.ModalBody(
                    html.Div(
                        children=[
                            dbc.Label(
                                "Select your dashboard", html_for="dashboard-selection"
                            ),
                            dcc.Dropdown(
                                style={"color": "black"},
                                options=dashboard_list,
                                value=dashboard_list[0]["value"],
                                id="dashboard-selection",
                            ),
                            html.Br(),
                            dbc.Label("Select your chart type", html_for="chart-type"),
                            html.Br(),
                            dcc.Dropdown(
                                style={"color": "black"},
                                options=list(self.chart_types.keys()),
                                value=list(self.chart_types.keys())[0],
                                id="chart-type",
                            ),
                            html.Br(),
                            dbc.Label(
                                "Select your data type", html_for="datatype-selection"
                            ),
                            html.Br(),
                            dcc.Dropdown(
                                style={"color": "black"},
                                options=[
                                    "Steps",
                                    "Distance",
                                    "Calories",
                                    "Elevation",
                                    "Floors",
                                ],
                                value="Steps",
                                id="datatype-selection",
                            ),
                            html.Br(),
                            dbc.Label(
                                "Select your time period", html_for="time-period"
                            ),
                            html.Br(),
                            dcc.DatePickerRange(
                                id="time-period",
                                min_date_allowed=date(1950, 1, 1),
                                max_date_allowed=date(2027, 4, 27),
                                initial_visible_month=date(2022, 4, 4),
                            ),
                            dbc.ButtonGroup(
                                [
                                    dbc.Button("Past Year", id="past-year"),
                                    dbc.Button("Year to Date", id="ytd"),
                                    dbc.Button("Past Month", id="past-month"),
                                    dbc.Button("Month to Date", id="mtd"),
                                    dbc.Button("Today", id="today"),
                                ],
                                size="sm",
                            ),
                            html.Br(),
                            html.Br(),
                            dbc.Label(
                                "Type a name for your widget", html_for="widget-name"
                            ),
                            html.Br(),
                            dbc.Input(
                                id="widget-name", placeholder="widget A", type="text"
                            ),
                            html.Br(),
                            dbc.Label("Set a goal (optional)", html_for="goal-set"),
                            html.Br(),
                            dcc.Slider(
                                0,
                                1000,
                                1,
                                id="goal-set",
                                tooltip={"placement": "bottom", "always_visible": True},
                                marks={
                                    0: {"label": "0"},
                                    250: {"label": "250"},
                                    500: {"label": "500"},
                                    750: {"label": "750"},
                                    1000: {"label": "1000"},
                                },
                                value=0,
                                updatemode="drag",
                            ),
                        ]
                    )
                ),
                dbc.ModalFooter(
                    dbc.Button("Submit", id="submit", className="ms-auto", n_clicks=0)
                ),
            ],
            id=self.my_id,
            is_open=False,
        )

        @app.callback(
            [
                Output("modal", "is_open"),
                Output("dashboard-selection", "options"),
                Output("content-wrapper", "children"),
                Output("alert-auto", "is_open"),
            ],
            [
                trigger,
                Input("submit", "n_clicks"),
                Input("dashboard-selection", "value"),
                Input("chart-type", "value"),
                Input("datatype-selection", "value"),
                Input("time-period", "start_date"),
                Input("time-period", "end_date"),
                Input("widget-name", "value"),
                Input("goal-set", "value"),
            ],
            State("modal", "is_open"),
            suppress_callback_exceptions=True,
            prevent_initial_call=True,
        )
        def toggle_modal(
            widget_open,
            submit,
            dashboard,
            chart_type,
            data_type,
            start_date,
            end_date,
            widget_name,
            goal,
            is_open,
        ):
            changed_id = [p["prop_id"] for p in callback_context.triggered][0]
            # If the widget is not opened but the open button was pressed, open the widget modal
            if widget_open and not is_open:
                # Updates the dashboard list in case user has added new dashboards
                return (
                    not is_open,
                    [
                        {"label": d.dashid, "value": d.parent_tab.tab_id}
                        for d in self.tabs.dashboards.values()
                    ],
                    dash.no_update,
                    False,
                )
            # If submit was pressed, create a widget from the selected input
            if "submit" in changed_id:
                if start_date is None or end_date is None or widget_name is None:
                    return (
                        is_open,
                        [
                            {"label": d.dashid, "value": d.parent_tab.tab_id}
                            for d in self.tabs.dashboards.values()
                        ],
                        dash.no_update,
                        True,
                    )
                tabs.dashboards[dashboard].widgets.append(
                    self.chart_types[chart_type](
                        self.data_manager,
                        data_type,
                        start_date,
                        end_date,
                        widget_name,
                        goal,
                    )
                )
                return not is_open, dash.no_update, tabs.render_content(), False
            # Essentially a no update, case where neither submit nor open was clicked, typically from callback being called on refresh of page
            return (
                is_open,
                [
                    {"label": d.dashid, "value": d.parent_tab.tab_id}
                    for d in self.tabs.dashboards.values()
                ],
                dash.no_update,
                False,
            )

        @app.callback(
            [
                Output("time-period", "start_date"),
                Output("time-period", "end_date"),
            ],
            [
                Input("past-year", "n_clicks"),
                Input("ytd", "n_clicks"),
                Input("past-month", "n_clicks"),
                Input("mtd", "n_clicks"),
                Input("today", "n_clicks"),
            ],
        )
        def date_pick(pastYear, ytd, pastMonth, mtd, today):
            changed_id = [p["prop_id"] for p in callback_context.triggered][0]
            td = datetime.date.today()
            if "past-year" in changed_id:
                return (td - datetime.timedelta(days=365)).strftime(
                    "%Y-%m-%d"
                ), td.strftime("%Y-%m-%d")
            if "ytd" in changed_id:
                return f"{td.year}-01-01", td.strftime("%Y-%m-%d")
            if "past-month" in changed_id:
                return (td - datetime.timedelta(days=30)).strftime(
                    "%Y-%m-%d"
                ), td.strftime("%Y-%m-%d")
            if "mtd" in changed_id:
                return f"{td.year}-{td.month}-01", td.strftime("%Y-%m-%d")
            if "today" in changed_id:
                return td.strftime("%Y-%m-%d"), td.strftime("%Y-%m-%d")
            return dash.no_update, dash.no_update

    def render(self):
        return self.content
