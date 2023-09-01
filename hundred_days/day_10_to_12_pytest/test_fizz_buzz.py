from hundred_days.day_10_to_12_pytest.fizz_buzz import fizz_buzz
import pytest

@pytest.mark.parametrizs('arg','ret', [
    (1,1),
    (2,2),
    (3,'fizz'),
    (4,4),
    (5,'buzz'),
    (6,'fizz'),
    (7,7),
    (8,8),
    (9,'fizz'),
    (10,'buzz'),
    (11,11),
    (12,'fizz'),
    (13,13),
    (14,14),
    (15,'fizz buzz'),
    (16,16),
])
def test_fizz_buzz():
    assert fizz_buzz(1) == 1
    assert fizz_buzz(2) == 2
    assert fizz_buzz(3) == 'fizz'