"""Tabbing Module for tracking all current Tabs/Dashboards"""
import dash_bootstrap_components as dbc
from dash import Input, Output, html

from .dashboard import Dashboard


class DashboardTabs:
    """
    A class for all tabs in the Dashboard App
    ...
    Attributes
    ----------
    app : Dash App
        instance of the running Dash application
    id : str
        unique string identifying this object
    tabs : List[dbc.Tabs]
        A list of all current tabs
    dashboards : Dict[Dashboard]
        A map of tab id's to Dashboards
    tab_index : int
        Incremented with every tab, used for generating unique identifiers
    content_id : str
        Identifier for the main content div

    Methods
    -------
    new_tab():
        generates a new tab and associated dashboard and switches to this tab
    render():
        renders the tabs and all child content
    """

    def __init__(self, app):
        self.app = app
        self.my_id = "tabs"
        self.tabs = dbc.Tabs([], id=self.my_id)
        self.dashboards = {}
        self.tab_index = 0
        self.content_id = "content"
        self.active_tab = None

        @app.callback(
            Output("content", "children"),
            Input("tabs", "active_tab"),
            prevent_initial_call=True,
        )
        def switch_tab(active_tab):
            self.active_tab = active_tab
            return self.render_tab(active_tab)

    def render_tab(self, tab_id=None):
        if tab_id:
            return self.dashboards[tab_id].render()
        return self.dashboards[self.active_tab].render()

    def new_tab(self, name):
        """
        Callback for switching tabs - used to recognize when user has selected "NEW TAB" tab,
        generates a new tab/dashboard, and sets the new tab as the active tab. Also renders
        dashboards when switching between tabs.
        :param at: the active tab id
        :return: (new active tab id, tab children, content of the new tab)
        """
        # Generate a new tab and switch to this tab
        self.tab_index += 1
        tab_id = f"tab-{self.tab_index}"
        tab_count = len(self.tabs.children)
        if name is None:
            tab = dbc.Tab(label=f"Dashboard {tab_count+1}", tab_id=tab_id)
            self.tabs.children.append(tab)
            self.dashboards[tab_id] = Dashboard(
                self.app, tab, f"Dashboard {self.tab_index}"
            )
        else:
            tab = dbc.Tab(label=name, tab_id=tab_id)
            self.tabs.children.append(tab)
            self.dashboards[tab_id] = Dashboard(self.app, tab, name)
        return tab_id

    def render_content(self, tab_id=None):
        """
        Renders the main content div and renders the active dashboard
        :param tab_id: for specifying the tab to render, if none defaults to active tab
        :return: the content div
        """
        if tab_id is None:
            if self.active_tab:
                return html.Div(
                    id=self.content_id,
                    children=[self.dashboards[self.active_tab].render()],
                )
            return html.Div(id=self.content_id)
        return html.Div(id=self.content_id, children=[self.dashboards[tab_id].render()])

    def render(self):
        """
        Creates the tab div and renders all child dashboards
        :return: The Tab Div
        """
        return html.Div(
            [
                self.tabs,
                html.Div(id="content-wrapper", children=[self.render_content()]),
            ]
        )
