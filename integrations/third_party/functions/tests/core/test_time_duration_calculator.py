from unittest.mock import patch, MagicMock
from ...actions.TimeDurationCalculator import main
from integration_testing.set_meta import set_metadata


class MockSession:
    def __init__(self):
        self.result_json = {}

    def add_result_json(self, data):
        self.result_json.update(data)


@set_metadata
def test_time_duration_calculator_success():
    session = MockSession()

    with patch("functions.actions.TimeDurationCalculator.SiemplifyAction") as MockSiemplifyAction:
        mock_siemplify = MagicMock()
        MockSiemplifyAction.return_value = mock_siemplify

        # 👉 Настраиваем mock так, чтобы действие использовало наш mock session
        mock_siemplify.extract_action_param.side_effect = lambda name, **kwargs: {
            "Input DateTime 1": "2024-01-01 00:00:00",
            "Input DateTime 1 Format": "%Y-%m-%d %H:%M:%S",
            "Input DateTime 2": "2025-01-01 00:00:00",
            "Input DateTime 2 Format": "%Y-%m-%d %H:%M:%S",
        }[name]

        mock_siemplify.result = session  # 👈 вот ключ — связываем mock с session

        main()

    # 🔍 Проверка
    assert hasattr(session, "result_json")
    assert "years" in session.result_json
    assert session.result_json["years"] == 1
