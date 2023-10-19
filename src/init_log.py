import logging
from pathlib import Path

LOG_DIR = 'log'

def get_log_dir():
    log_dir = Path(LOG_DIR)
    if not log_dir.exists() or not log_dir.is_dir():
        log_dir.mkdir()
    return log_dir


def get_logger(name_log):
    logger = logging.getLogger(name_log)

    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")

    handler_stresm = logging.StreamHandler()
    handler_stresm.setFormatter(formatter)
    handler_stresm.setLevel(logging.WARNING)

    handler_file = logging.FileHandler(Path(get_log_dir(),f"{name_log}.log"), mode='w')
    handler_file.setFormatter(formatter)
    handler_file.setLevel(logging.INFO)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler_file)
    logger.addHandler(handler_stresm)

    return logger
    
    