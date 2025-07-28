class Product:
    def __init__(self):
        self._input_data = {}

    def set_input_data(self, data: dict):
        self._input_data = data

    def get_input_data(self) -> dict:
        return self._input_data
