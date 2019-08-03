import logging


def configure_logging(log_filename='logfile.log', log_level=logging.DEBUG):
    """Log to the terminal and to file simultaneously."""
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s",
        level=log_level,
        # Multiple handlers can be added to your logging configuration.
        # By default log messages are appended to the file if it exists already
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler(),
        ])


def main():
    # Try begin_log(log_level=logging.WARNING) and see what happens
    # Try begin_log(log_filename='my_custom_log_file.log')
    # You may find it useful to include a timestamp string in the log filename
    configure_logging()
    # Log some things...
    logging.debug("Debugging information logged.")
    logging.info("Useful information logged.")
    logging.warning("Warning message logged.")
    logging.error("Error message logged.")
    logging.critical("Critical error message logged.")


if __name__ == '__main__':
    main()
