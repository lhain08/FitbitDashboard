from dash import Output, Input
import dash_bootstrap_components as dbc
import dash

class NavBar():
    def __init__(self, app, tabs, navid='navbar'):
        self.navid = navid
        self.tabs = tabs
        self. navbar = dbc.NavbarSimple(
            id=self.navid,
            children=[
                dbc.NavItem(dbc.Button("New Widget", id="new-widget", n_clicks=0)),
                dbc.NavItem(dbc.Button("New Dashboard", id="new-dashboard", n_clicks=0)),
            ],
            brand="Fitbit Dashboard",
            brand_href="#",
            color="primary",
            dark=True,
        )

        @app.callback(Output("new-widget", "id"), Input("new-widget", "n_clicks"),
                      suppress_callback_exceptions=True, prevent_initial_call=True)
        def open_widget_modal(clicks):
            print("WE WILL OPEN A MODAL HERE")
            # TODO: Create the widget modal for creating new widgets
            raise dash.exceptions.PreventUpdate

        @app.callback([Output(self.tabs.my_id, "active_tab"), Output(self.tabs.my_id, "children")], Input("new-dashboard", "n_clicks"),
                      suppress_callback_exceptions=True, prevent_initial_call=True)
        def create_new_dashboard(clicks):
            return self.tabs.new_tab(), self.tabs.tabs.children

    def render(self):
        return self.navbar