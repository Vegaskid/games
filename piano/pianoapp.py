# pianoapp.py
# v0.9
#
# This is a rough first version of a random chord generator to help pianists learn different chords in differen inversions
# This version only has the 5 primary 7th chords types (major, dominant, minor, half-diminished, and diminished)
# Project came about to learn Tkinter
# This file can be run with the standard library on most systems with Python 3.6+ installed

import random
from tkinter import *
from tkinter import ttk
window = Tk()

KEYS = ["Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G"]
RESET = False

def update_chord():
    # Runs when the Start button is pressed
    global RESET
    if RESET == True:
        RESET = False
        return
    btn.configure(text="Stop", command=stop)
    delay = int(refresh.get()) * 1000
    chord_types = []
    if 'selected' in C1.state():
        chord_types.append('maj7')
    if 'selected' in C2.state():
        chord_types.append('7')
    if 'selected' in C3.state():
        chord_types.append('m7')
    if 'selected' in C4.state():
        chord_types.append('ø7')
    if 'selected' in C5.state():
        chord_types.append('°7')
    inversions = []
    if 'selected' in C6.state():
        inversions.append('Root position')
    if 'selected' in C7.state():
        inversions.append('1st inversion')
    if 'selected' in C8.state():
        inversions.append('2nd inversion')
    if 'selected' in C9.state():
        inversions.append('3rd inversion')
    key = random.choice(KEYS)
    chord_type = random.choice(chord_types)
    inversion = random.choice(inversions)
    print(key+chord_type, inversion)
    chord_lbl.configure(text=key + chord_type)
    inversion_lbl.configure(text=inversion)
    inversion_lbl.after(delay, update_chord)

def stop():
    # Runs when the Stop button is pressed
    global RESET
    btn.configure(text="Start", command=update_chord)
    RESET = True

# Adds various components to the GUI. It isn't pretty!

panedwindow = ttk.PanedWindow(window, orient=HORIZONTAL)
panedwindow.pack(fill = BOTH, expand = True)

frame1 = ttk.Frame(panedwindow, width = 100, height = 600, relief = SUNKEN)
frame2 = ttk.Frame(panedwindow, width = 700, height = 600, relief = SUNKEN)
frame1.config(padding = (30, 15))
frame2.config(padding = (30, 15))
panedwindow.add(frame1, weight = 1)
panedwindow.add(frame2, weight = 7)

btn = ttk.Button(frame1, text="Start", command=update_chord)
btn.pack()

n = StringVar()
refresh = ttk.Combobox(frame1, width=27, textvariable=n)
refresh['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20)
# Default refresh time is 10 seconds (at position 9)
refresh.current(9)
refresh.pack()

refresh_lbl = Label(frame1, text="Refresh in secs (1-10)",
                    fg='blue', font=("Arial", 10))
refresh_lbl.pack()
chord_lbl = Label(frame2, fg='blue', font=("Arial", 200))
chord_lbl.pack()
inversion_lbl = Label(frame2, fg='green', font=("Arial", 60))
inversion_lbl.pack()

C1 = ttk.Checkbutton(frame1, text="Major 7ths")
C2 = ttk.Checkbutton(frame1, text="Dominant 7ths")
C3 = ttk.Checkbutton(frame1, text="Minor 7ths")
C4 = ttk.Checkbutton(frame1, text="Half-Diminished 7ths")
C5 = ttk.Checkbutton(frame1, text="Diminished 7ths")
C1.state(['!alternate'])
C2.state(['!alternate'])
C3.state(['!alternate'])
C4.state(['!alternate'])
C5.state(['!alternate'])
C1.state(['selected'])
C2.state(['selected'])
C3.state(['selected'])
C4.state(['selected'])
C5.state(['selected'])
C1.pack()
C2.pack()
C3.pack()
C4.pack()
C5.pack()

C6 = ttk.Checkbutton(frame1, text="Root position")
C7 = ttk.Checkbutton(frame1, text="1st inversion")
C8 = ttk.Checkbutton(frame1, text="2nd inversion")
C9 = ttk.Checkbutton(frame1, text="3rd inversion")
C6.state(['!alternate'])
C7.state(['!alternate'])
C8.state(['!alternate'])
C9.state(['!alternate'])
C6.state(['selected'])
C7.state(['selected'])
C8.state(['selected'])
C9.state(['selected'])
C6.pack()
C7.pack()
C8.pack()
C9.pack()

window.title('Piano Toolkit')
window.geometry("800x600+10+20")
window.state("zoomed")
window.mainloop()