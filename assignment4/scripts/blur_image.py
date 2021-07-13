from blur import blur
import cv2

args = blur.handle_arguments()
img = cv2.imread(args.image_in)
blur.blur_image_script(img, args.image_out, args.mode)
