from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

class DashboardTabs():
    def __init__(self, app):
        self.newTab = dbc.Tab(label='NEW TAB', tab_id='new-tab')
        self.tabs = dbc.Tabs([self.newTab], id='tabs', active_tab='new-tab')
        self.tab_index = 0

        @app.callback([Output("tabs", "active_tab"), Output("tabs", "children")], Input("tabs", "active_tab"))
        def __new_tab(at):
            if at == 'new-tab':
                self.tab_index += 1
                tab_count = len(self.tabs.children) - 1
                tab = dbc.Tab(label='Dashboard %d' % (tab_count + 1), tab_id='tab-%d' % (self.tab_index),
                              children=[html.P("THIS IS TAB %d" % (self.tab_index))])
                self.tabs.children.insert( tab_count, tab)

                return 'tab-%d' % (self.tab_index), self.tabs.children
            return at, self.tabs.children

    def render(self):
        return html.Div([
            self.tabs,
            html.Div(id='content')])
