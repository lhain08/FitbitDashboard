

class WidgetInterface():
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def render(self):
        raise Exception("Not Implemented")