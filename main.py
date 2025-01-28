import logging
import tkinter as tk
from login import Login
from game import Game

# to fix gif non-persistant background
# magick input.gif -coalesce output.gif

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='escape_room.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S')


def main():
    login = Login()
    if not login.is_auth:
        logger.info("User Authentication Failure")
    else:
        game = Game()


if __name__ == "__main__":
    main()
