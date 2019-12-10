from opcode_computer import OpcodeComputer
from threading import Thread


class ThreadedComputer(OpcodeComputer):
    def __init__(self, program, input_queue=None, output_queue=None):
        self.input_queue = input_queue
        self.output_queue = output_queue

        super().__init__(program, output=self.write_to_output)

    def start(self):
        self.thread = Thread(target=self.run)
        print(f"Calling computer thread start")
        self.thread.start()

    def finish(self):
        print("Waiting for thread to finish")
        self.thread.join()
        print("Thread finished")

    def read_input(self):
        print(f"read_input was called")
        return self.input_queue.get(block=True)

    def write_to_output(self, val):
        self.output_queue.put(val)
