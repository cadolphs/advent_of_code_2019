from amplifier_loop import AmplifierLoop


def test_loop_n_has_n_computers():
    loop = AmplifierLoop([], n_computers=3)
    assert len(loop.computers) == 3
    assert loop.computers[0] != loop.computers[1]


def test_output_queue_of_computer_n_is_input_queue_of_computer_n_plus_1():
    loop = AmplifierLoop([], n_computers=3)
    for computer in loop.computers:
        computer.write_to_output(42)

    for computer in loop.computers:
        assert computer.read_input() == 42


def test_manually_put_stuff_to_queues():
    loop = AmplifierLoop([], n_computers=3)
    for i in range(3):
        loop.put(i, 42)

    for computer in loop.computers:
        assert computer.read_input() == 42


def test_get_value_left_in_queue():
    loop = AmplifierLoop([], n_computers=3)
    loop.computers[-1].write_to_output(42)

    assert loop.get(2) == 42


def test_homepage_example():
    program = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26, 27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5".split(
        ","
    )
    program = [int(instr) for instr in program]

    loop = AmplifierLoop(program, n_computers=5)
    loop.set_phases([9, 8, 7, 6, 5])
    loop.put(0, 0)
    loop.run()

    assert loop.get(-1) == 139629729
