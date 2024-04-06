from __future__ import annotations
from deepattern.patterns.singleton.singleton_meta import SingletonMeta
import logging


class LoggerSingleton(metaclass=SingletonMeta):

    def start_logger(self, output_path: str = None, verbose: bool = True) -> LoggerSingleton:
        logging.basicConfig(level=logging.INFO, 
                            filename=output_path, 
                            format="%(asctime)s - %(levelname)s - %(message)s")
        self.verbose = verbose
        return self

    def info(self, text: str):
        if self.__getattribute__("verbose"):
            logging.info(text)

    def warning(self, text: str):
        if self.__getattribute__("verbose"):
            logging.warning(text)

    def error(self, text: str):
        if self.__getattribute__("verbose"):
            logging.error(text)
