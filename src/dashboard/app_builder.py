from dash import Input, html

from .navbar import Navbar
from .tabbing import DashboardTabs
from .widget_modal import WidgetModal
from .dashboard_modal import DashboardModal


class AppBuilder:
    """Factory for generating the full app"""

    def __init__(self, app, data_manager):
        self.app = app
        self.data_manager = data_manager
        self.tabs = DashboardTabs(self.app)
        self.dashmodal = DashboardModal(
            "dashmodal",
            Input("new-dashboard", "n_clicks"),
            self.tabs,
            self.app,
            self.data_manager,
        )
        self.modal = WidgetModal(
            "modal",
            Input("new-widget", "n_clicks"),
            self.tabs,
            self.app,
            self.data_manager,
        )
        self.navbar = Navbar(self.app, self.tabs, self.modal, self.dashmodal)

    def build(self):
        return html.Div(id="page", children=[self.navbar.render(), self.tabs.render()])
