import dash_bootstrap_components as dbc
from dash import html
from dash import Input, Output, State

FD_LOGO = "https://i.imgur.com/VS5lX0f.png"


class Navbar:
    def __init__(self, app, tabs, modal, dashmodal, navid="navbar"):
        self.navid = navid
        self.tabs = tabs

        self.navbar = dbc.Navbar(
            dbc.Container(
                [
                    html.A(
                        # Use row and col to control vertical alignment of logo / brand
                        dbc.Row(
                            [
                                # Our logo goes here
                                dbc.Col(html.Img(src=FD_LOGO, height="50px")),
                                dbc.Col(dbc.NavbarBrand(
                                    "Fitbit Dashboard", className="ms-2")),
                            ],
                            align="center",
                            className="g-0",
                        ),
                        href="#",
                        style={"textDecoration": "none"},
                    ),
                    dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                    dbc.Collapse(
                        dbc.Row(
                            [
                                dbc.Col(dbc.Button("New Widget",
                                        id="new-widget", n_clicks=0)),
                                dbc.Col(dbc.Button("New Dashboard",
                                        id="new-dashboard", n_clicks=0)),
                                modal.render(),
                                dashmodal.render(),
                            ],
                            className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
                            align="center"
                        ),
                        id="navbar-collapse",
                        is_open=False,
                        navbar=True,
                    ),
                ]
            ),
            color="primary",
            dark=True,
            id=self.navid,
        )

        # add callback for toggling the collapse on small screens
        @app.callback(
            Output("navbar-collapse", "is_open"),
            [Input("navbar-toggler", "n_clicks")],
            [State("navbar-collapse", "is_open")],
        )
        def toggle_navbar_collapse(n, is_open):
            if n:
                return not is_open
            return is_open

    def render(self):
        return self.navbar
