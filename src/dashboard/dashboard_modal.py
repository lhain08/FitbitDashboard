import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback_context, html


class DashboardModal:
    def __init__(self, my_id, trigger, tabs, app, data_manager):
        self.my_id = my_id
        self.trigger = trigger
        self.tabs = tabs
        self.app = app
        self.data_manager = data_manager

        self.content = dbc.Modal(
            [
                dbc.Alert(
                    "Error: There is already a dashboard with that name",
                    id="dashboard-alert-auto",
                    is_open=False,
                    duration=4000,
                    color="danger",
                ),
                dbc.ModalHeader(dbc.ModalTitle("Create A Dashboard")),
                dbc.ModalBody(
                    html.Div(
                        children=[
                            dbc.Label(
                                "Type a name for your dashboard",
                                html_for="dashboard-name",
                            ),
                            html.Br(),
                            dbc.Input(
                                id="dashboard-name",
                                placeholder="Dashboard",
                                type="text",
                            ),
                        ]
                    )
                ),
                dbc.ModalFooter(
                    dbc.Button(
                        "Submit", id="dashboard-submit", className="ms-auto", n_clicks=0
                    )
                ),
            ],
            id=self.my_id,
            is_open=False,
        )

        @app.callback(
            [
                Output("dashmodal", "is_open"),
                Output(self.tabs.my_id, "active_tab"),
                Output(self.tabs.my_id, "children"),
                Output("dashboard-alert-auto", "is_open"),
            ],
            [
                trigger,
                Input("dashboard-submit", "n_clicks"),
                Input("dashboard-name", "value"),
            ],
            State("dashmodal", "is_open"),
            suppress_callback_exceptions=True,
            prevent_initial_call=True,
        )
        def toggle_modal(
            dash_open,
            submit,
            dashboard_name,
            is_open,
        ):
            changed_id = [p["prop_id"] for p in callback_context.triggered][0]
            # If the widget is not opened but the open button was pressed, open the widget modal
            if dash_open and not is_open:
                # Updates the dashboard list in case user has added new dashboards
                return (
                    not is_open,
                    dash.no_update,
                    dash.no_update,
                    False,
                )
            # If submit was pressed, create a widget from the selected input
            if "dashboard-submit" in changed_id:
                # Get list of dashboards
                dashboard_list = [
                    {"label": d.dashid, "value": d.parent_tab.tab_id}
                    for d in tabs.dashboards.values()
                ]
                for name in dashboard_list:
                    if dashboard_name == name["label"]:
                        return (
                            is_open,
                            dash.no_update,
                            dash.no_update,
                            True,
                        )
                print("added: ", dashboard_name)
                return (
                    not is_open,
                    self.tabs.new_tab(dashboard_name),
                    self.tabs.tabs.children,
                    False,
                )
            # Essentially a no update, case where neither submit nor open was clicked, typically from callback being called on refresh of page
            return (
                is_open,
                dash.no_update,
                dash.no_update,
                False,
            )

    def render(self):
        return self.content
