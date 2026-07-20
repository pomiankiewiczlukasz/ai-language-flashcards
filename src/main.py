from excel_reader import load_sentences
from tts_generator import generate_audio
from audio_merger import merge_audio
from config import (
    INPUT_FILE,
    OUTPUT_DIR,
    GERMAN_VOICE,
    POLISH_VOICE,
)

from tqdm import tqdm

import asyncio
import os


df = load_sentences(INPUT_FILE)

# na razie testujemy tylko 3 zdania
# df = df.head(50)


async def main():

    for index, row in tqdm(df.iterrows(), total=len(df)):

        number = str(index + 1).zfill(4)

        output_folder = f"{OUTPUT_DIR}/{number}"

        os.makedirs(output_folder, exist_ok=True)

        german_file = f"{output_folder}/de.mp3"
        polish_file = f"{output_folder}/pl.mp3"
        final_file = f"{output_folder}/flashcard.mp3"

        if os.path.exists(final_file):
            print(f"{number} already exists - skipping")
            continue

        print(f"\nProcessing {number}")
        print(row["Deutsch"])
        print(row["Polski"])

        # Niemiecki
        await generate_audio(
            row["Deutsch"],
            german_file,
            GERMAN_VOICE,
        )

        # Polski
        await generate_audio(
            row["Polski"],
            polish_file,
            POLISH_VOICE,
        )

        # Połącz DE → PL → DE
        merge_audio(
            german_file,
            polish_file,
            final_file,
        )


asyncio.run(main())