"""Data Manager Module: Responsible for app's interactions with database/api"""
import re
from datetime import datetime
from fitbit import exceptions

import api.connect as connect

class DataManager():
    '''
    DataManager Class
    Responsible for retrieving data from the Fitbit Client
    '''
    def __init__(self, client=None):
        self.client = client
        if self.client is None:
            self.client = connect.get_client()

    def get_data(self, data_type, start_date, end_date):
        method = None
        if data_type == 'Steps':
            method = self.get_steps_data
        elif data_type == 'Distance':
            method = self.get_distance_data
        elif data_type == 'Calories':
            method = self.get_calories_data
        elif data_type == 'Elevation':
            method = self.get_elevation_data
        elif data_type == 'Floors':
            method = self.get_floors_data

        if method == None:
            raise Exception("Data type does not exist")

        return method(start_date, end_date)

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
        r = re.compile(r'\d{4}-\d{2}-\d{2}')
        if(r.match(descriptor)):
            fit_statsHR = self.client.time_series('activities/steps', base_date=start_date, end_date=descriptor)

            time_list = []
            val_list = []
            for i in fit_statsHR['activities-steps']:
                val_list.append(float(i['value']))
                time_list.append(i['dateTime'])
            heartdf = ({'Steps':val_list,'Time':time_list})
        else:
            fit_statsHR = self.client.intraday_time_series('activities/steps', base_date=start_date, detail_level=descriptor)

            time_list = []
            val_list = []
            for i in fit_statsHR['activities-steps-intraday']['dataset']:
                val_list.append(float(i['value']))
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
        r = re.compile(r'\d{4}-\d{2}-\d{2}')
        if(r.match(descriptor)):
            fit_statsHR = self.client.time_series('activities/distance', base_date=start_date, end_date=descriptor)

            time_list = []
            val_list = []
            for i in fit_statsHR['activities-distance']:
                val_list.append(float(i['value']))
                time_list.append(i['dateTime'])
            heartdf = ({'Distance':val_list,'Time':time_list})
        else:
            fit_statsHR = self.client.intraday_time_series('activities/distance', base_date=start_date, detail_level=descriptor)

            time_list = []
            val_list = []
            for i in fit_statsHR['activities-distance-intraday']['dataset']:
                val_list.append(float(i['value']))
                time_list.append(i['time'])
            heartdf = ({'Distance':val_list,'Time':time_list})

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
        r = re.compile(r'\d{4}-\d{2}-\d{2}')
        if(r.match(descriptor)):
            fit_statsHR = self.client.time_series('activities/calories', base_date=start_date, end_date=descriptor)

            time_list = []
            val_list = []
            for i in fit_statsHR['activities-calories']:
                val_list.append(int(i['value']))
                time_list.append(i['dateTime'])
            heartdf = ({'Calories':val_list,'Time':time_list})
        else:
            fit_statsHR = self.client.intraday_time_series('activities/calories', base_date=start_date, detail_level=descriptor)

            time_list = []
            val_list = []
            for i in fit_statsHR['activities-calories-intraday']['dataset']:
                val_list.append(int(i['value']))
                time_list.append(i['time'])
            heartdf = ({'Calories':val_list,'Time':time_list})

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
        r = re.compile(r'\d{4}-\d{2}-\d{2}')
        if(r.match(descriptor)):
            fit_statsHR = self.client.time_series('activities/elevation', base_date=start_date, end_date=descriptor)

            time_list = []
            val_list = []
            for i in fit_statsHR['activities-elevation']:
                val_list.append(float(i['value']))
                time_list.append(i['dateTime'])
            heartdf = ({'Elevation':val_list,'Time':time_list})
        else:
            fit_statsHR = self.client.intraday_time_series('activities/elevation', base_date=start_date, detail_level=descriptor)

            time_list = []
            val_list = []
            for i in fit_statsHR['activities-elevation-intraday']['dataset']:
                val_list.append(float(i['value']))
                time_list.append(i['time'])
            heartdf = ({'Elevation':val_list,'Time':time_list})

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
        r = re.compile(r'\d{4}-\d{2}-\d{2}')
        if(r.match(descriptor)):
            fit_statsHR = self.client.time_series('activities/floors', base_date=start_date, end_date=descriptor)

            time_list = []
            val_list = []
            for i in fit_statsHR['activities-floors']:
                val_list.append(float(i['value']))
                time_list.append(i['dateTime'])
            heartdf = ({'Floors':val_list,'Time':time_list})
        else:
            fit_statsHR = self.client.intraday_time_series('activities/floors', base_date=start_date, detail_level=descriptor)

            time_list = []
            val_list = []
            for i in fit_statsHR['activities-floors-intraday']['dataset']:
                val_list.append(float(i['value']))
                time_list.append(i['time'])
            heartdf = ({'Floors':val_list,'Time':time_list})

        return heartdf

    def get_sleep_data(self, start_date):
        '''
        get_sleep_data
        :param start_date: required, specifies date for sleep data 
                        to be gathered from
        :return: the time series data
        '''
        date = datetime.strptime(start_date, "%Y-%m-%d")
        fit_statsHR = self.client.get_sleep(date)
        
        time_list = []
        val_list = []
        for i in fit_statsHR['sleep'][0]['minuteData']:
            val_list.append(float(i['value']))
            time_list.append(i['dateTime'])
        heartdf = ({'Sleep':val_list,'Time':time_list})

        return heartdf
