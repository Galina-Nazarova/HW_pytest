import logging


def setup_logging(log_file: str) -> logging.Logger:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filename=log_file,
        filemode="w",
        encoding="utf-8",
    )
    return logging.getLogger()
