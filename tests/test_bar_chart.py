from unittest.mock import Mock

from src.dashboard.widgets.bar_chart import BarChartWidget


class TestBarChartWidget:
    # Create a new mock client and data manager
    mock_data_manager = Mock()

    def test_bar_chart(self):
        bar_chart_under_test = BarChartWidget(
            self.mock_data_manager,
            "Steps",
            "2022-04-01",
            "2022-04-04",
            "Test Bar Chart",
            0,
            None,
        )

        self.mock_data_manager.get_data.return_value = {
            "Time": ["2022-04-01", "2022-04-02", "2022-04-03"],
            "Steps": [1000, 2000, 3000],
        }

        bar_chart_under_test.render()

        # Check database call is correct
        assert self.mock_data_manager.get_data.called_with(
            "Steps", "2022-04-01", "2022-04-04"
        )

        # Verify the output content

        # assert type(widget_output) == html.Div
        # graph = widget_output.children[0]
        # assert type(graph) == dcc.Graph
        # fig = graph.figure
        # assert fig.data[0].type == 'bar'
        # assert fig.data[0].x == ('2022-04-01', '2022-04-02', '2022-04-03',)
        # assert fig.data[0].y == (1000, 2000, 3000)
