# AI Language Flashcards Generator 🇩🇪🇵🇱

Python application that automatically creates audio flashcards from German language learning materials.

The project takes sentences and translations from an Excel file, generates AI speech using Microsoft Edge Text-to-Speech, and creates ready-to-use MP3 flashcards for language learning.

## Project idea

The goal was to automate the creation of language learning materials.

Instead of manually recording thousands of sentences, the application:

1. Reads German sentences and Polish translations from Excel.
2. Generates German and Polish audio using AI voices.
3. Adds pauses between parts.
4. Combines recordings into individual flashcards.
5. Creates complete audio learning material automatically.

Example:

```
German sentence
        ↓
pause
        ↓
Polish translation
        ↓
pause
        ↓
German sentence again
```

## Features (MVP)

✅ Read sentences from Excel file
✅ Generate German AI voice
✅ Generate Polish AI voice
✅ Create individual MP3 flashcards
✅ Generate complete audio learning material
✅ Process hundreds/thousands of sentences automatically
✅ Skip already generated files
✅ Configurable voices and settings

## Technologies

* Python 3.12
* pandas
* openpyxl
* edge-tts
* pydub
* ffmpeg

## Project structure

```
ai-language-flashcards/

│
├── data/
│   └── test_sentences.xlsx
│
├── output/
│   └── generated flashcards
│
├── src/
│   ├── main.py
│   ├── excel_reader.py
│   ├── tts_generator.py
│   ├── audio_merger.py
│   └── config.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## How it works

### 1. Input data

The application reads sentences from an Excel file.

Required columns:

| Deutsch          | Polski        |
| ---------------- | ------------- |
| Guten Morgen.    | Dzień dobry.  |
| Wie geht es dir? | Jak się masz? |

Example:

```
data/test_sentences.xlsx
```

### 2. Configuration

Project settings are stored in:

```
src/config.py
```

Example:

```python
INPUT_FILE = "data/test_sentences.xlsx"

OUTPUT_DIR = "output"

GERMAN_VOICE = "de-DE-KatjaNeural"

POLISH_VOICE = "pl-PL-ZofiaNeural"

PAUSE_MS = 1500
```

This allows changing voices, input files, output folders, and pause duration without modifying the main application logic.

### 3. Audio generation

For every sentence pair the application creates:

```
output/
 └── 0001/
     ├── de.mp3
     ├── pl.mp3
     └── flashcard.mp3
```

Final flashcard format:

```
German sentence
↓
pause
↓
Polish translation
↓
pause
↓
German sentence
```

## Installation

Clone the repository:

```bash
git clone <repository-url>

cd ai-language-flashcards
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

Windows PowerShell:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Make sure FFmpeg is installed:

```bash
ffmpeg -version
```

## Run

Start generation:

```bash
python src/main.py
```

Generated files will appear in:

```
output/
```

## Example result

Example generated flashcard:

```
0001/
 ├── de.mp3
 ├── pl.mp3
 └── flashcard.mp3
```

The application can generate thousands of flashcards automatically.

## Current status

Version: **MVP 1.0**

The application successfully generated:

* 1832 German language flashcards
* AI-generated German and Polish audio files
* Ready-to-use language learning materials
* Complete automated audio learning content

## Future improvements

Possible next steps:

* command line arguments
* logging system
* better error handling
* metadata generation (level, topic, keywords)
* automated tests
* GitHub Actions CI pipeline
* Docker support

## Author

Created as a personal AI automation project to explore:

* Python development
* AI-based content generation
* automation pipelines
* practical AI engineering workflows


