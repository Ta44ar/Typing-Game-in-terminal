import logging
import random

TEXT_FILE = "text.txt"
HIGHSCORE_FILE = "highscore.txt"

def load_text():
    try:
        with open(TEXT_FILE, "r") as f:
            lines = f.readlines()
            return random.choice(lines).strip()
    except FileNotFoundError:
        logging.error(f"File not found: {TEXT_FILE}")
        return None
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None

def get_highscore():
    try:
        with open(HIGHSCORE_FILE, 'r') as file:
            content = file.read().strip()
            highscore_str, _ = content.split(':')
            highscore = int(highscore_str)
            return highscore
    except FileNotFoundError:
        logging.error(f"File not found: {HIGHSCORE_FILE}")
        return None
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None

def save_highscore(score, nickname):
    try:
        with open(HIGHSCORE_FILE, 'w') as file:
            file.write(f"{score}:{nickname}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
