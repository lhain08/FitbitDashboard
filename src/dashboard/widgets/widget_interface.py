

class WidgetInterface():
    def __init__(self, data_manager, data_type, time_period):
        self.data_manager = data_manager
        self.data_type = data_type
        self.time_period = time_period

    def render(self):
        raise Exception("Not Implemented")