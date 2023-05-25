"""
This is a python program written by Rushil Shah and Ben Clarke on 3/29/22
This program will big alt coins fast. Very Fast

The code takes in the input CSV_FILENAME as CSV_FILE (a below variable) which should follow the following standards
each line of the csv should be a 3 input (lets delineate for now as x, y, z)
x, y represent the data and z represents the function

The functions available are obvious - who needs documentation anyways
"""

import pyautogui
import keyboard
from csv import reader
from time import sleep


CSV_FILENAME = "buyBot.csv"  # the input file that will execute the actions of the csv
TIME_DELAY = 0.15  # the delay between each action specified by the csv
SAFETY = True  # toggles the warning before the program runs
CONFIDENCE = 0.65
REGION = (0, 0, 1005, 599)


def next_row(filename):
    """a generator function that returns the next row of a csv file"""
    with open(filename, 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            yield row


def main():
    if SAFETY:
        result = pyautogui.confirm("This will start the program")
        if result != "OK":
            raise ConnectionAbortedError

    for task, *args in next_row(CSV_FILENAME):
        if task == "move":
            pyautogui.moveTo(int(args[0]), int(args[1]))
        elif task == "drag":
            pyautogui.moveRel(int(args[0]), int(args[1]))
            pyautogui.click()
        elif task == "click":
            pyautogui.moveTo(int(args[0]), int(args[1]))
            pyautogui.click()
        elif task == "scroll":
            pyautogui.scroll(int(args[0]))  # x represents the amount of clicks that will be scrolled
            sleep(0.2)
        elif task == "delay":
            sleep(float(args[0]))
        elif task == "find":
            # returns the x,y pixels of the center of the image file
            result = pyautogui.locateCenterOnScreen(args[0], confidence=CONFIDENCE, region=REGION)
            if result is None:
                result = pyautogui.locateCenterOnScreen(args[0], confidence=CONFIDENCE, region=REGION)
                if result is None:
                    raise ValueError("Unable to find " + args[0] + " on screen")
            pyautogui.moveTo(*result)
            pyautogui.click()
        else:
            pass

        sleep(TIME_DELAY)


if __name__ == '__main__':
    main()
