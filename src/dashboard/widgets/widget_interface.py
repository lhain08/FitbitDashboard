class WidgetInterface():
    def __init__(self, data_manager, data_type, start_date, end_date, name, goal):
        self.data_manager = data_manager
        self.data_type = data_type
        self.start_date = start_date
        self.end_date = end_date
        self.intraday = False
        if self.start_date == self.end_date:
            self.end_date = '15min' # Set the end date as a period instead for intraday data
            self.intraday = True
        self.name = name
        self.goal = goal

    def render(self):
        raise Exception("Not Implemented")
