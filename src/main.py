from dash import Dash, html

from data_manager import DataManager

dm = DataManager()
app = Dash(__name__) #, external_stylesheets=[dbc.themes.DARKLY])

try:
    app.layout = html.P("Connected")
except Exception as e:
    app.layout = html.P('error here')

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', debug=True)
