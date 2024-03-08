import curses
import time

from model import save_highscore, get_highscore

def start_screen(stdscr):
    stdscr.clear()
    curses.curs_set(0)  # Ukryj kursor
    stdscr.refresh()

    # Pobierz rozmiary terminala
    height, width = stdscr.getmaxyx()

    title = "Super Mega Impressive Typing Game Deluxe!"

    x = width // 2 - len(title) // 2
    y = height // 2

    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    title_color = curses.color_pair(4)

    colors = [curses.COLOR_RED, curses.COLOR_GREEN, curses.COLOR_YELLOW, curses.COLOR_BLUE, curses.COLOR_MAGENTA]

    for _ in range(1):
        for color in colors:
            stdscr.attron(curses.A_BOLD)  
            stdscr.addstr(y, x, title, curses.color_pair(color))
            stdscr.attroff(curses.A_BOLD) 
            stdscr.refresh()
            time.sleep(0.2)
            stdscr.clear()
            stdscr.refresh()
            time.sleep(0.1)

    stdscr.addstr(y, x, title, title_color)
    stdscr.refresh()

    stdscr.getch() 
    curses.curs_set(1)  

def menu_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "How fast you think you can type? Select difficulty level:")
    stdscr.addstr(1, 0, "1 - Fast and Furious!  (easy mode - typing speed only)")
    stdscr.addstr(2, 0, "2 - Watch your steps!  (hard mode - typing speed + errors counter)")
    stdscr.addstr(3, 0, "3 - Current highscore")
    stdscr.addstr(4, 0, "ESC - Quit")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")
    stdscr.addstr(2, 0, f"ESC - back")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)

def display_text2(stdscr, target, current, wpm=0, errors=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}   Errors: {errors}")
    stdscr.addstr(2, 0, f"ESC - back")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
            errors += 1

        stdscr.addstr(0, i, char, color)
        
def beatedHighscoreMessage(stdscr):
    stdscr.addstr(2, 0, f"Congratulations! You've beat the highscore!")
    stdscr.addstr(3, 0, "Enter your nickname: ")

def displayHighscoreMessage(stdscr):
    stdscr.clear()
    try:
        highscore = get_highscore()
        stdscr.addstr(1, 0, f"Current highscore is {highscore} WPM."
                            f"\nENTER - back to menu")
    except FileNotFoundError as e:
        stdscr.addstr(1, 0, f"Highscore file not found. {str(e)}")
    except Exception as e:
        stdscr.addstr(1, 0, f"Error while getting highscore. {str(e)}")
    stdscr.refresh()
    stdscr.getkey()

def quittingApp(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 0, "Closing the application...")
    stdscr.refresh()
    time.sleep(1)
    raise SystemExit(0)

def congratulationsMessage(stdscr):
    stdscr.addstr(2, 0, f"Congratulations! You succesfully finished this one! \n Press any button to continue...")

def pressButtonMessage(stdscr):
    stdscr.addstr(5, 0, f"Press any button to continue...")