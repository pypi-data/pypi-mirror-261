import logging
import contextvars
from logging.handlers import TimedRotatingFileHandler

from .singleton import singleton
from .handler import SocketIOHandler
from .utils import setup_logging

context = contextvars.ContextVar('context', default="logngo")


class CustomFormatter(logging.Formatter):
    def format(self, record):
        record.request_id = context.get()
        return super().format(record)


@singleton
class Logger:
    def __init__(self):
        self.logger = logging.getLogger("logngo")
        self.logger.setLevel(logging.DEBUG)
        self.formatter = CustomFormatter(
            '[%(levelname)s] - %(asctime)s - %(message)s *** %(request_id)s - %(filename)s - %(name)s *** '
        )
        self.file_handler = None
        self.socket_handler = None
        self.stream_handler = None

    def setup(self, name: str, formatter: str = None, level: int = logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.level = level
        if formatter:
            self.formatter = CustomFormatter(f"%(request_id)s - {formatter}")

    def setup_file_handler(self, file_path: str, when: str, interval: int):
        if self.file_handler:
            raise Exception("logngo: File handler existed")
        setup_logging(file_path)
        self.file_handler = TimedRotatingFileHandler(filename=file_path, when=when, interval=interval)
        self.file_handler.setLevel(self.level)
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)
        print("logngo: Add file handler")

    def setup_socket_handler(self, url: str, handshake_path: str, channel: str):
        if self.socket_handler:
            raise Exception("logngo: Socket handler existed")
        self.socket_handler = SocketIOHandler(url, handshake_path, channel)
        self.socket_handler.setLevel(self.level)
        self.socket_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.socket_handler)
        print("logngo: Add socket handler")

    def setup_stream_handler(self):
        if self.stream_handler:
            raise Exception("logngo: Stream handler existed")
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setLevel(self.level)
        self.stream_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.stream_handler)
        print("logngo: Add stream handler")
