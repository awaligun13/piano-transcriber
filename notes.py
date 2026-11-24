from dataclasses import dataclass, asdict
import json
from typing import Optional

@dataclass
class Note:
    pitch: int #midi note number. 60 = middle c
    start: float #when will the note start
    length: float #how long will a not last
    velocity: int #midi 0-127, volume
    hand: Optional[str] = None #"L" or "R"

def save_notes(notes, path, meta = None):
    data = {"meta": meta or {}, "notes": [asdict(n) for n in notes]}
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def load_notes(path):
    with open(path) as f:
        data = json.load(f)
    return [Note(**n) for n in data["notes"]], data.get("meta", {})