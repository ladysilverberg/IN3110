from blur import blur_faces
import cv2

img = cv2.imread("../beatles.jpg")
blur_faces.blur_faces(img, "beatles_blurred.jpg")
