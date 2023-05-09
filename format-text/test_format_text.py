import pytest

import format_text


@pytest.mark.parametrize("params", [
    {"input": "foo", "expected": "bar"}
])
def test_should_somehow_work(params):
    assert format_text.execute(params["input"]) == params["expected"]
