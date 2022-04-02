from dash import Input, html
from .navbar import Navbar
from .tabbing import DashboardTabs
from .widget_modal import WidgetModal


class AppBuilder():
    """ Factory for generating the full app """
    def __init__(self, app, data_manager):
        self.app = app
        self.data_manager = data_manager
        self.tabs = DashboardTabs(self.app)
        self.modal = WidgetModal("modal", Input("new-widget", "n_clicks"), self.tabs, self.app, self.data_manager)
        self.navbar = Navbar(self.app, self.tabs, self.modal)

    def build(self):
        return html.Div(id='page', children=[
            self.navbar.render(),
            self.tabs.render()
        ])