import logging
from logging.handlers import RotatingFileHandler
import os
from dotenv import load_dotenv


def setup_logging():
    # Load environment variables from .env file
    load_dotenv()

    # Get the logging level from environment variable or default to INFO
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    log_file = os.getenv("LOG_FILE", "log/app.log")

    # Create a custom logging format
    log_format = "%(asctime)s - %(levelname)s - %(message)s"

    # Set up rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=5)
    handler.setFormatter(logging.Formatter(log_format))

    # Configure the logging settings
    logging.basicConfig(
        level=log_level,
        format=log_format,
        handlers=[
            handler,
            logging.StreamHandler()  # Also log to console
        ]
    )

    logging.info("11Logging is set up. Log level: %s", log_level)