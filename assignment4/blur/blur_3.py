import cv2
import numpy as np
from numba import jit


@jit(nopython=True)
def convolve(img, blurred, H, W, C):
    for c in range(C):
        for w in range(W):
            for h in range(H):
                th = h + 1
                tw = w + 1
                tc = c + 1
                blurred[h][w][c] = (img[th][tw][tc]
                                    + img[th-1][tw][tc]
                                    + img[th+1][w][c]
                                    + img[th][tw-1][tc]
                                    + img[th][tw+1][tc]
                                    + img[th-1][tw-1][tc]
                                    + img[th-1][tw+1][tc]
                                    + img[th+1][tw-1][tc]
                                    + img[th+1][tw+1][tc]
                                    ) / 9
    return blurred


def blur_image(image_in, image_out=None):
    img = image_in
    (H, W, C) = img.shape
    blurred = np.zeros(img.shape)
    img = np.pad(img, pad_width=1, mode='edge')
    img = img.astype(float)
    out = convolve(img, blurred, H, W, C)
    out = out.astype(np.uint8)
    if image_out is not None:
        cv2.imwrite(image_out, out)
    return out


def main():
    img = cv2.imread("beatles.jpg")
    blur_image(img, "beatles_blurred.jpg")


if __name__ == '__main__':
    main()
