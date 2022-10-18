import yaml
from box import Box
from pathlib import Path

from yt_download import run_yt_downloading
from transcription import transcribe_wav_file
from utils.setting_logger import Logger

l = Logger(__name__)
logger = l.get_logger()

with open(r"config.yml") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)
    logger.info(config)
    config = Box(config)

yt_output_catalog = Path(config.yt_output_catalog)

def main():
    logger.info("running yt downloading")
    wav_path = run_yt_downloading(config.link, yt_output_catalog, config.remove_mp3_file)
    logger.info("Transcribing sound file")
    transcribe_wav_file(wav_path, config.language, config.remove_wav_file)

if __name__ == "__main__":
    main()