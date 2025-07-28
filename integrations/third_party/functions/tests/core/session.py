class MockSession:
    def __init__(self):
        self.results = []
        self.result_json = {}

    def set_results(self, results):
        self.results = results

    def set_result_json(self, result_json):
        self.result_json = result_json

    @property
    def action_output(self):
        return self
