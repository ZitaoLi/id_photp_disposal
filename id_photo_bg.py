import cv2
import numpy as np

RED_BG = 1
BULE_BG = 2
WHITE_BG = 3

# 背景HSV范围
lower_blue = np.array([78, 43, 46])
upper_blue = np.array([110, 255, 255])

lower_red = np.array([156, 43, 46])
upper_red = np.array([180, 255, 255])

lower_white = np.array([0, 0, 221])
upper_white = np.array([180, 30, 255])


def read_img(path):
    img = cv2.imread(path)
    cv2.imshow('img', img)
    return img


def erode_dilate(mask):
    erode = cv2.erode(mask, None, iterations=3)
    cv2.imshow('erode', erode)
    dilate = cv2.dilate(erode, None, iterations=4)
    cv2.imshow('dilate', dilate)
    return dilate


def replace_pixel(img, profile, color):
    RED = (0, 0, 255)
    BULE = (255, 0, 0)
    WHITE = (255, 255, 255)
    rows, cols, channels = img.shape

    for i in range(rows):
        for j in range(cols):
            if profile[i, j] == 255:
                if color == RED_BG:
                    img[i, j] = RED
                elif color == BULE_BG:
                    img[i, j] = BULE
                elif color == WHITE_BG:
                    img[i, j] = WHITE

    cv2.imshow('res', img)


def change_bg(img, bg_from, bg_to):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    if bg_from == RED_BG:
        mask = cv2.inRange(hsv, lower_red, upper_red)
    elif bg_from == BULE_BG:
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
    elif bg_from == WHITE_BG:
        mask = cv2.inRange(hsv, lower_white, upper_white)

    profile = erode_dilate(mask)
    replace_pixel(img, profile, bg_to)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
