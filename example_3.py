import sys
import logging
import traceback


def _exception_handler(error_type, error_value, error_traceback):
    """Log all uncaught exceptions at runtime with sys.excepthook"""
    logging.critical("Uncaught exception {} {}".format(
        str(error_type), str(error_value)))
    tb = traceback.format_exception(
        error_type, error_value, error_traceback)
    traceback_string = ''
    for ln in tb:
        traceback_string += ln
    logging.critical(traceback_string)


def begin_log(log_filename='logfile.log', log_level=logging.DEBUG):
    """Log to terminal & file including traceback of any uncaught exceptions"""
    # We use sys.excepthook to handle any uncaught exceptions
    sys.excepthook = _exception_handler
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s",
        level=log_level,
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler(),
        ])


def main():
    begin_log(log_filename='logfile_capturing_traceback.log')
    # Log some things...
    logging.debug("Debugging information logged.")
    logging.info("Useful information logged.")
    logging.warning("Warning message logged.")
    logging.error("Error message logged.")
    logging.critical("Critical error message logged.")
    # You should aim to catch and handle exceptions properly in your code
    # and not rely on logging uncaught exceptions.
    # However, having the full stack trace for any unanticipated exceptions
    # can be very valuable in the event things go wrong.
    raise RuntimeError('This uncaught exception causes the program to crash')


if __name__ == '__main__':
    main()
