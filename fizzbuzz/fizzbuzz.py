def convert(number: int) -> str:
    __ensure_is_between_boundaries(number)

    if __is_divisible_by_3_and_5(number):
        return "fizzbuzz"
    if __is_divisible_by_3(number):
        return "fizz"
    if __is_divisible_by_5(number):
        return "buzz"
    return str(number)


def __ensure_is_between_boundaries(number):
    if __is_between_boundaries(number):
        raise ValueError(f'Received {number} which is not between 1-100')


def __is_between_boundaries(number):
    return not 1 <= number <= 100


def __is_divisible_by_3_and_5(number):
    return __is_divisible_by_3(number) and __is_divisible_by_5(number)


def __is_divisible_by_3(number: int):
    return number % 3 == 0


def __is_divisible_by_5(number: int):
    return number % 5 == 0


if __name__ == '__main__':
    print('Hello World!')
