from queue import Queue
import pytest

from threaded_computer import ThreadedComputer


def test_reads_from_input_queue():
    input_queue = Queue()
    computer = ThreadedComputer([3, 0, 99], input_queue=input_queue)
    input_queue.put(42)

    computer.start()
    computer.finish()

    assert computer[0] == 42


def test_reads_asynchronously_from_input_queue():
    input_queue = Queue()
    computer = ThreadedComputer([3, 0, 99], input_queue=input_queue)

    print(f"Starting computer...")
    computer.start()
    print(f"Putting 42 into queue")
    input_queue.put(42)
    computer.finish()

    assert computer[0] == 42


def test_writes_to_output_queue():
    output_queue = Queue()
    computer = ThreadedComputer([104, 42, 99], output_queue=output_queue)
    computer.start()
    computer.finish()

    assert output_queue.get(block=False) == 42


def test_writes_to_output_asynchronously():
    output_queue = Queue()
    computer = ThreadedComputer([104, 42, 99], output_queue=output_queue)
    computer.start()
    assert output_queue.get(block=True, timeout=2) == 42
    computer.finish()
