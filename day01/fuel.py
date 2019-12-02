def compute_fuel(weight_list):
    '''To compute total weight of fuel, add up the fule for each module'''
    return sum(fuel_for_weight(weight) for weight in weight_list)


def fuel_for_weight(weight):
    '''This performs integer division (rounding down!) and applies the formula. Catches negative weight'''
    return max(weight // 3 - 2, 0)


def compute_fuel_total(weight_list):
    '''To compute total weight of fuel including fuel, add up fuel for each module'''
    return sum(total_fuel_per_module(weight) for weight in weight_list)


def total_fuel_per_module(weight):
    '''To compute total weight of fuel for a module, add up the fuel for the module's weight 
    and the fuel for the fuel.'''
    fuel = fuel_for_weight(weight)
    total_fuel = 0
    while fuel > 0:
        total_fuel += fuel
        fuel = fuel_for_weight(fuel)
    return total_fuel


if __name__ == "__main__":
    from helpers import get_data
    data = get_data(day=1).split('\n')
    amount = compute_fuel(int(entry) for entry in data)
    print(f"Required fuel amount is {amount}")

    amount = compute_fuel_total(int(entry) for entry in data)
    print(f"Required TOTAL amount of fuel is {amount}")