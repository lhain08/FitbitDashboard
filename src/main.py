import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

from data_manager import DataManager
<<<<<<< HEAD
from dashboard.tabbing import DashboardTabs
from dashboard.navbar import NavBar

dm = DataManager()
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

tabs = DashboardTabs(app)
navbar = NavBar(app, tabs)

app.title = "Fitbit Dashboard"
app.layout = html.Div(children=[
    navbar.render(),
    tabs.render(),
])
=======

dm = DataManager()
app = Dash(__name__) #, external_stylesheets=[dbc.themes.DARKLY])

try:
    app.layout = html.P("Connected")
except Exception as e:
    app.layout = html.P('error here')
>>>>>>> draft-shell-of-the-data-manager

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', debug=True)
