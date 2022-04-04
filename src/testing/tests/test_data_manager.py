from unittest.mock import Mock
import pytest

from src.data_manager import DataManager


class TestDataManager:
    # Create a new mock client and data manager
    mock_client = Mock()
    data_manager_under_test = DataManager(client=mock_client)

    def test_get_steps_success(self):
        self.mock_client.time_series.return_value = {
            'activities-steps': [
                {'dateTime': '2022-04-01', 'value': '1000'},
                {'dateTime': '2022-04-02', 'value': '2000'},
                {'dateTime': '2022-04-03', 'value': '3000'},
            ]
        }

        assert self.data_manager_under_test.get_steps_data('2022-04-01', '2022-04-04') == {
            'Time': ['2022-04-01', '2022-04-02', '2022-04-03'],
            'Steps': [1000, 2000, 3000]
        }
        assert self.mock_client.time_series.called_with('activities/steps', base_date='2022-04-01', end_date='2022-04-04')

    def test_get_distance(self):
        self.mock_client.time_series.return_value = {
            'activities-distance': [
                {'dateTime': '2022-04-01', 'value': '1.01'},
                {'dateTime': '2022-04-02', 'value': '2.02'},
                {'dateTime': '2022-04-03', 'value': '3.03'},
            ]
        }

        assert self.data_manager_under_test.get_distance_data('2022-04-01', '2022-04-04') == {
            'Time': ['2022-04-01', '2022-04-02', '2022-04-03'],
            'Distance': [1.01, 2.02, 3.03]
        }
        assert self.mock_client.time_series.called_with('activities/distance', base_date='2022-04-01', end_date='2022-04-04')

    def test_get_calories_success(self):
        self.mock_client.time_series.return_value = {
            'activities-calories': [
                {'dateTime': '2022-04-01', 'value': '5000'},
                {'dateTime': '2022-04-02', 'value': '6000'},
                {'dateTime': '2022-04-03', 'value': '7000'},
            ]
        }

        assert self.data_manager_under_test.get_calories_data('2022-04-01', '2022-04-04') == {
            'Time': ['2022-04-01', '2022-04-02', '2022-04-03'],
            'Calories': [5000, 6000, 7000]
        }
        assert self.mock_client.time_series.called_with('activities/calories', base_date='2022-04-01', end_date='2022-04-04')

    def test_get_elevation_success(self):
        self.mock_client.time_series.return_value = {
            'activities-elevation': [
                {'dateTime': '2022-04-01', 'value': '500'},
                {'dateTime': '2022-04-02', 'value': '600'},
                {'dateTime': '2022-04-03', 'value': '700'},
            ]
        }

        assert self.data_manager_under_test.get_elevation_data('2022-04-01', '2022-04-04') == {
            'Time': ['2022-04-01', '2022-04-02', '2022-04-03'],
            'Elevation': [500.0, 600.0, 700.0]
        }
        assert self.mock_client.time_series.called_with('activities/elevation', base_date='2022-04-01', end_date='2022-04-04')

    def test_get_floors_success(self):
        self.mock_client.time_series.return_value = {
            'activities-floors': [
                {'dateTime': '2022-04-01', 'value': '5000'},
                {'dateTime': '2022-04-02', 'value': '6000'},
                {'dateTime': '2022-04-03', 'value': '7000'},
            ]
        }

        assert self.data_manager_under_test.get_floors_data('2022-04-01', '2022-04-04') == {
            'Time': ['2022-04-01', '2022-04-02', '2022-04-03'],
            'Floors': [5000, 6000, 7000]
        }
        assert self.mock_client.time_series.called_with('activities/floors', base_date='2022-04-01', end_date='2022-04-04')

    def test_get_steps_intraday_success(self):
        self.mock_client.intraday_time_series.return_value = {
            'activities-steps-intraday': {
                'dataset': [
                    {'time': '01:00:00', 'value': '100'},
                    {'time': '01:15:00', 'value': '200'},
                    {'time': '01:30:00', 'value': '300'},
                ]
            }
        }

        assert self.data_manager_under_test.get_steps_data('2022-04-01', '15min') == {
            'Time': ['01:00:00', '01:15:00', '01:30:00'],
            'Steps': [100, 200, 300]
        }
        assert self.mock_client.time_series.called_with('activities/steps', base_date='2022-04-01', detail_level='15min')

    def test_get_distance_intraday_success(self):
        self.mock_client.intraday_time_series.return_value = {
            'activities-distance-intraday': {
                'dataset': [
                    {'time': '01:00:00', 'value': '0.01'},
                    {'time': '01:15:00', 'value': '0.02'},
                    {'time': '01:30:00', 'value': '0.03'},
                ]
            }
        }

        assert self.data_manager_under_test.get_distance_data('2022-04-01', '15min') == {
            'Time': ['01:00:00', '01:15:00', '01:30:00'],
            'Distance': [0.01, 0.02, 0.03]
        }
        assert self.mock_client.time_series.called_with('activities/distance', base_date='2022-04-01', detail_level='15min')

    def test_get_calories_intraday_success(self):
        self.mock_client.intraday_time_series.return_value = {
            'activities-calories-intraday': {
                'dataset': [
                    {'time': '01:00:00', 'value': '111'},
                    {'time': '01:15:00', 'value': '222'},
                    {'time': '01:30:00', 'value': '333'},
                ]
            }
        }

        assert self.data_manager_under_test.get_calories_data('2022-04-01', '15min') == {
            'Time': ['01:00:00', '01:15:00', '01:30:00'],
            'Calories': [111, 222, 333]
        }
        assert self.mock_client.time_series.called_with('activities/calories', base_date='2022-04-01', detail_level='15min')

    def test_get_elevation_intraday_success(self):
        self.mock_client.intraday_time_series.return_value = {
            'activities-elevation-intraday': {
                'dataset': [
                    {'time': '01:00:00', 'value': '101'},
                    {'time': '01:15:00', 'value': '202'},
                    {'time': '01:30:00', 'value': '303'},
                ]
            }
        }

        assert self.data_manager_under_test.get_elevation_data('2022-04-01', '15min') == {
            'Time': ['01:00:00', '01:15:00', '01:30:00'],
            'Elevation': [101.0, 202.0, 303.0]
        }
        assert self.mock_client.time_series.called_with('activities/elevation', base_date='2022-04-01', detail_level='15min')

    def test_get_floors_intraday_success(self):
        self.mock_client.intraday_time_series.return_value = {
            'activities-floors-intraday': {
                'dataset': [
                    {'time': '01:00:00', 'value': '1'},
                    {'time': '01:15:00', 'value': '2'},
                    {'time': '01:30:00', 'value': '3'},
                ]
            }
        }

        assert self.data_manager_under_test.get_floors_data('2022-04-01', '15min') == {
            'Time': ['01:00:00', '01:15:00', '01:30:00'],
            'Floors': [1, 2, 3]
        }
        assert self.mock_client.time_series.called_with('activities/floors', base_date='2022-04-01', detail_level='15min')

