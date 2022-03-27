from dash import html, Output, Input
import dash_bootstrap_components as dbc
import dash

class Dashboard():
    def __init__(self, app, parent_tab, dashid):
        self.parent_tab = parent_tab
        self.dashid = dashid

    def render(self):
        return html.Div(id=self.dashid, children=[])