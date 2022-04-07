from unittest.mock import Mock
import pytest
from dash import html
import dash_bootstrap_components as dbc

from src.dashboard.widgets.stats_card import StatsCardWidget


class TestStatsCard:
    # Create a new mock client and data manager
    mock_data_manager = Mock()

    def test_stats_card_date_range(self):
        stats_card_under_test = StatsCardWidget(self.mock_data_manager, 'Steps', '2022-04-01', '2022-04-04', 'Test Stats Card', 0)

        self.mock_data_manager.get_data.return_value = {
            'Time': ['2022-04-01', '2022-04-02', '2022-04-03'],
            'Steps': [1000, 2000, 3000]
        }

        widget_output = stats_card_under_test.render()

        # Check database call is correct
        assert self.mock_data_manager.get_data.called_with('Steps', '2022-04-01', '2022-04-04')

        # Verify the output content
        assert type(widget_output) == html.Div
        assert len(widget_output.children) == 1
        header = widget_output.children[0].children[0]
        assert type(header) == dbc.CardHeader
        assert type(header.children) == html.H4
        assert header.children.children == 'Test Stats Card'
        body = widget_output.children[0].children[1].children.children
        body_data = {x.id:x.children for x in body if hasattr(x, 'id')}
        assert body_data['total'].split() == ['6000', 'Steps']
        assert body_data['average'].split() == ['2000', 'Steps']
        assert body_data['max-value'].split() == ['3000', 'Steps']
        assert body_data['max-date'] == 'Apr 03 2022'

    def test_stats_card_intraday(self):
        stats_card_under_test = StatsCardWidget(self.mock_data_manager, 'Distance', '2022-04-04', '2022-04-04', 'Test Stats Card', 0)

        self.mock_data_manager.get_data.return_value = {
            'Time': ['05:00:00', '05:15:00', '05:30:00', '05:45:00'],
            'Distance': [0.5, 0.1, 0.4, 0.0]
        }

        widget_output = stats_card_under_test.render()

        # Check database call is correct
        assert self.mock_data_manager.get_data.called_with('Distance', '2022-04-04', '15min')

        # Verify the output content
        assert type(widget_output) == html.Div
        assert len(widget_output.children) == 1
        header = widget_output.children[0].children[0]
        assert type(header) == dbc.CardHeader
        assert type(header.children) == html.H4
        assert header.children.children == 'Test Stats Card'
        body = widget_output.children[0].children[1].children.children
        body_data = {x.id:x.children for x in body if hasattr(x, 'id')}
        assert body_data['total'].split() == ['1', 'Miles']
        assert body_data['average'].split() == ['0.333', 'Miles']
        assert body_data['max-value'].split() == ['0.5', 'Miles']
        assert body_data['max-time'] == '05:00:00'
