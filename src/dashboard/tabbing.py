from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

from .dashboard import Dashboard


class DashboardTabs():
    def __init__(self, app):
        self.newTab = dbc.Tab(label='NEW TAB', tab_id='new-tab')
        self.tabs = dbc.Tabs([self.newTab], id='tabs', active_tab='new-tab')
        self.dashboards = {}
        self.tab_index = 0

        @app.callback([Output("tabs", "active_tab"), Output("tabs", "children"), Output("content", "children")],\
                      Input("tabs", "active_tab"))
        def __new_tab(at):
            '''
            Callback for switching tabs - used to recognize when user has selected "NEW TAB" tab,
            generates a new tab/dashboard, and sets the new tab as the active tab. Also renders
            dashboards when switching between tabs.
            :param at: the active tab id
            :return: (new active tab id, tab children, content of the new tab)
            '''
            if at == 'new-tab':
                # Generate a new tab and switch to this tab
                self.tab_index += 1
                tab_id = 'tab-%d' % (self.tab_index)
                tab_count = len(self.tabs.children) - 1
                tab = dbc.Tab(label='Dashboard %d' % (tab_count + 1), tab_id=tab_id)
                self.tabs.children.insert( tab_count, tab)
                self.dashboards[tab_id] = Dashboard(tab, "dashboard-%d" % (self.tab_index))

                return tab_id, self.tabs.children, self.__render_tab(tab_id)
            return at, self.tabs.children, self.__render_tab(at), self.__render_tab(tab_id)

    def __render_tab(self, tab_id):
        return self.dashboards[tab_id].render()

    def render(self):
        return html.Div([
            self.tabs,
            html.Div(id='content')])
