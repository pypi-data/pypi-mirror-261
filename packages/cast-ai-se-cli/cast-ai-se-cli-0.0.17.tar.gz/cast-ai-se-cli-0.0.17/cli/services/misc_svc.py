import os
import platform
import sys
from dotenv import load_dotenv
from docopt import ParsedOptions

from cli.constants import LOG_DIR, LOG_FILE, CONFIG_PATH
from cli.models.config import ConfigObject
import logging


def init(parsed_options: ParsedOptions) -> ConfigObject:
    CONFIG_PATH_PREFIX = os.getenv('CONFIG_PATH_PREFIX') or ""
    cfg = ConfigObject(parsed_options, config_file_path=CONFIG_PATH_PREFIX + CONFIG_PATH)

    log_level = logging.DEBUG if cfg.app_inputs["debug"] else logging.WARNING
    os.makedirs(LOG_DIR, exist_ok=True)
    logging.basicConfig(filename=os.path.join(LOG_DIR, LOG_FILE),
                        format='%(asctime)s - %(levelname)s:%(name)s - %(message)s',
                        level=log_level)

    logger = logging.getLogger(__name__)

    logger.info(f"{'=' * 200}")
    logger.info(f"Starting executing SE CLI Command Sequencer with the following inputs: {sys.argv[1:]}")
    logger.debug(f"{get_system_info()}")
    return cfg


def get_system_info():
    return {'OS': platform.system(), 'OS Version': platform.version(), 'Machine': platform.machine()}


def load_env():
    if os.path.exists("constants.env"):
        load_dotenv(dotenv_path="constants.env")


def get_current_version() -> str:
    current_file_path = os.path.abspath(__file__)  # Get absolute path of the current file
    grandparent_dir_path = os.path.dirname(os.path.dirname(os.path.dirname(current_file_path)))  # Go 3 levels up
    version_file_path = os.path.join(grandparent_dir_path, 'version.txt')  # Construct the full path
    try:
        with open(version_file_path, 'r') as version_file:
            return version_file.read()
    except FileNotFoundError:
        return "ERROR: Version file not found"
