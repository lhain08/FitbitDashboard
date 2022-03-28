from dash import Input, Output, State, html, dcc, callback_context
import dash
import dash_bootstrap_components as dbc
from .widgets.mock_widget import MockWidget

class WidgetModal():
    def __init__(self, my_id, trigger, tabs, app):
        self.my_id = my_id
        self.trigger = trigger
        self.tabs = tabs
        self.app = app

        dashboard_list = [{'label': d.dashid, 'value': d.parent_tab.tab_id} for d in tabs.dashboards.values()]

        self.content = dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Create A Widget")),
                dbc.ModalBody(html.Div(children=[
                    dbc.Label("Select your dashboard", html_for="dashboard-selection"),
                    dcc.Dropdown(
                        options = dashboard_list,
                        value = dashboard_list[0]['value'],
                        id="dashboard-selection",
                    ),
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

        @app.callback([Output("modal", "is_open"), Output("dashboard-selection", "options")],
                      [trigger, Input("submit", "n_clicks"), Input("dashboard-selection", "value")],
                      State("modal", "is_open"),
                      suppress_callback_exceptions=True, prevent_initial_call=True)
        def toggle_modal(open, submit, dashboard, is_open):
            changed_id = [p['prop_id'] for p in callback_context.triggered][0]
            if open and not is_open:
                return not is_open,\
                       [{'label': d.dashid, 'value': d.parent_tab.tab_id} for d in self.tabs.dashboards.values()]
            elif 'submit' in changed_id:
                tabs.dashboards[dashboard].widgets.append(
                    MockWidget("widget on " + tabs.dashboards[dashboard].parent_tab.label)
                )
                return not is_open, dash.no_update
            return is_open, [{'label': d.dashid, 'value': d.parent_tab.tab_id} for d in self.tabs.dashboards.values()]

    def render(self):
        return self.content
