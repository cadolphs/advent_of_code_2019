from internal_memory import InternalMemory


def test_reading_from_any_address_in_fresh_memory_gives_zero():
    memory = InternalMemory()

    assert memory[42] == 0


def test_can_set_and_read_from_any_address():
    memory = InternalMemory()
    memory[3] = 42
    assert memory[3] == 42


def test_can_get_slice():
    memory = InternalMemory()
    assert memory[3:5] == [0, 0]
