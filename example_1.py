import logging


def begin_log(log_level=logging.DEBUG):
    """A basic logging setup."""
    logging.basicConfig(
        # display timestamp, logging level, and then the message
        format="%(asctime)s %(levelname)s %(message)s",
        level=log_level,  # Log levels: debug, info, warning, error, critical
        handlers=[
            logging.StreamHandler()
        ])


def main():
    begin_log()  # Try begin_log(log_level=logging.WARNING) & see what happens
    # Log some things...
    logging.debug("Debugging information logged.")
    logging.info("Useful information logged.")
    logging.warning("Warning message logged.")
    logging.error("Error message logged.")
    logging.critical("Critical error message logged.")


if __name__ == '__main__':
    main()
