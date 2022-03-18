import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

from data_manager import DataManager
from tabbing import DashboardTabs

dm = DataManager()
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

tabs = DashboardTabs(app)

app.layout = tabs.render()

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', debug=True)
