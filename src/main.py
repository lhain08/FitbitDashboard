from dash import Dash, html

from api import connect

app = Dash(__name__) #, external_stylesheets=[dbc.themes.DARKLY])

try:
    connect.get_client()
    app.layout = html.P("Connected")
except:
    app.layout = html.P("Error")

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', debug=True)
