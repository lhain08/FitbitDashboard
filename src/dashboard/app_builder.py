from dash import Input, html
from .navbar import Navbar
from .tabbing import DashboardTabs
from .widget_modal import WidgetModal


class AppBuilder():
    """ Factory for generating the full app """
    def __init__(self, app):
        self.app = app

    def build(self):
        tabs = DashboardTabs(self.app)
        modal = WidgetModal("modal", Input("new-widget", "n_clicks"), tabs, self.app)
        navbar = Navbar(self.app, tabs, modal)

        return html.Div(children=[
            navbar.render(),
            tabs.render()
        ])