from password_filter import PasswordFilter, PasswordFilterExactPairs
import pytest


def test_digit_range_test():
    pwd_filter = PasswordFilter(1, 9999999)

    assert pwd_filter.has_six_digits(123456) is True
    assert pwd_filter.has_six_digits(12345) is False
    assert pwd_filter.has_six_digits(1234567) is False


def test_range_check():
    pwd_filter = PasswordFilter(5, 10)
    assert pwd_filter.is_in_range(4) is False
    assert pwd_filter.is_in_range(11) is False
    assert pwd_filter.is_in_range(5) is True
    assert pwd_filter.is_in_range(7) is True
    assert pwd_filter.is_in_range(10) is True


@pytest.mark.parametrize("pwd,expected", [(0, False), (1, False), (12, False), (22, True), (223, True), (123, False), (122, True)])
def test_adjacent_double(pwd, expected):
    pwd_filter = PasswordFilter(100000, 999999)

    assert pwd_filter.has_adjacent_pair(pwd) is expected


@pytest.mark.parametrize("pwd,expected", [(0, True), (21, False), (12, True), (121, False)])
def test_nondecreasing_digits(pwd, expected):
    pwd_filter = PasswordFilter(100000, 999999)

    assert pwd_filter.has_nondecreasing_digits(pwd) is expected


@pytest.mark.parametrize("pwd,expected", [(111111, True), (223450, False), (123789, False)])
def test_all_rules_together(pwd, expected):
    pwd_filter = PasswordFilter(100000, 999999)

    assert pwd_filter(pwd) is expected


@pytest.mark.parametrize("pwd,expected", [(111111, False), (112345, True), (123444, False), (111122, True)])
def test_exact_pairs(pwd, expected):
    pwd_filter = PasswordFilterExactPairs(100000, 999999)

    assert pwd_filter.has_adjacent_pair(pwd) is expected
