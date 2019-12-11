import numpy as np


class Image:
    def __init__(self, data, shape):
        int_data = self.parse_data(data)
        self.shape = shape
        self.internal_data = self.reshape_data(int_data)

    def value_at(self, layer_idx, width_idx, height_idx):
        return self.internal_data[layer_idx, height_idx, width_idx]

    def parse_data(self, data):
        return np.array([int(c) for c in data])

    def reshape_data(self, int_data):
        return np.reshape(int_data, (-1, self.shape[1], self.shape[0]))

    def checksum(self):
        layer_to_check = self._get_layer_with_fewest_0s()
        return self._get_checksum_for_layer(layer_to_check)

    def _get_layer_with_fewest_0s(self):
        nonzeros = np.count_nonzero(self.internal_data == 0, axis=(1, 2))
        return np.argmin(nonzeros)

    def _get_checksum_for_layer(self, layer_idx):
        layer = self.internal_data[layer_idx, :, :]
        number_of_ones = np.count_nonzero(layer == 1)
        number_of_twos = np.count_nonzero(layer == 2)

        return number_of_ones * number_of_twos

    def render(self):
        transparentified_data = self._make_transparent(self.internal_data)

        first_non_transparent_pos = np.argmax(transparentified_data != 0, axis=0)
        idx_array = np.expand_dims(first_non_transparent_pos, axis=0)

        colors = np.take_along_axis(self.internal_data, idx_array, axis=0)[0]

        return colors

    def _make_transparent(self, data):
        return -(data - 2)
