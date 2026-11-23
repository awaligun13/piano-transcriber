# Piano Sheet Music Transcriber

Upload a recording of solo piano and get playable sheet music at a chosen
difficulty, plus key and chord analysis.

## Pipeline

1. Transcribe: piano audio to note events
2. Clean up and analyze: quantize rhythm, assign hands, detect key
3. Reduce: simplify to a chosen difficulty
4. Render: export MusicXML and display the score

## Setup

    python -m venv .venv
    source .venv/bin/activate    # Windows: .venv\Scripts\Activate.ps1
    pip install -r requirements.txt

## Usage

    python transcribe.py audio/mysong.wav
    python cleanup.py output/mysong.raw.json

## Status

- [ ] Stage 1: transcription
- [ ] Stage 2: cleanup and analysis
- [ ] Stage 3: difficulty reducer
- [ ] Stage 4: rendering