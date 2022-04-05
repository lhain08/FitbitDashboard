import dash
from dash import html
import dash_bootstrap_components as dbc
from datetime import datetime
from .constants import Constants

from .widget_interface import WidgetInterface


class StatsCardWidget(WidgetInterface):
    def __init(self, data_manager, data_type, start_date, end_date, name='Stats Card'):
        super().__init__(data_manager, data_type, start_date, end_date, name=name)

    def render(self):
        # Get the data first
        data = self.data_manager.get_data(self.data_type, self.start_date, self.end_date)
        values = data[self.data_type]
        dateTimes = data['Time']

        # Compute the stats
        body = None
        if self.intraday: # Intra-day statistics
            total = sum(values)
            max_index = max(range(len(values)), key=values.__getitem__)
            max_value = values[max_index]
            max_time = dateTimes[max_index]

            # Generate the card body
            body = html.Div([
                html.H3(f"Total {self.data_type}", style={'text-align': 'center'}),
                html.H4(f"{total:.3f} {Constants.UNITS[self.data_type]}".rstrip('0').rstrip('.'),
                        style={'text-align': 'center'}),
                # html.H3(f"Peak Time", style={'text-align': 'center'}),
                # html.H4(f"{avg:.3f}".rstrip('0').rstrip('.'), style={'text-align': 'center'}),
                html.H3(f"Peak Interval", style={'text-align': 'center'}),
                html.H4(f"{max_value:.3f} {Constants.UNITS[self.data_type]}".rstrip('0').rstrip('.'),
                        style={'text-align': 'center'}),
                html.H4(max_time, style={'text-align': 'center'})
            ])
        else:
            total = sum(values)
            avg = total / len(values)
            max_index = max(range(len(values)), key=values.__getitem__)
            max_value = values[max_index]
            max_date = datetime.strptime(dateTimes[max_index], "%Y-%m-%d")

            # Generate the card body
            body = html.Div([
                html.H3(f"Total {self.data_type}", style={'text-align': 'center'}),
                html.H4(f"{total:.3f} {Constants.UNITS[self.data_type]}".rstrip('0').rstrip('.'),
                        style={'text-align': 'center'}),
                html.H3(f"Average {self.data_type}", style={'text-align': 'center'}),
                html.H4(f"{avg:.3f} {Constants.UNITS[self.data_type]}".rstrip('0').rstrip('.'),
                        style={'text-align': 'center'}),
                html.H3(f"Max {self.data_type} Per Day", style={'text-align': 'center'}),
                html.H4(f"{max_value:.3f} {Constants.UNITS[self.data_type]}".rstrip('0').rstrip('.'),
                        style={'text-align': 'center'}),
                html.H4(max_date.strftime("%b %d %Y"), style={'text-align': 'center'})
            ])

        return dbc.Card([
            dbc.CardHeader(html.H4(self.name)),
            dbc.CardBody(body)
        ])
