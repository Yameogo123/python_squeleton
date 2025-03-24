import logging


def configurer_logger(nom_logger="logger", niveau=logging.INFO):
    """
        Configure and return a logger with the specified name and level.

        This function sets up a logger that logs messages to both a file named 'log.log'
        and the console. If the logger with the specified name already exists, it will
        not add additional handlers.

        Args:
            nom_logger (str): The name of the logger. Defaults to "logger".
            niveau (int): The logging level (e.g., logging.INFO, logging.DEBUG). Defaults to logging.INFO.

        Returns:
            logging.Logger: The configured logger instance.
    """
    # Create a logger for the package if does not already exist
    logger = logging.getLogger(nom_logger)
    if not logger.handlers:
        logger.setLevel(niveau)

        # Configure to add to log.log file
        fichier = logging.FileHandler("log.log")  # Nom du fichier de log
        fichier.setLevel(niveau)  # Gravity level for a file
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fichier.setFormatter(formatter)
        logger.addHandler(fichier)

        # Configure to stream the log in the console
        console = logging.StreamHandler()
        console.setLevel(niveau)  # Gravity level for a file
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

logger = configurer_logger()