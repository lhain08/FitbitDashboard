from api import connect

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
        :param start_date: required, specifies start date for date range or date for intraday requests
        :param end_date: optional, when specified gets a range of data from start date to end date
        :param period: time increments for intraday data, defaults to 15min. Can also be 1sec or 1min.
        :return: the time series data
        '''
        if start_date is None:
            raise Exception("No start date given")

        if end_date is not None:
            data = self.client.time_series('activities/' + data_type, base_date=start_date, end_date=end_date)
            return data['activites-' + data_type]

        else:
            data = self.client.intraday_time_series('activities/' + data_type, base_date=start_date, detail_level=period)
            return data['activities-' + data_type + '-intraday']

    def get_steps_data(self, start_date, end_date=None, period='15min'):
        '''
        get_steps_data
        :param start_date: required, specifies start date for date range or date for intraday requests
        :param end_date: optional, when specified gets a range of data from start date to end date
        :param period: time increments for intraday data, defaults to 15min. Can also be 1sec or 1min.
        :return: the time series data
        '''
        return self.__get_time_series('steps', start_date, end_date, period)

    def get_distance_data(self, start_date, end_date=None, period='15min'):
        '''
        get_distance_data
        :param start_date: required, specifies start date for date range or date for intraday requests
        :param end_date: optional, when specified gets a range of data from start date to end date
        :param period: time increments for intraday data, defaults to 15min. Can also be 1sec or 1min.
        :return: the time series data
        '''
        return self.__get_time_series('distance', start_date, end_date, period)

    def get_calories_data(self, start_date, end_date=None, period='15min'):
        '''
        get_calories_data
        :param start_date: required, specifies start date for date range or date for intraday requests
        :param end_date: optional, when specified gets a range of data from start date to end date
        :param period: time increments for intraday data, defaults to 15min. Can also be 1sec or 1min.
        :return: the time series data
        '''
        return self.__get_time_series('calories', start_date, end_date, period)

    def get_elevation_data(self, start_date, end_date=None, period='15min'):
        '''
        get_elevation_data
        :param start_date: required, specifies start date for date range or date for intraday requests
        :param end_date: optional, when specified gets a range of data from start date to end date
        :param period: time increments for intraday data, defaults to 15min. Can also be 1sec or 1min.
        :return: the time series data
        '''
        return self.__get_time_series('elevation', start_date, end_date, period)

    def get_floors_data(self, start_date, end_date=None, period='15min'):
        '''
        get_floors_data
        :param start_date: required, specifies start date for date range or date for intraday requests
        :param end_date: optional, when specified gets a range of data from start date to end date
        :param period: time increments for intraday data, defaults to 15min. Can also be 1sec or 1min.
        :return: the time series data
        '''
        return self.__get_time_series('floors', start_date, end_date, period)
