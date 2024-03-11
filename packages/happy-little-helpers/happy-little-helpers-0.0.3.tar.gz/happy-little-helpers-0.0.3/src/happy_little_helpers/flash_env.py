import os
import platform
import getpass
from happy_little_helpers.debugger import debug_print


def get_flash_path(root_directory):

    if os.name == "nt":  # 'nt' indicates Windows
        # Print OS
        debug_print("Operating System: Windows")

        # Get flashdrive path prefix
        path_prefix = _get_windows_drive_path_prefix()

        # Construct path for windows
        flash_drive_path = os.path.join(path_prefix, root_directory, ".env")

        # Print root_directory
        debug_print("Root Directory: " + root_directory)

    elif platform.system() == "Linux":
        # Print OS
        debug_print("Operating System: Linux")

        # Get root directory and username
        username = _get_linux_username()

        # Construct the path for Linux machines
        flash_drive_path = f"/media/{username}/credentials/{root_directory}/.env"
        debug_print("Flash drive path (Linux): " + flash_drive_path)

    elif platform.system() == "Darwin":
        debug_print("Operating System: MacOS")
        # macOS
    else:
        debug_print("Operating System: Other")
        # Handle other operating systems here
        flash_drive_path = None

    return flash_drive_path


def read_env(flash_drive_path):
    try:
        with open(flash_drive_path, "r") as file:
            env_contents = file.read()
            debug_print("Contents of .env file:")
            debug_print(env_contents)
    except FileNotFoundError:
        debug_print(".env file not found at the specified path.")


def _get_linux_username():
    username = getpass.getuser()
    debug_print("Username: " + username)
    return username


def _get_windows_drive_path_prefix():
    drives = []
    # Get all available drive letters
    for drive in range(ord("A"), ord("Z") + 1):
        drive_letter = chr(drive) + ":"
        if os.path.exists(drive_letter):
            drives.append(drive_letter)

    # Iterate through each drive and check if the volume label matches
    for drive in drives:
        volume_label = "credentials"
        try:
            check_label = os.popen(f"vol {drive}").read().split("\n")[0].split(" ")[-1]
        except Exception as e:
            pass
        if check_label == volume_label:
            debug_print("Drive: " + drive)
            return drive

    return
