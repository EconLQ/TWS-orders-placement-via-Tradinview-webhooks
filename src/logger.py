import logging

# Create and configure logger
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

# Create console handler and set level to INFO
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add formatter to ch
ch.setFormatter(formatter)

# Add ch to logger
LOGGER.addHandler(ch)
