# Morse Code Audio Converter

This Python project converts text into Morse code and plays audio for each dot and dash using `pygame`.
The program prints Morse code in real time as it plays and supports letters, numbers, spaces, and multiple punctuation symbols.
It is designed to be simple, readable, and easy to extend.

---

## Features

- Converts entire words and phrases to Morse code
- Plays sounds for dots (.) and dashes (-)
- Prints Morse code as audio plays
- Supports letters A–Z, digits 0–9, spaces, and punctuation
- Allows users to convert multiple phrases in one session
- Uses simple, maintainable Python functions
- Fully customizable timing, sound files, and character mappings

---

## Requirements

- Python 3.8 or higher
- pygame library

Install pygame:

    pip install pygame

---

## Installation

1. Clone or download the repository:

        git clone https://github.com/your-username/your-repo-name.git
        cd your-repo-name

2. Ensure the following sound files exist:

        assets/sounds/dot.wav
        assets/sounds/dash.wav

3. Verify your project folder matches the structure below.

---

## Project Structure

        project-folder/
        │
        ├── assets/
        │   └── sounds/
        │       ├── dot.wav
        │       └── dash.wav
        │
        ├── morse_converter.py
        └── README.md

---

## How to Run

Run the script directly from the terminal:

        python morse_converter.py

Then:

1. Enter a word or phrase
2. Each character is converted to Morse
3. Dots and dashes play as audio
4. Morse code prints on a single line
5. You can convert again or exit

---

## Example Output

        What word or phrase do you need converted to morse code? hello

        Here is your morse code:
        .... . .-.. .-.. ---

The audio plays as each dot (.) and dash (-) prints.

---

## Code Overview

Dot sound function:

        def play_dot_sound():
            dot_sound = pygame.mixer.Sound('assets/sounds/dot.wav')
            dot_sound.play()
            print(".", end='')
            time.sleep(.25)

Dash sound function:

        def play_dash_sound():
            dash_sound = pygame.mixer.Sound('assets/sounds/dash.wav')
            dash_sound.play()
            print("_", end='')
            time.sleep(.25)

Character mapping is handled through a dictionary linking letters, digits, and punctuation to Morse code signals.
The main loop manages input, printing, sound playback, and error handling.

---

## Potential Future Improvements

- Adjustable playback speed (WPM)
- GUI application
- Export Morse code to audio file
- Reverse decoding (Morse → text)
- Additional supported symbols
- LED/blink mode for visual Morse output

---

## License

This project is open source and available under the MIT License.
