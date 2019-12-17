from collections import defaultdict


class InternalMemory:
    def __init__(self):
        self._memory = defaultdict(int)

    def __getitem__(self, key):
        if isinstance(key, slice):
            idxs = range(*key.indices(key.stop))
            return [self._memory[idx] for idx in idxs]
        elif isinstance(key, int):
            if key < 0:
                raise IndexError("No negative indices please.")
            return self._memory[key]

    def __setitem__(self, key, item):
        self._memory[key] = item

    def _raw(self):
        max_idx = max(self._memory.keys())

        return [self._memory[key] for key in range(max_idx + 1)]

    def __eq__(self, value):
        if isinstance(value, InternalMemory):
            return self._raw() == value._raw()
        else:
            return self._raw() == value
