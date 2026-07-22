"""
WayClip configuration paths.
"""

from pathlib import Path
import os

APP_NAME = "wayclip"

CONFIG_DIR = Path.home() / ".config" / APP_NAME
DATA_DIR = Path.home() / ".local" / "share" / APP_NAME
CACHE_DIR = Path.home() / ".cache" / APP_NAME

RUNTIME_DIR = Path(
    os.environ.get(
        "XDG_RUNTIME_DIR",
        f"/run/user/{os.getuid()}"
    )
) / APP_NAME


def ensure_directories():
    """Create all required directories if they don't exist."""
    for directory in (
        CONFIG_DIR,
        DATA_DIR,
        CACHE_DIR,
        RUNTIME_DIR,
    ):
        directory.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    ensure_directories()

    print("Configuration directories:")
    print(f"Config : {CONFIG_DIR}")
    print(f"Data   : {DATA_DIR}")
    print(f"Cache  : {CACHE_DIR}")
    print(f"Runtime: {RUNTIME_DIR}")
