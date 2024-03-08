import curses
from curses import wrapper
import time
from model import load_text, get_highscore, save_highscore
from view import menu_screen, display_text, display_text2, start_screen, displayHighscoreMessage, quittingApp, \
    beatedHighscoreMessage, pressButtonMessage, congratulationsMessage

def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            return wpm

        try:
            key = stdscr.getkey()
        except:
            continue

        # ESC button
        if ord(key) == 27:
            break
        # BACKSPACE button
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

        stdscr.clear()
        stdscr.refresh()

def wpm_and_errors_test(stdscr):
    target_text = load_text()
    current_text = []
    errors = 0
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text2(stdscr, target_text, current_text, wpm, errors)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            return wpm

        try:
            key = stdscr.getkey()
        except:
            continue

        # ESC button
        if ord(key) == 27:
            break
        # BACKSPACE button
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
            else:
                errors += 1  # Zwiększ licznik błędów
        elif len(current_text) < len(target_text):
            if key != target_text[len(current_text)]:
                errors += 1  # Zwiększ licznik błędów
            current_text.append(key)

        stdscr.clear()
        stdscr.refresh()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        menu_screen(stdscr)
        key = stdscr.getkey()

        result = 0
        if key == "1":
            result = wpm_test(stdscr)
        elif key == "2":
            result = wpm_and_errors_test(stdscr)
        elif key == "3":
            displayHighscoreMessage(stdscr)
        elif ord(key) == 27:
            quittingApp(stdscr)

        previous = int(get_highscore())

        if key == "1" or key == "2":
            if result > previous:
                beatedHighscoreMessage(stdscr)
                curses.echo()
                player = stdscr.getstr(4, 0).decode('utf-8')
                curses.noecho()
                save_highscore(result, player)
                pressButtonMessage(stdscr)
            else:
                congratulationsMessage(stdscr)

        key = stdscr.getkey()

        if ord(key) == 27:
            break
wrapper(main)
