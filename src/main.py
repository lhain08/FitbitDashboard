""" Main module: Runs the application """
from dash import Dash, html
import dash_bootstrap_components as dbc

from data_manager import DataManager
from dashboard.app_builder import AppBuilder

dm = DataManager()
t= dm.get_steps_data("2019-07-01", "2019-07-03")
t= dm.get_steps_data("2019-07-01", "15min")

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
server = app.server

builder = AppBuilder(app)

app.title = "Fitbit Dashboard"
app.layout = builder.build

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8000, debug=True)
