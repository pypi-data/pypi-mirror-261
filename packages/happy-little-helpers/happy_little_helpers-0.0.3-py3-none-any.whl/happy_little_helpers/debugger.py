# Default Setting
DEBUG_MODE = False


def debug_print(message):
    """
    Print the message if debug mode is enabled.
    """
    if DEBUG_MODE:
        print("[DEBUG]:", message)


def enable_debug_mode():
    global DEBUG_MODE
    DEBUG_MODE = True


def disable_debug_mode():
    global DEBUG_MODE
    DEBUG_MODE = False
