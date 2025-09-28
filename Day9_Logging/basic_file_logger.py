"""
28/09/2025

The usage of this script is to ask user for a message, and write it into activy log with a timestamp 

Eg. YYYY-MM-DD HH:MM:SS | INFO | User Types: Hello world
"""

import logging 
# Configure the basic logging settings
logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w", format='%(asctime)s | %(levelname)s | %(message)s')

logging.info("Program started")
logging.warning("This might cause an issue")
logging.error("Something went wrong")