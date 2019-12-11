from image import Image
import numpy as np


def test_can_load_twolayer_image():
    image = Image(data="123456789012", shape=(3, 2))

    # Now image layer 1, bottom right pixel should be 6
    assert image.value_at(0, 2, 1) == 6
    assert image.value_at(1, 1, 0) == 8


def test_simple_image_has_correct_checlsum():
    image = Image(data="123456789012", shape=(3, 2))
    # First layer, 123456 has no zeros, so it gets chosen
    # It has one one and one 2, so checksum is one
    assert image.checksum() == 1

    image = Image(data="121226789012", shape=(3, 2))
    assert image.checksum() == 6


def test_simple_rendering():
    image = Image(data="0222112222120000", shape=(2, 2))
    assert np.all(image.render() == np.array([[0, 1], [1, 0]]))
