import pyautogui
from pathlib import Path


def find_image_on_screen(img: Path, confidence: float):
    """
    Given an image file the code will find the first instance of that image and its pixel coordinates in the
    center of that image if it is found on screen. if the image is not found on the screen then it will return None.

    :param img: (Path) the path location of the image file that will be compared to the screen
    :param confidence: how closely the image object must be to validate the image on screen (0.8 is average)
    :return: returns a Point object with the pixel coordinates of the image on the screen
    """
    result = pyautogui.locateCenterOnScreen(f"{img.resolve()}", confidence=confidence)
    return result


def main():
    point = find_image_on_screen(Path("./test.png"), confidence=0.8)
    print(point)


if __name__ == '__main__':
    main()
