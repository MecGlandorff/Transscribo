



# Load MP4

import os
from moviepy.editor import VideoFileClip

def extract_audio(mp4_path, audio_output_path):
    if not os.path.isfile(mp4_path):
        raise FileNotFoundError(f"The file {mp4_path} does not exist")

    try:
        video = VideoFileClip(mp4_path)
        audio = video.audio
        if audio is None:
            raise ValueError("no audio track found in the MP4 file")
        audio.write_audiofile(audio_output_path, codec='pcm_s16le')
        audio.close()
        video.close()
        print(f"Audio extracted and saved to {audio_output_path}")
    except Exception as e:
        raise RuntimeError(f"Failed to extract audio: {e}")
