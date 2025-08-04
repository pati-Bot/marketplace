from __future__ import annotations

from TIPCommon.base.action import ExecutionState
from integration_testing.platform.script_output import MockActionOutput
from integration_testing.set_meta import set_metadata

from ...actions import MathFunctions

pytest_plugins: tuple[str, ...] = ("integration_testing.conftest",)


class TestMathAbs:
    @set_metadata(parameters={"Numbers": "-7", "Function": "Abs"})
    def test_math_abs_on_negative_number(self, action_output: MockActionOutput) -> None:
        MathFunctions.main()
        assert action_output.results.result_value == 7.0
        assert action_output.results.output_message == "[-7.0] successfully converted to [7.0] with abs function"
        assert action_output.results.json_output.json_result == [7.0]
        assert action_output.results.execution_state is ExecutionState.COMPLETED


class TestMathFloat:
    @set_metadata(parameters={"Numbers": "3", "Function": "Float"})
    def test_math_float_on_integer(self, action_output: MockActionOutput) -> None:
        MathFunctions.main()
        assert action_output.results.result_value == 3.0
        assert action_output.results.output_message == "[3.0] successfully converted to [3.0] with float function"
        assert action_output.results.json_output.json_result == [3.0]
        assert action_output.results.execution_state is ExecutionState.COMPLETED


class TestMathDisplay:
    @set_metadata(parameters={"Numbers": "1.2345", "Function": "Display"})
    def test_math_display(self, action_output: MockActionOutput) -> None:
        MathFunctions.main()
        assert action_output.results.result_value == 1.2345
        assert action_output.results.output_message == "[1.2345] successfully converted to [1.2345] with display function"
        assert action_output.results.json_output.json_result == [1.2345]
        assert action_output.results.execution_state is ExecutionState.COMPLETED


class TestMathHex:
    @set_metadata(parameters={"Numbers": "255", "Function": "Hex"})
    def test_math_hex(self, action_output: MockActionOutput) -> None:
        MathFunctions.main()
        assert action_output.results.result_value == "0xff"
        assert action_output.results.output_message == "[255.0] successfully converted to [0xff] with hex function"
        assert action_output.results.json_output.json_result == ["0xff"]
        assert action_output.results.execution_state is ExecutionState.COMPLETED


class TestMathInt:
    @set_metadata(parameters={"Numbers": "4.9", "Function": "Int"})
    def test_math_int_on_float(self, action_output: MockActionOutput) -> None:
        MathFunctions.main()
        assert action_output.results.result_value == 4
        assert action_output.results.output_message == "[4.9] successfully converted to [4] with int function"
        assert action_output.results.json_output.json_result == [4]
        assert action_output.results.execution_state is ExecutionState.COMPLETED


class TestMathMax:
    @set_metadata(parameters={"Numbers": "1, 5, 3", "Function": "Max"})
    def test_math_max(self, action_output: MockActionOutput) -> None:
        MathFunctions.main()
        assert action_output.results.result_value == 5.0
        assert action_output.results.output_message == "[1.0, 5.0, 3.0] successfully converted to [5.0] with max function"
        assert action_output.results.json_output.json_result == [5.0]
        assert action_output.results.execution_state is ExecutionState.COMPLETED


class TestMathMin:
    @set_metadata(parameters={"Numbers": "2, -1, 0", "Function": "Min"})
    def test_math_min(self, action_output: MockActionOutput) -> None:
        MathFunctions.main()
        assert action_output.results.result_value == -1.0
        assert action_output.results.output_message == "[2.0, -1.0, 0.0] successfully converted to [-1.0] with min function"
        assert action_output.results.json_output.json_result == [-1.0]
        assert action_output.results.execution_state is ExecutionState.COMPLETED


class TestMathRound:
    @set_metadata(parameters={"Numbers": "3.75", "Function": "Round"})
    def test_math_round(self, action_output: MockActionOutput) -> None:
        MathFunctions.main()
        assert action_output.results.result_value == 4
        assert action_output.results.output_message == "[3.75] successfully converted to [4] with round function"
        assert action_output.results.json_output.json_result == [4]
        assert action_output.results.execution_state is ExecutionState.COMPLETED


class TestMathSort:
    @set_metadata(parameters={"Numbers": "5, 1, 3", "Function": "Sort"})
    def test_math_sort(self, action_output: MockActionOutput) -> None:
        MathFunctions.main()
        assert action_output.results.result_value == [1.0, 3.0, 5.0]
        assert action_output.results.output_message == "[5.0, 1.0, 3.0] successfully converted to [1.0, 3.0, 5.0] with sort function"
        assert action_output.results.json_output.json_result == [1.0, 3.0, 5.0]
        assert action_output.results.execution_state is ExecutionState.COMPLETED


class TestMathSum:
    @set_metadata(parameters={"Numbers": "1.5, 2.5", "Function": "Sum"})
    def test_math_sum(self, action_output: MockActionOutput) -> None:
        MathFunctions.main()
        assert action_output.results.result_value == 4.0
        assert action_output.results.output_message == "[1.5, 2.5] successfully converted to [4.0] with sum function"
        assert action_output.results.json_output.json_result == [4.0]
        assert action_output.results.execution_state is ExecutionState.COMPLETED
