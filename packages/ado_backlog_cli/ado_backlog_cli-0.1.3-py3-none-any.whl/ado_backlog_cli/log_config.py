"""
Defines custom log levels and sets up logging configuration.

The custom log levels DEV and PERF can be used to log messages
at the developer and performance tracing levels respectively.

The setup_logging function configures the default logging with
the provided log level string, converting it to the appropriate 
numeric level.
"""
# log_config.py
import logging

# Define custom log levels
# DEV_LEVEL_NUM is used for developer level logging
DEV_LEVEL_NUM = 15  
# PERF_LEVEL_NUM is used for performance tracing level logging
PERF_LEVEL_NUM = 25

def setup_custom_log_levels():
    # Add developer level name and logging function
    logging.addLevelName(DEV_LEVEL_NUM, "DEV")
    def dev(self, message, *args, **kwargs):
        if self.isEnabledFor(DEV_LEVEL_NUM):
            self._log(DEV_LEVEL_NUM, message, args, **kwargs)
    logging.Logger.dev = dev

    # Add performance level name and logging function
    logging.addLevelName(PERF_LEVEL_NUM, "PERF")
    def perf(self, message, *args, **kwargs):
        if self.isEnabledFor(PERF_LEVEL_NUM):
            self._log(PERF_LEVEL_NUM, message, args, **kwargs)
    logging.Logger.perf = perf

def setup_logging(log_level='INFO'):
    # Set up the custom log levels
    setup_custom_log_levels()

    # Convert the log level string to a numeric value
    if log_level.upper() == "DEV":
        # Map DEV level string to DEV_LEVEL_NUM
        numeric_level = DEV_LEVEL_NUM
    elif log_level.upper() == "PERF":
        # Map PERF level string to PERF_LEVEL_NUM
        numeric_level = PERF_LEVEL_NUM
    else:
        # Get standard level's numeric value
        numeric_level = getattr(logging, log_level.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError(f'Invalid log level: {log_level}')

    # Set up basic logging with the given log level
    logging.basicConfig(level=numeric_level, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
