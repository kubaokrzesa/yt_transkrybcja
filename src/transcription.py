import os
import speech_recognition as sr
from pathlib import Path

from utils.setting_logger import Logger

l = Logger(__name__)
logger = l.get_logger()

def transcribe_wav_file(wav_path, language, remove_wav_file):
    audio_file = sr.AudioFile(wav_path)

    recognizer = sr.Recognizer()
    with audio_file as source:
        audio_data = recognizer.record(source)

    # Transcribe AudioData to text
    text = recognizer.recognize_google(audio_data, language=language)

    if remove_wav_file:
        logger.info("Removing wav file")
        os.remove(wav_path)

    otp_path = os.path.basename(os.path.normpath(wav_path))
    otp_path, _ = os.path.splitext(otp_path)

    logger.info("Saving transcript")
    with open(f'transcriptions/{otp_path}.txt', 'w') as f:
        f.write(text)

    print(text)