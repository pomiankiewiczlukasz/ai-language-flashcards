import edge_tts


async def generate_audio(text, output_file, voice):

    communicate = edge_tts.Communicate(
        text,
        voice
    )

    await communicate.save(output_file)