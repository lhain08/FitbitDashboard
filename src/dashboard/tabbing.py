from dash import html, Input, Output
import dash_bootstrap_components as dbc

from .dashboard import Dashboard


class DashboardTabs():
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
        self.id = "tabs"
        self.tabs = dbc.Tabs([], id=self.id)
        self.dashboards = {}
        self.tab_index = 0
        self.content_id = "content"

        # Create first tab
        self.new_tab()

        @app.callback(Output("content", "children"), Input("tabs", "active_tab"), prevent_initial_call=True)
        def switch_tab(active_tab):
            return self.__render_tab(active_tab)

    def __render_tab(self, tab_id):
        return self.dashboards[tab_id].render()

    def new_tab(self):
        '''
        Callback for switching tabs - used to recognize when user has selected "NEW TAB" tab,
        generates a new tab/dashboard, and sets the new tab as the active tab. Also renders
        dashboards when switching between tabs.
        :param at: the active tab id
        :return: (new active tab id, tab children, content of the new tab)
        '''
        # Generate a new tab and switch to this tab
        self.tab_index += 1
        tab_id = f"tab-{self.tab_index}"
        tab_count = len(self.tabs.children)
        tab = dbc.Tab(label=f"Dashboard {tab_count}", tab_id=tab_id)
        self.tabs.children.append(tab)
        self.dashboards[tab_id] = Dashboard(self.app, tab, f"dashboard-{self.tab_index}")
        return tab_id

    def render(self):
        '''
        Creates the tab div and renders all child dashboards
        :return: The Tab Div
        '''
        return html.Div([
            self.tabs,
            html.Div(id=self.content_id)])
