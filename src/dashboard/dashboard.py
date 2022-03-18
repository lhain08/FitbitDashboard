from dash import html, Output, Input
import dash_bootstrap_components as dbc
import dash

class Dashboard():
    def __init__(self, app, parent_tab, id):
        self.parent_tab = parent_tab
        self.id = id

        @app.callback(Output(self.id, "children"), Input("new-widget", "n_clicks"))
        def open_widget_modal(clicks):
            print("WE WILL OPEN A MODAL HERE")
            # TODO: Create the widget modal for creating new widgets
            return dash.no_update

    def navbar(self):
        return dbc.Nav([
            dbc.NavItem(dbc.NavLink("New Widget", id="new-widget", n_clicks=0))
        ])

    def render(self):
        return html.Div(id=self.id, children=[self.navbar()])