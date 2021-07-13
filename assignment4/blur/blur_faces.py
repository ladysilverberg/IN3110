import cv2
import numpy as np
import os
from . import blur_2 as numpy_blur

def blur_faces(image_in, image_out=None):
    assert image_in is not None, "Value of image_in is None. Image probably failed to read."
    try:
        img = np.array(image_in)
    except ValueError:
        raise ValueError("Recieved image_in not of array-like type.")

    current_path = os.path.dirname(os.path.abspath(__file__))
    classifier_path = os.path.join(current_path, "haarcascade_frontalface_default.xml")
    assert os.path.exists(classifier_path), f"There is no file named \'{classifier_path}\'."

    face_cascade = cv2.CascadeClassifier(classifier_path)
    faces = face_cascade.detectMultiScale(
            img,
            scaleFactor=1.025,
            minNeighbors=5,
            minSize=(30, 30))
    for (x, y, w, h) in faces:
        subimg = img[y:h+y, x:w+x, :]
        blurred_face = numpy_blur.blur_image(subimg)
        for num_sweeps in range(10):
            blurred_face = numpy_blur.blur_image(blurred_face)
        img[y:h+y, x:w+x, :] = blurred_face[:, :, :]
    img = img.astype("uint8")
    if image_out is not None:
        cv2.imwrite(image_out, img)
    return img

def main():
    img = cv2.imread("beatles.jpg")
    blur_faces(img, "beatles_blurred.jpg")

if __name__ == '__main__':
    main()
