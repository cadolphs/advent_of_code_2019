from password_filter import PasswordFilter, PasswordFilterExactPairs
from helpers import get_data

data = get_data(day=4)
low, high = map(int, data.split('-'))

pwd_filter = PasswordFilter(low, high)
valid_passwords = [pwd for pwd in range(low, high + 1) if pwd_filter(pwd)]

print(f"Number of valid passwords is {len(valid_passwords)}")

pwd_filter = PasswordFilterExactPairs(low, high)
valid_passwords = [pwd for pwd in range(low, high + 1) if pwd_filter(pwd)]

print(f"Number of valid passwords with the exact pair rule is {len(valid_passwords)}")