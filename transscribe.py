



# Transscribe

import openai
import os
from dotenv import load_dotenv

load_dotenv()

def transcribe_audio(audio_path, model="whisper-1"):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise EnvironmentError("OpenAI API key not found. Please set it in the .env file.")

    if not os.path.isfile(audio_path):
        raise FileNotFoundError(f"The audio file {audio_path} does not exist.")

    try:
        with open(audio_path, "rb") as audio_file:
            response = openai.Audio.transcribe(
                model=model,
                file=audio_file,
                language="en"
            )
        return response.get("text", "")
    except Exception as e:
        raise RuntimeError(f"Failed to transcribe audio: {e}")
