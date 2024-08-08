import pygame
import time

# While Playsound3 would have been less code, the speed at which it returned each dot and dash was not suitable for
# the project. I selected pygame's sound mixer instead.

# Initiate Sound
pygame.init()
pygame.mixer.init()


# Sound path, play function, and time delay are kept in functions to easily make changes to path or time should the
# code expand in the future.

# Learned that the print function has an end parameter that is by default set to \n for a new line.
# I updated this end parameter so the morse code would print on the same line as its played.
def play_dot_sound():
    dot_sound = pygame.mixer.Sound('assets/sounds/dot.wav')
    dot_sound.play()
    print(".", end='')
    time.sleep(.25)


def play_dash_sound():
    dash_sound = pygame.mixer.Sound('assets/sounds/dash.wav')
    dash_sound.play()
    print("_", end='')
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
converter_on = True
while converter_on:
    word = input("What word or phrase do you need converted to morse code? ").lower()
    print("\nHere is your morse code:")
    time.sleep(.5)
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
            print(" ", end='')
            if i < len(word): # Ensures there is not an unnecessary space at the end of the conversion.
                time.sleep(.25)
                morse_code += " "

    except KeyError:
        print("\nMorse code has no signal for one or more of your inputted symbols. Please try again.\n")
        time.sleep(1.5)

    convert_again = input("\n\nWould you like to convert another word or phrase? Type Yes or No: ").lower()
    print("")
    if convert_again == "no":
        converter_on = False

pygame.quit()