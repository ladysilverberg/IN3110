import argparse
import cv2
import os
import numpy as np
from . import blur_1 as python_blur
from . import blur_2 as numpy_blur
from . import blur_3 as numba_blur
from . import blur_faces as face_blur

def handle_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "--image_in",
            required=True,
            help="Filename of image to blur")
    parser.add_argument(
            "--image_out",
            required=True,
            help="Filename of blurred image")
    parser.add_argument(
            "--mode",
            required=True,
            help="Blur mode to use. Can be python, numpy, numba or faces.")
    args = parser.parse_args()
    assert os.path.exists(args.image_in), "Argument image_in must refer to an existing file." \
                                          + f"Found no file named \'{args.image_in}\'."
    return args

def blur_image_script(image_in, image_out, mode):
    assert image_in is not None, "Value of image_in is None. Image probably failed to read."
    try:
        img = np.array(image_in)
    except ValueError:
        raise ValueError("Argument image_in is not of array-like type.")

    if mode == "python":
        python_blur.blur_image(img, image_out)
    elif mode == "numpy":
        numpy_blur.blur_image(img, image_out)
    elif mode == "numba":
        numba_blur.blur_image(img, image_out)
    elif mode == "faces":
        face_blur.blur_faces(img, image_out)
    else:
        print("Invalid mode!")

def blur_image(input_filename, output_filename=None):
    return numpy_blur.blur_image(input_filename, output_filename)

def main():
    args = handle_arguments()
    img = cv2.imread(args.image_in)
    blur_image_script(img, args.image_out, args.mode)

if __name__ == "__main__":
    main()
