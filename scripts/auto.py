import cv2
import ctypes
import numpy as np
import platform
import pynput
from time import sleep
from PIL import ImageGrab

mouse = pynput.mouse.Controller()

if platform.system().lower() == "windows":
    # Query DPI Awareness (Windows 10 and 8)
    awareness = ctypes.c_int()
    errorCode = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
    # Set DPI Awareness  (Windows 10 and 8)
    errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(2)
    # the argument is the awareness level, which can be 0, 1 or 2:
    # for 1-to-1 pixel control I seem to need it to be non-zero (I'm using level 2)
    # Set DPI Awareness  (Windows 7 and Vista)
    success = ctypes.windll.user32.SetProcessDPIAware()

def reduce(image, mult=0.5):
    h, w = image.shape[:2]
    return cv2.resize(image, (int(w * mult), int(h * mult)), interpolation=cv2.INTER_AREA)

def screen():
    prtscr = ImageGrab.grab()
    printscreen_numpy = np.array(prtscr, dtype='uint8')\
    .reshape((prtscr.size[1],prtscr.size[0],3))
    return printscreen_numpy

def match_all(image, template, threshold=0.8):
    """ Match all template occurrences which have a higher likelihood than the threshold """
    height, width = template.shape[:2]
    match_probability = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    match_locations = np.where(match_probability >= threshold)

    # Add the match rectangle to the screen
    rectangles = []
    for x, y in zip(*match_locations[::-1]):
        rectangles.append([int(x), int(y), int(width), int(height)])
    rectangles, _ = cv2.groupRectangles(rectangles, 1, 0.2)
    return rectangles

def match_best(image, template, threshold=0.8):
    height, width = template.shape[:2]
    match_probability = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    # return np.unravel_index(match_probability.argmax(), match_probability.shape)
    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match_probability)
    _, max_val, _, max_point = cv2.minMaxLoc(match_probability)
    if max_val < threshold:
        return None
    return *max_point, width, height

def screen_find(imagefile, threshold=0.8):
    img = cv2.imread(imagefile)
    if img is None:
        return None
    scrn = screen()
    return match_best(scrn, img, threshold)

def goto_rect(rect):
    if rect:
        x, y, w, h = rect
        mouse.move(-9999, -9999)
        sleep(0.1)
        mouse.move(int(x + w / 2), int(y + h / 2))
        # mouse.move(int(x + w / 2), int(y + h / 2))

def click_image(imagefile, threshold=0.8, delay=0.1):
    rect = screen_find(imagefile, threshold)
    if not rect:
        return False
    goto_rect(rect)
    sleep(0.1)
    mouse.press(pynput.mouse.Button.left)
    sleep(delay)
    mouse.release(pynput.mouse.Button.left)
    return True

def main():
    pass
    # img = cv2.imread("D:/src/Screenshot 2021-11-02 230428.png")
    # scrn = screen()
    # print(match_all(scrn, img))
    # rect = screen_find("D:/src/Screenshot.png")
    # goto_rect(rect)
    # cv2.rectangle(scrn, best, (best[0] + webaccept.shape[1], best[1] + webaccept.shape[0]), (0,255,255), 2)
    # cv2.imshow('resize', reduce(scrn))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
