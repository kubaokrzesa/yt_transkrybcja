import os
from pathlib import Path

from pytube import YouTube
from pydub import AudioSegment

from utils.setting_logger import Logger

l = Logger(__name__)
logger = l.get_logger()

def run_yt_downloading(link, outputs_folder, remove_mp3_file):

    download_from_yt(link, outputs_folder)
    logger.info("Downloading succesful")

    mp4_path, mp3_path, wav_path = get_output_names(outputs_folder)

    logger.info("Renaming to mp3")
    change_mp4_to_mp3(mp4_path, mp3_path)
    logger.info("Changing mp3 to wav")
    change_mp3_to_wav(mp3_path, wav_path)

    if remove_mp3_file:
        logger.info("Deleting mp3 file")
        os.remove(mp3_path)
    return wav_path



def download_from_yt(link: str, outputs_folder):
    yt = YouTube(link)
    path = Path(os.getcwd()) / outputs_folder
    print(path)
    yt.streams.filter(only_audio=True)[0].download(path)


def get_output_names(outputs_folder):
    mp4_path = outputs_folder / list(filter(lambda x: x.endswith('.mp4'), os.listdir(outputs_folder)))[-1]
    base, ext = os.path.splitext(mp4_path)
    mp3_path = base + '.mp3'
    wav_path = base + '.wav'
    return mp4_path, mp3_path, wav_path


def change_mp4_to_mp3(mp4_path, mp3_path):
    os.rename(mp4_path, mp3_path)


def change_mp3_to_wav(mp3_path, wav_path):
    sound = AudioSegment.from_file(mp3_path)
    sound.export(wav_path, format="wav")
