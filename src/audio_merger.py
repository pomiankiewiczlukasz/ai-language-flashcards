from pydub import AudioSegment
from config import PAUSE_MS


def merge_audio(german_file, polish_file, output_file):

    german_audio = AudioSegment.from_mp3(german_file)
    polish_audio = AudioSegment.from_mp3(polish_file)

    pause = AudioSegment.silent(duration=PAUSE_MS)

    final_audio = (
        german_audio
        + pause
        + polish_audio
        + pause
        + german_audio
        + pause
    )

    final_audio.export(output_file, format="mp3")