import pygame
import time

# While Playsound3 would have been less code, the speed at which it returned each dot and dash was not suitable for
# the project. I selected pygame's sound mixer instead.

# Initiate Sound
pygame.init()
pygame.mixer.init()


# Sound path, play function, and time delay are kept in functions to easily make changes to path or time should the
# code expand in the future.
def play_dot_sound():
    dot_sound = pygame.mixer.Sound('assets/sounds/dot.wav')
    dot_sound.play()
    time.sleep(.25)


def play_dash_sound():
    dash_sound = pygame.mixer.Sound('assets/sounds/dash.wav')
    dash_sound.play()
    time.sleep(.25)


# Alphabet dictionary holds key:value pairs for the text based letter, numbers, and symbols as keys along with their
# corresponding text based morse code signals as signals.
# The dictionary will allow for a for loop to run to find the appropriate signals.
alphabet = {"a": [".","-"], "b": ["-",".",".","."], "c": ["-",".","-","."],"d": ["-",".","."], "e": ["."],
            "f": [".",".","-","."], "g": ["-","-","."], "h": [".",".",".","."],"i": [".","."], "j": [".","-","-","-"],
            "k": ["-",".","-"], "l": [".","-",".","."], "m": ["-","-"], "n": ["-","."], "o": ["-","-","-"],
            "p": [".","-","-","."], "q": ["-","-",".","-"], "r": [".","-","."],"s": [".",".","."],"t": ["-"],
            "u": [".",".","-"],"v": [".",".",".","-"],"w": [".","-","-"],"x": ["-",".",".","-"],"y": ["-",".","-","-"],
            "z": ["-","-",".","."], "0": ["-","-","-","-","-"], "1": [".","-","-","-","-"], "2": [".",".","-","-","-"],
            "3": [".",".",".","-","-"], "4": [".",".",".",".","-"], "5": [".",".",".",".","."],
            "6": ["-",".",".",".","."], "7": ["-","-",".",".","."], "8": ["-","-","-",".","."],
            "9": ["-","-","-","-","."], " ": [" "], "?": [".",".","-","-",".","."], "!": ["-",".","-",".","-","-"],
            ".": [".","-",".","-",".","-"], ",": ["-","-",".",".","-","-"], ";": ["-",".","-",".","-","."],
            ":": ["-","-","-",".",".","."], "+": [".","-",".","-","."], "-": ["-",".",".",".",".","-"],
            "/": ["-",".",".","-","."], "*": ["-",".",",","-"], "=": ["-",".",".",".","-"], "(": ["-",".","-","-","."],
            ")": ["-",".","-","-",".","-"], "'": [".","-","-","-","-","."], "_": [".",".","-","-",".","-"],
            "@": [".","-","-",".","-","."], '"': [".","-",".",".","-","."]
}

morse_code = ""

# While loop created to give user another try and converting text to morse code should they enter a symbol that
# cannot be converted to morse code.
valid_input = True
while valid_input:
    word = input("What word or phrase do you need converted to morse code? ").lower()
    try:
        i = 0
        for letter in word:
            i += 1
            for signal in alphabet[letter]: # For loop to play audio of converted Morse Code before displaying text
                if signal == ".":
                    play_dot_sound()
                else:
                    play_dash_sound()
                morse_code += signal
            if i < len(word): # Ensures there is not an unnecessary space at the end of the conversion.
                time.sleep(.25)
                morse_code += " "
        valid_input = False
    except KeyError:
        print("\nMorse code has no signal for one or more of your inputted symbols. Please try again.\n")
        time.sleep(1.5)

pygame.quit()

print(f"The printed version of the morse code you heard was: {morse_code}")