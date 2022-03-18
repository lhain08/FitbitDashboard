from dash import html

class Dashboard():
    def __init__(self, parent_tab, id):
        self.parent_tab = parent_tab
        self.id = id

    def render(self):
        return html.Div(id=self.id, children=[html.P("This is some content")])