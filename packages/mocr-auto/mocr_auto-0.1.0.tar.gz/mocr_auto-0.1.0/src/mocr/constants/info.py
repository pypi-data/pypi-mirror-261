import os
import sys
from pathlib import Path


MOCR_VERSION = "0.1.0"
DEFAULT_CHROMIUM_VERSION = "1233136"
DEFAULT_FIREFOX_BUILD = "123.0a1"
CHROMIUM_VERSION = os.environ.get(
    'MOCR_CHROMIUM_VERSION',
    DEFAULT_CHROMIUM_VERSION,
)
FIREFOX_BUILD = os.environ.get(
    'MOCR_CHROMIUM_VERSION',
    DEFAULT_FIREFOX_BUILD,
)

if os.environ.get("MOCR_INSTALL_DIR"):
    INSTALL_DIR_NAME = os.environ["MOCR_INSTALL_DIR"]
elif sys.platform == "linux":
    INSTALL_DIR_NAME = "~/.cache/"
elif sys.platform == "darwin":
    INSTALL_DIR_NAME = "~/Library/Caches/"
elif sys.platform == "win32":
    INSTALL_DIR_NAME = os.path.expandvars("%USERPROFILE%/AppData/Local/")
else:
    raise NotImplementedError(
        "Unsupported platform. Set MOCR_INSTALL_DIR environment variable to"
        " bypass this check."
    )
INSTALL_PATH = Path(INSTALL_DIR_NAME) / 'mocr'
