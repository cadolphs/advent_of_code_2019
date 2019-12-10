from helpers import get_data
from amplifier_queue import AmplifierQueue
from itertools import permutations
from amplifier_loop import AmplifierLoop

data = get_data(day=7)
program = list(map(int, data.split(",")))

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

# Now for part b...
max_output = 0
max_permutation = None

for permutation in permutations(range(5, 10)):
    loop = AmplifierLoop(program, n_computers=5)
    loop.set_phases(permutation)
    loop.put(0, 0)

    loop.run()

    output = loop.get(-1)
    if output > max_output:
        max_output = output
        max_permutation = permutation

print(f"Highest output of {max_output} achieved for phase settings {permutation}")
