from calculator.sum import sum


def test_sum():
    assert sum(2, 3) == 5


def test_sum_minus():
    assert sum(-2, -3) == -5
