import time
from pygame import mixer

def play_warningsound():
	mixer.init()
	if mixer.music.get_busy == False:
		mixer.music.load("WarningSound.mp3")
		mixer.music.play()
	else: time.sleep(0.2)

def main_delay():
    while True:
        play_warningsound()
        time.sleep(1)


if __name__ == "__main__":
    main_delay()