import logging


class Logger:
    def __init__(self):
        logging.basicConfig(
            filename="game_log.log",
            force=True,
            format="%(asctime)s -- [%(levelname)s] :: %(message)s",
        )
        self.logger = logging.getLogger()

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
