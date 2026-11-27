from pathlib import Path

import librosa
import numpy as np
import pretty_midi
from notes import Note, load_notes, save_notes

QUARTER = 0.25
MIN_DURATION = 0.05
MIN_VELOCITY = 20
MIDDLE_C = 60

MAJOR = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
MINOR = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])
NAMES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]

def filter_notes(notes): #returns cleaned list of notes
    cleaned = []#new array for cleaned notes

    notes = [n for n in notes if n.duration >= MIN_DURATION and n.velocity >= MIN_VELOCITY]#get rid of all notes that arent within plausible ranges of velocity and duration
    notes.sort(key=lambda n: (n.pitch, n.start))#sort 

    for n in notes:#iterate, get rid of duplicates and overlap
        if cleaned:
            prev = cleaned[-1]
        else:
            prev = None

        if prev and prev.pitch == n.pitch:#if the last and current note are the same
            if abs(n.start-prev.start) < 0.03:#if two of the same note started within 30 ms
                if n.velocity > prev.velocity:
                    cleaned[-1] = n
                continue
            if n.start < prev.start + prev.duration:#overlap
                prev.duration = n.start - prev.start#end the previos before the current starts
        cleaned.append(n)

    cleaned.sort(key = lambda n: (n.start,n.pitch))
    return cleaned