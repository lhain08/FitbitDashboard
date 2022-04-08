from dash import html


class Dashboard:
    def __init__(self, app, parent_tab, dashid):
        self.parent_tab = parent_tab
        self.dashid = dashid
        self.widgets = []

    def render(self):
        return html.Div(id=self.dashid, children=[w.render() for w in self.widgets])
