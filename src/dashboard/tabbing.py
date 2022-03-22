from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

from .dashboard import Dashboard


class DashboardTabs():
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
        def switch_tab(at):
            return self.__render_tab(at)

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
        tab_id = 'tab-%d' % (self.tab_index)
        tab_count = len(self.tabs.children)
        tab = dbc.Tab(label='Dashboard %d' % (tab_count), tab_id=tab_id)
        self.tabs.children.append(tab)
        self.dashboards[tab_id] = Dashboard(self.app, tab, "dashboard-%d" % (self.tab_index))
        return tab_id

    def render(self):
        return html.Div([
            self.tabs,
            html.Div(id=self.content_id)])
