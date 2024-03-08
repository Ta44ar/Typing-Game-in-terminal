from curses import wrapper
from controller import main as controller_main

def main(stdscr):
    controller_main(stdscr)

if __name__ == "__main__":
    wrapper(main)
