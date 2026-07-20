from pydub import AudioSegment
from tqdm import tqdm
import os

combined = AudioSegment.empty()

for i in tqdm(range(1, 1833)):

    number = str(i).zfill(4)

    file = f"output/{number}/flashcard.mp3"

    if os.path.exists(file):
        combined += AudioSegment.from_mp3(file)

output = "output/flashcards_complete.mp3"

combined.export(output, format="mp3")

print("Done!")