from unicodedata import name
from dash import Input, Output, State, html, dcc, callback_context
from datetime import date
import dash
import dash_bootstrap_components as dbc

class DashboardModal():
    def __init__(self, my_id, trigger, tabs, app, data_manager):
        self.my_id = my_id
        self.trigger = trigger
        self.tabs = tabs
        self.app = app
        self.data_manager = data_manager

        # dashboard_list = [{'label': d.dashid, 'value': d.parent_tab.tab_id} for d in tabs.dashboards.values()]

        # self.content = dbc.Modal(
        #     [
        #         dbc.Alert(
        #             "Error: Please fill out all fields",
        #             id="dash-alert-auto",
        #             is_open=False,
        #             duration=4000,
        #             color="danger"
        #         ),
        #         dbc.ModalHeader(dbc.ModalTitle("Create A Dashboard")),
        #         dbc.ModalBody(html.Div(children=[
        #             dbc.Label("Type a name for your dashboard", html_for="dashboard-name"), html.Br(),
        #             dbc.Input(id="dashboard-name", placeholder="dashboard A", type="text"), html.Br(),
        #         ])),
        #         dbc.ModalFooter(
        #             dbc.Button(
        #                 "Submit", id="dashsubmit", className="ms-auto", n_clicks=0
        #             )
        #         ),
        #     ],
        #     id=self.my_id,
        #     is_open=False,
        # )

        # @app.callback([Output("dashmodal", "is_open"), 
        #                Output("dash-content-wrapper", "children"), Output("dash-alert-auto", "is_open")],
        #               [trigger, Input("dashsubmit", "n_clicks"), 
        #                Input('dashboard-name', 'value')],
        #               State("dashmodal", "is_open"),
        #               suppress_callback_exceptions=True, prevent_initial_call=True)
        # def toggle_modal(open, submit, dashboard_name, is_open):
        #     changed_id = [p['prop_id'] for p in callback_context.triggered][0]
        #     # If the widget is not opened but the open button was pressed, open the widget modal
        #     if open and not is_open:
        #         # Updates the dashboard list in case user has added new dashboards
        #         return not is_open,\
        #                [{'label': d.dashid, 'value': d.parent_tab.tab_id} for d in self.tabs.dashboards.values()],\
        #                dash.no_update, False
        #     # If submit was pressed, create a widget from the selected input
        #     elif 'submit' in changed_id:
        #         if start_date is None or end_date is None or widget_name is None:
        #             return is_open, [{'label': d.dashid, 'value': d.parent_tab.tab_id} for d in self.tabs.dashboards.values()],\
        #            dash.no_update, True
        #         tabs.dashboards[dashboard].widgets.append(
        #             self.chart_types[chart_type](self.data_manager, data_type, start_date, end_date, widget_name, goal)
        #         )
        #         return not is_open, dash.no_update, tabs.render_content(), False
        #     # Essentially a no update, case where neither submit nor open was clicked, typically from callback being called on refresh of page
        #     return is_open, [{'label': d.dashid, 'value': d.parent_tab.tab_id} for d in self.tabs.dashboards.values()],\
        #            dash.no_update, False
        self.dashcontent = html.Div(
            [
                dbc.Button(
                    "Click me", id="example-button", className="me-2", n_clicks=0
                ),
                html.Span(id="example-output", style={"verticalAlign": "middle"}),
            ]
        )


        @app.callback(
            Output("example-output", "children"), [Input("example-button", "n_clicks")],
            suppress_callback_exceptions=True
        )
        def on_button_click(n):
            if n is None:
                print("CLICKIED")
                return "Not clicked."
            else:
                print("CLICKIED")
                return f"Clicked {n} times."

    def render(self):
        return self.content
