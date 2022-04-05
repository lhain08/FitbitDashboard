""" Main module: Runs the application """
from dash import Dash, html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

from api.data_manager import DataManager
from dashboard.app_builder import AppBuilder

# Generate our app
load_figure_template(['darkly'])
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Create data manager and app builder
dm = DataManager()
builder = AppBuilder(app, dm)

app.title = "Fitbit Dashboard"
app.layout = builder.build

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8000, debug=True)
