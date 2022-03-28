from dash import Input, Output, State, html, dcc
import dash_bootstrap_components as dbc

class WidgetModal():
    def __init__(self, my_id, trigger, tabs, app):
        self.my_id = my_id
        self.trigger = trigger
        self.tabs = tabs
        self.app = app

        dashboard_list = [{'label': d.dashid, 'value': d.dashid} for d in tabs.dashboards.values()]

        self.content = dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Create A Widget")),
                dbc.ModalBody(html.Div(children=[
                    html.P("Select your dashboard"),
                    dcc.Dropdown(
                        options = dashboard_list,
                        value = dashboard_list[0]['value'],
                        id="dashboard-selection",
                    ),
                ])),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="close", className="ms-auto", n_clicks=0
                    )
                ),
            ],
            id=self.my_id,
            is_open=False,
        )

        @app.callback(Output("modal", "is_open"), Output("dashboard-selection", "options"),
                      [trigger, Input("close", "n_clicks")],
                      State("modal", "is_open"),
                      suppress_callback_exceptions=True, prevent_initial_call=True)
        def toggle_modal(open, close, is_open):
            if open or close:
                return not is_open, [{'label': d.dashid, 'value': d.dashid} for d in self.tabs.dashboards.values()]
            return is_open, [{'label': d.dashid, 'value': d.dashid} for d in self.tabs.dashboards.values()]

    def render(self):
        return self.content
