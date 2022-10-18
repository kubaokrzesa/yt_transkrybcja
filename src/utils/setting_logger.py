# -*- coding: utf-8 -*-
import logging


class Logger:
    def __init__(self, name: str) -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        c_handler = logging.StreamHandler()
        c_handler.setLevel(logging.INFO)
        c_format = logging.Formatter(
            "%(name)s -- %(filename)s -- %(levelname)s -- %(asctime)s -- %(message)s"
        )
        c_handler.setFormatter(c_format)
        self.logger.addHandler(c_handler)

    def get_logger(self) -> logging.Logger:
        return self.logger


def set_logger() -> logging.Logger:
    # logging.basicConfig(format='%(name)s - %(asctime)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S', level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.INFO)
    c_format = logging.Formatter(
        "%(name)s -- %(filename)s -- %(levelname)s -- %(asctime)s -- %(message)s"
    )
    c_handler.setFormatter(c_format)
    logger.addHandler(c_handler)
    return logger
