from dash import html, Output, Input
import dash_bootstrap_components as dbc
import dash

class Dashboard():
    def __init__(self, app, parent_tab, id):
        self.parent_tab = parent_tab
        self.id = id

    def render(self):
        return html.Div(id=self.id, children=[])