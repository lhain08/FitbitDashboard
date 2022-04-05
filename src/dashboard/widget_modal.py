from dash import Input, Output, State, html, dcc, callback_context
from datetime import date
import dash
import dash_bootstrap_components as dbc
from .widgets.bar_chart import BarChartWidget
from .widgets.line_chart import LineChartWidget
from .widgets.stats_card import StatsCardWidget
from .widgets.scatter_plot import ScatterPlotWidget
from .widgets.radar_chart import RadarChartWidget

class WidgetModal():
    def __init__(self, my_id, trigger, tabs, app, data_manager):
        self.my_id = my_id
        self.trigger = trigger
        self.tabs = tabs
        self.app = app
        self.data_manager = data_manager
        self.chart_types = {'Line Chart': LineChartWidget, 'Bar Chart': BarChartWidget,
                            'Stats Card': StatsCardWidget, 'Scatter Plot': ScatterPlotWidget,
                            'Radar Chart': RadarChartWidget}

        dashboard_list = [{'label': d.dashid, 'value': d.parent_tab.tab_id} for d in tabs.dashboards.values()]

        self.content = dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Create A Widget")),
                dbc.ModalBody(html.Div(children=[
                    dbc.Label("Select your dashboard", html_for="dashboard-selection"),
                    dcc.Dropdown(style={'color': 'black'},
                        options = dashboard_list,
                        value = dashboard_list[0]['value'],
                        id="dashboard-selection",
                    ), html.Br(),
                    dbc.Label("Select your chart type", html_for="chart-type"), html.Br(),
                    dcc.RadioItems(list(self.chart_types.keys()), list(self.chart_types.keys())[0],
                                   labelStyle={'display': 'block'}, id="chart-type"), html.Br(),
                    dbc.Label("Select your data type", html_for="datatype-selection"), html.Br(),
                    dcc.Dropdown(style={'color': 'black'},
                        options = ['Steps', 'Distance', 'Calories', 'Elevation', 'Floors'],
                        value = 'Steps',
                        id="datatype-selection",
                    ), html.Br(),
                    dbc.Label("Select your time period", html_for="time-period"), html.Br(),
                    dcc.DatePickerRange(
                        id="time-period",
                        min_date_allowed=date(1950, 1, 1),
                        max_date_allowed=date(2027, 4, 27),
                        initial_visible_month=date(2022, 4, 4),
                    )
                ])),
                dbc.ModalFooter(
                    dbc.Button(
                        "Submit", id="submit", className="ms-auto", n_clicks=0
                    )
                ),
            ],
            id=self.my_id,
            is_open=False,
        )

        @app.callback([Output("modal", "is_open"), Output("dashboard-selection", "options"),
                       Output("content-wrapper", "children")],
                      [trigger, Input("submit", "n_clicks"), Input("dashboard-selection", "value"),
                       Input('chart-type', 'value'), Input('datatype-selection', 'value'),
                       Input('time-period', 'start_date'), Input('time-period', 'end_date')],
                      State("modal", "is_open"),
                      suppress_callback_exceptions=True, prevent_initial_call=True)
        def toggle_modal(open, submit, dashboard, chart_type, data_type, start_date, end_date, is_open):
            changed_id = [p['prop_id'] for p in callback_context.triggered][0]
            # If the widget is not opened but the open button was pressed, open the widget modal
            if open and not is_open:
                # Updates the dashboard list in case user has added new dashboards
                return not is_open,\
                       [{'label': d.dashid, 'value': d.parent_tab.tab_id} for d in self.tabs.dashboards.values()],\
                       dash.no_update
            # If submit was pressed, create a widget from the selected input
            elif 'submit' in changed_id:
                tabs.dashboards[dashboard].widgets.append(
                    self.chart_types[chart_type](self.data_manager, data_type, start_date, end_date)
                )
                return not is_open, dash.no_update, tabs.render_content()
            # Essentially a no update, case where neither submit nor open was clicked, typically from callback being called on refresh of page
            return is_open, [{'label': d.dashid, 'value': d.parent_tab.tab_id} for d in self.tabs.dashboards.values()],\
                   dash.no_update

    def render(self):
        return self.content
