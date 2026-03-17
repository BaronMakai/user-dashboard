# utils.py

import os
import time
import logging

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def get_timestamp():
    """Returns the current time in seconds since the epoch."""
    return int(time.time())

def get_user_dir():
    """Returns the user's home directory."""
    return os.path.expanduser('~')

def get_logs_dir(user_dir):
    """Returns the path to the logs directory."""
    return os.path.join(user_dir, '.user-dashboard', 'logs')

def get_data_dir(user_dir):
    """Returns the path to the data directory."""
    return os.path.join(user_dir, '.user-dashboard', 'data')

def get_config_file(user_dir):
    """Returns the path to the configuration file."""
    return os.path.join(user_dir, '.user-dashboard', 'config.json')

def get_cache_file(user_dir):
    """Returns the path to the cache file."""
    return os.path.join(user_dir, '.user-dashboard', 'cache.json')