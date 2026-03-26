# ⌨️ Typing Speed Tester

A simple typing speed test app built with Python and CustomTkinter.

## Features
- 4 difficulty modes: Easy, Medium, Hard, and Punctuation
- Live WPM, accuracy, and timer stats
- Border turns green/red as you type
- Tab to skip to a new sentence

## Requirements
- Python 3.x
- CustomTkinter

Install the dependency with:
```
pip install customtkinter
```

## How to Run
Make sure `main.py` and `sentences.py` are in the same folder, then run:
```
python main.py
```
Or install the .exe given in the release folder

## How to Use
1. Select a difficulty using the buttons at the top
2. Start typing in the text box — the timer starts automatically
3. Finish the sentence to see your WPM and accuracy
4. Press **Tab** or click **New Test** for a new sentence
5. Click **Reset** to restart the current sentence

## Building an EXE
```
pip install pyinstaller
pyinstaller --onefile --windowed main.py --add-data "sentences.py;."
```
The `.exe` will be in the `dist/` folder.

## Project Structure
```
typing-speed-tester/
├── main.py         # App logic and UI
├── sentences.py    # Sentence lists by difficulty
└── README.md
```
