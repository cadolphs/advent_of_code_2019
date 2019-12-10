from threaded_computer import ThreadedComputer
from queue import Queue


class AmplifierLoop:
    def __init__(self, program, n_computers):
        self.queues = [Queue() for _ in range(n_computers)]
        self.n_computers = n_computers
        self.computers = []
        for i in range(n_computers):
            input_queue = self.queues[i]
            output_queue = self.queues[(i + 1) % n_computers]
            self.computers.append(
                ThreadedComputer(
                    program=list(program),
                    input_queue=input_queue,
                    output_queue=output_queue,
                )
            )

    def run(self):
        for computer in self.computers:
            computer.start()

        for computer in self.computers:
            computer.finish()

    def get(self, n):
        return self.queues[(n + 1) % self.n_computers].get()

    def put(self, n, val):
        self.queues[n].put(val)

    def set_phases(self, phases):
        for queue, phase in zip(self.queues, phases):
            queue.put(phase)
