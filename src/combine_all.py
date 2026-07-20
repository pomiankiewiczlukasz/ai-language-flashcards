from pydub import AudioSegment
from tqdm import tqdm
import os
from config import TOTAL_FLASHCARDS

combined = AudioSegment.empty()

for i in tqdm(range(1, TOTAL_FLASHCARDS + 1)):

    number = str(i).zfill(4)

    file = f"output/{number}/flashcard.mp3"

    if os.path.exists(file):
        combined += AudioSegment.from_mp3(file)

output = "examples/demo_flashcards.mp3"

combined.export(output, format="mp3")

print("Done!")