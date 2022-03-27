""" Main module: Runs the application """
from dash import Dash, html
import dash_bootstrap_components as dbc

from data_manager import DataManager
from dashboard.tabbing import DashboardTabs
from dashboard.navbar import NavBar

dm = DataManager()
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
server = app.server

tabs = DashboardTabs(app)
navbar = NavBar(app, tabs)

app.title = "Fitbit Dashboard"
app.layout = html.Div(children=[
    navbar.render(),
    tabs.render(),
])

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8000, debug=True)
