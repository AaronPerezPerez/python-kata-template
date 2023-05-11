import pytest

import fizzbuzz


@pytest.mark.parametrize("non_divisible", [[1, "1"], [2, "2"], [4, "4"], [7, "7"]])
def test_should_return_the_numbers_as_strings(non_divisible):
    assert fizzbuzz.convert(non_divisible[0]) == non_divisible[1]


@pytest.mark.parametrize("number_divisible_by_three", [3, 6, 9, 12])
def test_should_return_fizz_with_numbers_divisible_by_three(number_divisible_by_three):
    assert fizzbuzz.convert(number_divisible_by_three) == "fizz"


@pytest.mark.parametrize("number_divisible_by_five", [5, 10, 20, 25])
def test_should_return_fizz_with_numbers_divisible_by_five(number_divisible_by_five):
    assert fizzbuzz.convert(number_divisible_by_five) == "buzz"


@pytest.mark.parametrize("number_divisible_by_five_and_three", [15, 30, 45, 60])
def test_should_return_fizz_with_numbers_divisible_by_five_and_three(number_divisible_by_five_and_three):
    assert fizzbuzz.convert(number_divisible_by_five_and_three) == "fizzbuzz"


@pytest.mark.parametrize("number_lower_than_1", [0, -123, -322, -897])
def test_should_raise_an_error_when_the_number_is_lower_than_one(number_lower_than_1):
    with pytest.raises(ValueError):
        fizzbuzz.convert(number_lower_than_1)


@pytest.mark.parametrize("number_higher_than_100", [101, 205, 333, 412])
def test_should_raise_an_error_when_the_number_is_higher_than_one_hundred(number_higher_than_100):
    with pytest.raises(ValueError):
        fizzbuzz.convert(number_higher_than_100)
