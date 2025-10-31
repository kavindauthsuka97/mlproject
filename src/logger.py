import logging  # Standard Python logging library for emitting log messages
import os       # OS utilities for paths and filesystem operations
from datetime import datetime  # For generating timestamps

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # Filename like '10_31_2025_14_22_05.log'

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)  # Build a path: <cwd>/logs/<timestamp>.log  (used as a *directory* here)
os.makedirs(logs_path, exist_ok=True)  # Create the directory path above; no error if it already exists

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)  # Full file path: <cwd>/logs/<timestamp>.log/<timestamp>.log

logging.basicConfig(  # Configure the root logger once for the process
    filename=LOG_FILE_PATH,  # Write log messages to the file at LOG_FILE_PATH
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Timestamp, line no., logger name, level, message
    level=logging.INFO,  # Minimum level to log; INFO and above will be recorded
)  # End of basic logging configuration
