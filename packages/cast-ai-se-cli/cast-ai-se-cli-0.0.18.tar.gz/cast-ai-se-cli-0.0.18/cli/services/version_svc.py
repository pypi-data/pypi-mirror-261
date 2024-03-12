import os
import requests
from typing import Optional
from packaging import version


def get_current_version() -> str:
    current_file_path = os.path.abspath(__file__)  # Get absolute path of the current file
    grandparent_dir_path = os.path.dirname(os.path.dirname(os.path.dirname(current_file_path)))  # Go 3 levels up
    version_file_path = os.path.join(grandparent_dir_path, 'version.txt')  # Construct the full path
    try:
        with open(version_file_path, 'r') as version_file:
            return version_file.read()
    except FileNotFoundError:
        return ""


def get_latest_version(package_name: str = "cast-ai-se-cli") -> Optional[str]:
    try:
        response = requests.get(f'https://pypi.org/pypi/{package_name}/json')
        response.raise_for_status()
        data = response.json()
        latest_version = data['info']['version']
        return latest_version
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None


def check_if_latest_version():
    l_version = get_latest_version()
    c_version = get_current_version()
    if not l_version or not c_version:
        return
    latest_version = version.parse(l_version)
    current_version = version.parse(c_version)
    if latest_version > current_version:
        print(f"New version ({latest_version}) is out! Please consider upgrading.\n")
