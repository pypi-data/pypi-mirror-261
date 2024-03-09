import os
import platform
import getpass
from happy_little_helpers.debugger import debug_print


def get_flash_path():

    if os.name == 'nt':  # 'nt' indicates Windows
        debug_print('Operating System: Windows')
    elif platform.system() == 'Linux':
        # Print OS
        debug_print('Operating System: Linux')

        # Get root directory and username
        root_directory_name = _get_root_directory_name()
        username = _get_linux_username()

        # Construct the path for Linux machines
        flash_drive_path = f"/media/{username}/credentials/{root_directory_name}/.env"
        debug_print("Flash drive path (Linux): " + flash_drive_path)

    elif platform.system() == 'Darwin':
        debug_print('Operating System: MacOS')
        # macOS
    else:
        debug_print('Operating System: Other')
        # Handle other operating systems here
        flash_drive_path = None

    return flash_drive_path



def read_env(flash_drive_path):
    # Read the contents of the .env file and print it to the console
    try:
        with open(flash_drive_path, 'r') as file:
            env_contents = file.read()
            debug_print("Contents of .env file:")
            debug_print(env_contents)
    except FileNotFoundError:
        debug_print(".env file not found at the specified path.")

def _get_root_directory_name():
    # Get the current file path (should be env-loader.py in components directory)
    current_file_path = os.path.abspath(__file__)
    debug_print("Current file path: " + current_file_path)

    # Get the root directory name (should be the directory just after GitHub)
    root_directory_name = os.path.basename(os.path.dirname(os.path.dirname(current_file_path)))
    debug_print("Root directory name: " + root_directory_name)
    return root_directory_name

def _get_linux_username():
    # Get the current username
    username = getpass.getuser()
    debug_print("Username: " + username)
    return username