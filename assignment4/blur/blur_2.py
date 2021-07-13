import cv2
import numpy as np

def blur_image(image_in, image_out=None):
    img = np.asarray(image_in)
    (height, width, channel) = img.shape
    img = img.astype("float")
    padded_img = np.pad(img, pad_width=1, mode='edge')
    padded_img = padded_img[:, :, 1:4]

    n = padded_img[:height, :width, :]
    s = padded_img[1:(height + 1), :width, :]
    e = padded_img[2:(height + 2), :width, :]
    w = padded_img[:height, 1:(width + 1), :]
    ne = padded_img[2:(height + 2), 1:(width + 1), :]
    se = padded_img[:height, 2:(width + 2), :]
    nw = padded_img[1:(height + 1), 2:(width + 2), :]
    sw = padded_img[2:(height + 2), 2:(width + 2), :]

    blurred = (img + n + s + e + w + ne + se + nw + sw) / 9
    blurred = blurred.astype(np.uint8)
    if image_out is not None:
        cv2.imwrite(image_out, blurred)
    return blurred

def main():
    img = cv2.imread("beatles.jpg")
    blur_image(img, "beatles_blurred.jpg")

if __name__ == '__main__':
    main()
