from helpers import get_data
from amplifier_queue import AmplifierQueue
from itertools import permutations

data = get_data(day=7)
program = list(map(int, data.split(',')))

max_output = 0
max_permutation = None
for permutation in permutations(range(5)):
    queue = AmplifierQueue(program, permutation)
    queue.run()
    output = queue.get_output()

    if output > max_output:
        max_output = output
        max_permutation = permutation

print(f"Highest output of {max_output} achieved for input {permutation}")
