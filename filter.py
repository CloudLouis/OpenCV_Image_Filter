import numpy as np
import cv2 as cv


def main(path):
    img = cv.imread(path)


    cv.imshow("Lul", img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.imwrite("image_result.png", img)


if __name__=="__main__":
    main("image_path_here")
