from .config import TOKEN

if TOKEN is None:
    raise ValueError("Discord Token is not set. Please set Token in config.py")
