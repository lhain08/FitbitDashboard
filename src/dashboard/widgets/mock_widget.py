from dash import html


class MockWidget():
    """Mock widget class for testing purposes"""
    def __init__(self, my_id):
        self.my_id = my_id

    def render(self):
        return html.Div(html.P("I'm Widget " + self.my_id))