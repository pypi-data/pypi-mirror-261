"""
shell_log_handler.py

A module to configure logging for shell scripts, including log rotation and
retention features.

This module allows specifying the log file path, the maximum number of days to
retain the logs, and the maximum log file size before rotation.
"""

import logging
import logging.handlers
from typing import NoReturn


def setup_logging(log_file_path: str, max_days: int, max_size_mb: int, verbose: bool = False) -> NoReturn:
    """
    Sets up logging with rotation and retention policies.

    Args:
        log_file_path (str): The path to the log file where logs will be written.
        max_days (int): The maximum number of days to retain the log files.
        max_size_mb (int): The maximum size of a log file in megabytes before it's rotated.
        verbose (bool, optional): If True, also logs to stdout. Defaults to False.

    Returns:
        NoReturn
    """
    # Convert max size in MB to bytes for the RotatingFileHandler
    max_size_bytes = max_size_mb * 1024 * 1024

    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Define log format
    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Setup file handler with rotation and retention
    file_handler = logging.handlers.TimedRotatingFileHandler(
        log_file_path, when='D', interval=1, backupCount=max_days, encoding='utf-8'
    )
    file_handler.setFormatter(log_format)
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    # If verbose, add stdout handler
    if verbose:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(log_format)
        logger.addHandler(stream_handler)


def log_info(message: str) -> NoReturn:
    """
    Logs an informational message.

    Args:
        message (str): The message to log.

    Returns:
        NoReturn
    """
    logging.info(message)


def log_error(message: str) -> NoReturn:
    """
    Logs an error message.

    Args:
        message (str): The message to log.

    Returns:
        NoReturn
    """
    logging.error(message)


