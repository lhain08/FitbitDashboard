from dash import html


def MockWidget():
    """Mock widget class for testing purposes"""
    def __init__(my_id):
        self.my_id = my_id

    return html.Div(html.P(my_id))