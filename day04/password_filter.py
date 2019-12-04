class PasswordFilter:

    def __init__(self, low: int, high: int):
        self.low, self.high = low, high

    def has_six_digits(self, password: int):
        return 100000 <= password <= 999999

    def is_in_range(self, password: int):
        return self.low <= password <= self.high

    def has_adjacent_pair(self, password: int):
        pwd = f"{password}"
        for i in range(len(pwd) - 1):
            if pwd[i] == pwd[i + 1]:
                return True
        return False

    def has_nondecreasing_digits(self, password: int):
        pwd = f"{password}"
        for i in range(len(pwd) - 1):
            if pwd[i] > pwd[i + 1]:
                return False
        return True

    def __call__(self, password: int):
        return (self.has_six_digits(password) and
                self.is_in_range(password) and
                self.has_adjacent_pair(password) and
                self.has_nondecreasing_digits(password))


class PasswordFilterExactPairs(PasswordFilter):

    def has_adjacent_pair(self, password):
        pwd = f"{password}"

        current_symbol = pwd[0]
        current_count = 1
        for i in range(1, len(pwd)):
            if pwd[i] == current_symbol:
                current_count += 1
            else:
                if current_count == 2:
                    return True
                current_symbol = pwd[i]
                current_count = 1
        return current_count == 2
