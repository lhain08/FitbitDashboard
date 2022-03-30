"""Data Manager Module: Responsible for app's interactions with database/api"""
from api import connect
import re

class DataManager():
    '''
    DataManager Class
    Responsible for retrieving data from the Fitbit Client
    '''
    def __init__(self):
        self.client = connect.get_client()

    def __get_time_series(self, data_type, start_date, end_date=None, period='15min'):
        '''
        __get_time_series - used for getting time series for all activity resources
        :param data_type: required, specifies the desired activity resource
        :param start_date: required, specifies start date for date range or date for
                           intraday requests
        :param end_date: optional, when specified gets a range of data from start date
                         to end date
        :param period: time increments for intraday data, defaults to 15min. Can also
                       be 1sec or 1min.
        :return: the time series data
        '''
        if start_date is None:
            raise Exception("No start date given")

        if end_date is not None:
            data = self.client.time_series('activities/' + data_type,
                                           base_date=start_date, end_date=end_date)
            return data['activites-' + data_type]

        data = self.client.intraday_time_series('activities/' + data_type,
                                                base_date=start_date,
                                                detail_level=period)
        return data['activities-' + data_type + '-intraday']

    def get_steps_data(self, start_date, descriptor):
        '''
        get_steps_data
        :param start_date: required, specifies start date for date range
                           or date for intraday requests
        :param descriptor: can be either end_date or period depending on users input
                            end_date for daily values period for specific values throughout day
        :end_date: optional, when specified gets a range of data from
                         start date to end date
        :period: time increments for intraday data, defaults to 15min.
                       Can also be 1sec or 1min.
        
        :return: the time series data
        '''
        # Check if descriptor is date format
        r = re.compile('\d{4}-\d{2}-\d{2}')
        if(r.match(descriptor)):
            fit_statsHR = self.client.time_series('activities/steps', base_date=start_date, end_date=descriptor)

            time_list = []
            val_list = []
            for i in fit_statsHR['activities-steps']:
                val_list.append(i['value'])
                time_list.append(i['dateTime'])
            heartdf = ({'Steps':val_list,'Time':time_list})
        else:
            fit_statsHR = self.client.intraday_time_series('activities/steps', base_date=start_date, detail_level=descriptor)

            time_list = []
            val_list = []
            for i in fit_statsHR['activities-steps-intraday']['dataset']:
                val_list.append(i['value'])
                time_list.append(i['time'])
            heartdf = ({'Steps':val_list,'Time':time_list})

        return heartdf

    def get_distance_data(self, start_date, descriptor):
        '''
        get_distance_data
        :param start_date: required, specifies start date for date range or
                           date for intraday requests
        :param descriptor: can be either end_date or period depending on users input
                            end_date for daily values period for specific values throughout day
        :end_date: optional, when specified gets a range of data from
                         start date to end date
        :period: time increments for intraday data, defaults to 15min.
                       Can also be 1sec or 1min.
        :return: the time series data
        '''
        # Check if descriptor is date format
        r = re.compile('\d{4}-\d{2}-\d{2}')
        if(r.match(descriptor)):
            fit_statsHR = self.client.time_series('activities/distance', base_date=start_date, end_date=descriptor)

            time_list = []
            val_list = []
            for i in fit_statsHR['activities-distance']:
                val_list.append(i['value'])
                time_list.append(i['dateTime'])
            heartdf = ({'Distance':val_list,'Time':time_list})
            print(heartdf)
        else:
            fit_statsHR = self.client.intraday_time_series('activities/distance', base_date=start_date, detail_level=descriptor)

            time_list = []
            val_list = []
            for i in fit_statsHR['activities-distance-intraday']['dataset']:
                val_list.append(i['value'])
                time_list.append(i['time'])
            heartdf = ({'Distance':val_list,'Time':time_list})
            print(heartdf)

        return heartdf

    def get_calories_data(self, start_date, descriptor):
        '''
        get_calories_data
        :param start_date: required, specifies start date for date range or date
                           for intraday requests
        :param descriptor: can be either end_date or period depending on users input
                            end_date for daily values period for specific values throughout day
        :end_date: optional, when specified gets a range of data from start
                         date to end date
        :period: time increments for intraday data, defaults to 15min.
                       Can also be 1sec or 1min.
        :return: the time series data
        '''
        # Check if descriptor is date format
        r = re.compile('\d{4}-\d{2}-\d{2}')
        if(r.match(descriptor)):
            fit_statsHR = self.client.time_series('activities/calories', base_date=start_date, end_date=descriptor)

            time_list = []
            val_list = []
            for i in fit_statsHR['activities-calories']:
                val_list.append(i['value'])
                time_list.append(i['dateTime'])
            heartdf = ({'Calories':val_list,'Time':time_list})
            print(heartdf)
        else:
            fit_statsHR = self.client.intraday_time_series('activities/calories', base_date=start_date, detail_level=descriptor)

            time_list = []
            val_list = []
            for i in fit_statsHR['activities-calories-intraday']['dataset']:
                val_list.append(i['value'])
                time_list.append(i['time'])
            heartdf = ({'Calories':val_list,'Time':time_list})
            print(heartdf)

        return heartdf

    def get_elevation_data(self, start_date, descriptor):
        '''
        get_elevation_data
        :param start_date: required, specifies start date for date range or date
                           for intraday requests
        :param descriptor: can be either end_date or period depending on users input
                            end_date for daily values period for specific values throughout day
        :end_date: optional, when specified gets a range of data from start
                         date to end date
        :period: time increments for intraday data, defaults to 15min.
                       Can also be 1sec or 1min.
        :return: the time series data
        '''
        # Check if descriptor is date format
        r = re.compile('\d{4}-\d{2}-\d{2}')
        if(r.match(descriptor)):
            fit_statsHR = self.client.time_series('activities/elevation', base_date=start_date, end_date=descriptor)

            time_list = []
            val_list = []
            for i in fit_statsHR['activities-elevation']:
                val_list.append(i['value'])
                time_list.append(i['dateTime'])
            heartdf = ({'Elevation':val_list,'Time':time_list})
            print(heartdf)
        else:
            fit_statsHR = self.client.intraday_time_series('activities/elevation', base_date=start_date, detail_level=descriptor)

            time_list = []
            val_list = []
            for i in fit_statsHR['activities-elevation-intraday']['dataset']:
                val_list.append(i['value'])
                time_list.append(i['time'])
            heartdf = ({'Elevation':val_list,'Time':time_list})
            print(heartdf)

        return heartdf

    def get_floors_data(self, start_date, descriptor):
        '''
        get_floors_data
        :param start_date: required, specifies start date for date range or date
                           for intraday requests
        :param descriptor: can be either end_date or period depending on users input
                            end_date for daily values period for specific values throughout day
        :end_date: optional, when specified gets a range of data from start
                         date to end date
        :period: time increments for intraday data, defaults to 15min.
                       Can also be 1sec or 1min.
        :return: the time series data
        '''
        # Check if descriptor is date format
        r = re.compile('\d{4}-\d{2}-\d{2}')
        if(r.match(descriptor)):
            fit_statsHR = self.client.time_series('activities/floors', base_date=start_date, end_date=descriptor)

            time_list = []
            val_list = []
            for i in fit_statsHR['activities-floors']:
                val_list.append(i['value'])
                time_list.append(i['dateTime'])
            heartdf = ({'Floors':val_list,'Time':time_list})
            print(heartdf)
        else:
            fit_statsHR = self.client.intraday_time_series('activities/floors', base_date=start_date, detail_level=descriptor)

            time_list = []
            val_list = []
            for i in fit_statsHR['activities-floors-intraday']['dataset']:
                val_list.append(i['value'])
                time_list.append(i['time'])
            heartdf = ({'Floors':val_list,'Time':time_list})
            print(heartdf)

        return heartdf
