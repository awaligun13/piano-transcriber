#Note this will only work with piano audio!

from pathlib import Path
from piano_transcription_inference import PianoTranscription, sample_rate, load_audio
from notes import Note, save_notes

def transcribe(audio_path: str, out_dir: str = "output", device: str = "cpu"):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    stem = Path(audio_path).stem

    audio, _ = load_audio(audio_path, sr=sample_rate, mono=True)
    transcriptor = PianoTranscription(device=device, checkpoint_path=None)

    midi_path = out / f"{stem}.raw.mid"
    result = transcriptor.transcribe(audio, str(midi_path))

    notes =[ Note(
        pitch = int(e["midi_note"]),
        start=float(e["onset_time"]),
        length=float(e["offset_time"] - e["onset_time"]),
        velocity = int(e["velocity"]),
    )for e in result["est_note_events"]
    ]
    notes.sort(key = lambda n: (n.start, n.pitch))

    pedal = [
        {"start": float(p["onset_time"]), "end": float(p["offset_time"])}
        for p in result["est_pedal_events"]
    ]

    json_path = out / f"{stem}.raw.json"
    save_notes(notes, json_path, meta = {"audio": audio_path, "pedal": pedal})
    print(f"{len(notes)} notes, {len(pedal)} pedal events")
    print(f"Wrote {midi_path} and {json_path}")
    return json_path
