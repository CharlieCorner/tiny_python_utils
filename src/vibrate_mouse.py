#!/usr/bin/python3

import pyautogui
import sys
import time
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


def main():
    args = _parse_args()

    try:
        if args.timeout_time >= 1:
            for i in range(0, args.timeout_time):
                print("Remaining seconds: %i" % (args.timeout_time - i))
                vibrate_cursor(args)
        else:
            while True:
                vibrate_cursor(args)
    except KeyboardInterrupt:
        print("Exiting...!")


def vibrate_cursor(args):
    move_x = args.x_pixels
    move_y = args.y_pixels

    x, y = pyautogui.position()

    if x <= 30 or y <= 30:
        print("Exiting because cursor is at <= (30,30)...")
        raise sys.exit()

    # print("X: %i, Y: %i" % (x, y))
    pyautogui.moveTo(x + move_x, y + move_y, 0.25)
    time.sleep(0.1)
    pyautogui.moveTo(x, y, 0.25)
    pyautogui.click()
    time.sleep(0.4)


def _parse_args():
    """Parse args with argparse
    :returns: args
    """
    parser = ArgumentParser(description="Make the mouse cursor vibrate.",
                            formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument('-t',
                        default=-1,
                        dest="timeout_time",
                        type=int,
                        help="The amount of time in seconds before exiting. Any value less than 1 equals to infinity.")

    parser.add_argument('-x',
                        default=35,
                        dest="x_pixels",
                        type=int,
                        help="How many pixels along the X-Axis should the cursor move.")

    parser.add_argument('-y',
                        default=35,
                        dest="y_pixels",
                        type=float,
                        help="How many pixels along the X-Axis should the cursor move.")

    return parser.parse_args()


if __name__ == '__main__':
    main()
