import dash_bootstrap_components as dbc


class Navbar:
    def __init__(self, tabs, modal, dashmodal, navid="navbar"):
        self.navid = navid
        self.tabs = tabs
        self.navbar = dbc.NavbarSimple(
            id=self.navid,
            children=[
                dbc.NavItem(dbc.Button("New Widget", id="new-widget", n_clicks=0)),
                dbc.NavItem(
                    dbc.Button("New Dashboard", id="new-dashboard", n_clicks=0)
                ),
                modal.render(),
                dashmodal.render(),
            ],
            brand="Fitbit Dashboard",
            brand_href="#",
            color="primary",
            dark=True,
        )

    def render(self):
        return self.navbar
