import time
import random

from pynput.mouse import Controller, Button
import argparse

# type of point on display (x, y)
Point = tuple[int, int]


def get_place_to_click(start_place: Point, dispersion: int = 0) -> Point:
    """Get point to click by start point and dispertion

    Args:
        start_place (Point)
        dispersion (int, optional): in px. Defaults to 0.

    Returns:
        Point: result point
    """
    place_x = random.randint(
        start_place[0] - dispersion,
        start_place[0] + dispersion,
    )

    place_y = random.randint(
        start_place[1] - dispersion,
        start_place[1] + dispersion,
    )

    return place_x, place_y


def setup_argparser() -> argparse.ArgumentParser:
    """setup and return CL args parser"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-x",
        required=True,
        type=int,
        help="x of start mouse point",
    )
    parser.add_argument(
        "-y",
        required=True,
        type=int,
        help="y of start mouse point",
    )
    parser.add_argument(
        "--dispersion",
        "-d",
        type=int,
        default=0,
        help="Dispersion of mouse pinter to click",
    )
    parser.add_argument(
        "--time-sleep",
        "-ts",
        type=float,
        default=5.00,
        help="Time sleep between clicks (in seconds)",
    )
    return parser


def main():
    # get cli command args
    parser = setup_argparser()
    args = parser.parse_args()
    # args
    start_place: Point = (args.x, args.y)
    dispersion: int = args.dispersion
    time_sleep: float = args.time_sleep
    # mouse to click
    mouse = Controller()
    while time.sleep(time_sleep) is None:

        click_place = get_place_to_click(start_place=start_place, dispersion=dispersion)

        mouse.position = click_place
        mouse.click(button=Button.left)


if __name__ == "__main__":
    main()
