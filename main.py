import pyautogui as pt
import pyperclip
import pytesseract as tess
from PIL import Image, ImageEnhance
import cv2
import numpy as np

tess.pytesseract.tesseract_cmd = r'C:\Users\adame\AppData\Local\Tesseract-OCR\tesseract.exe'


# Helper functions
def nav_to_image(image, clicks, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=0.7)
    if position is None:
        print(f'{image} not found..')
        return 0
    else:
        pt.moveTo(position, duration=0.1)
        pt.moveRel(off_x, off_y, duration=0.1)
        pt.click(clicks=clicks, interval=0.3)


def grid(num: int) -> list[list[int]]:
    return [[col for col in range(num)] for row in range(num)]


def find_coords_X():
    pt.hotkey('f3', 'c')
    coords = pyperclip.paste().split()[6]
    return round(float(coords), 1)


def find_coords_Z():
    pt.hotkey('f3', 'c')
    coords = pyperclip.paste().split()[8]
    return round(float(coords), 1)


# Farming logic
temp = input("Enter the size of the square farm: ")
size = int(temp)

sleep(3)  # Wait for game to load
nav_to_image("resume/resume.png", 3)  # Click resume button to enter game

for row in range(size):
    # Scroll inventory to correct location
    pt.keyDown('x')
    pt.keyUp('x')
    pt.scroll(-1000)
    pt.keyDown('x')
    pt.keyUp('x')
    pt.scroll(-1000)
    pt.keyDown('x')
    pt.keyUp('x')
    pt.scroll(1000)
    pt.scroll(1000)

    # Move player to correct position on X-axis
    current_position = find_coords_X()
    position = find_coords_X() if row == 0 else position + 1
    if row % 2 == 0:
        while position > current_position:
            pt.keyDown('w')
            pt.keyUp('w')
            current_position = find_coords_X()
            if round(position - current_position, 1) <= 0.2:
                pt.keyDown('shift')
            sleep(0.05)
        pt.keyUp('shift')
    else:
        while position < current_position:
            pt.keyDown('s')
            pt.keyUp('s')
            current_position = find_coords_X()
            if round(current_position - position, 1) <= 0.2:
                pt.keyDown('shift')
            sleep(0.05)
        pt.keyUp('shift')

    # Plant crops
    pt.keyDown('e')  # Open inventory
    pt.keyUp('e')
    for i in range(size):
        for j in range(size):
            pt.click(x=958 + 23 * j, y=664 + 23 * i, clicks=1, interval=0.15)  # Click on each spot to plant crops
            sleep(0.05)
    pt.keyDown('esc')  # Close inventory
    pt.keyUp('esc')

    # Move player to next row and correct position on Z-axis
    position_z = find_coords_Z() - 1
    current_position_z = find_coords_Z()
    while position_z < current_position_z:
        pt.keyDown('shift')

