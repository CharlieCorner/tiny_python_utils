import pyautogui
import time
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


def main():
    args = _parse_args()

    try:
        if args.timeout_time >= 1:
            for i in range(0, args.timeout_time):
                print("Second: %i" % i)
                vibrate_cursor()
        else:
            while True:
                vibrate_cursor()
    except KeyboardInterrupt:
        print("Exiting...!")


def vibrate_cursor():
    x, y = pyautogui.position()
    # print("X: %i, Y: %i" % (x, y))
    pyautogui.moveTo(x + 35, y + 35)
    time.sleep(0.10)
    pyautogui.moveTo(x, y)


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
    return parser.parse_args()


if __name__ == '__main__':
    main()
