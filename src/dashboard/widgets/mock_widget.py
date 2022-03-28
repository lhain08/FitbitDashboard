from dash import html


class MockWidget():
    """Mock widget class for testing purposes"""
    def __init__(self, my_id, content):
        self.my_id = my_id
        self.content = content

    def render(self):
        return html.Div(self.content)