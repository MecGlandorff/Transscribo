



# Transscribe

import os
import sys
from load_mp4 import extract_audio
from transcribe import transcribe_audio

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py path_to_video.mp4")
        sys.exit(1)

    mp4_path = sys.argv[1]

    if not os.path.isfile(mp4_path):
        print(f"Error: File {mp4_path} does not exist")
        sys.exit(1)

    audio_path = "extracted_audio.wav"

    try:
        extract_audio(mp4_path, audio_path)
        transcription = transcribe_audio(audio_path)
        print("\n--- Transcription ---\n")
        print(transcription)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if os.path.isfile(audio_path):
            os.remove(audio_path)

if __name__ == "__main__":
    main()
