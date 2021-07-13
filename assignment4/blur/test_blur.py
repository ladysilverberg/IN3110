#!/usr/bin/env python

from . import blur
import numpy as np

def test_max_array_value():
    random_arr = np.random.randint(0, 255, size=(250, 250, 3))
    max_value_before = np.amax(random_arr)
    blurred = blur.blur_image(random_arr)
    max_value_after = np.amax(blurred)
    assert max_value_after < max_value_before

def test_pixel():
    random_arr = np.random.randint(0, 255, size=(250, 250, 3))
    blurred = blur.blur_image(random_arr)
    rand_h = 1
    rand_w = 1
    rand_c = 1
    average_value = (random_arr[rand_h][rand_w][rand_c]
                     + random_arr[rand_h-1][rand_w][rand_c]
                     + random_arr[rand_h+1][rand_w][rand_c]
                     + random_arr[rand_h][rand_w-1][rand_c]
                     + random_arr[rand_h][rand_w+1][rand_c]
                     + random_arr[rand_h-1][rand_w-1][rand_c]
                     + random_arr[rand_h-1][rand_w+1][rand_c]
                     + random_arr[rand_h+1][rand_w-1][rand_c]
                     + random_arr[rand_h+1][rand_w+1][rand_c]
                     ) / 9
    assert blurred[rand_h][rand_w][rand_c] == int(average_value)

if __name__ == '__main__':
    test_max_array_value()
    test_pixel()
