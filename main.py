from venv import logger
from app import App


if __name__ == '__main__':
    logger.info('info message')

    app = App()
    app.start()