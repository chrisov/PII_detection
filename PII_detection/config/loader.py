import json
from pathlib import Path
from PII_detection import PACKAGE_ROOT


def load_json(name: str) -> dict:
    """
    Load a JSON config file from PII_detection.config.

    Parameters
        name : Filename without extension (e.g. 'paths', 'rules')

    Returns:
        dict
    """
    
    path = PACKAGE_ROOT / "config" / f"{name}.json"

    if not path.is_file():
        raise FileNotFoundError(f"Config file '{name}.json' not found")

    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def ensure_directory(path: Path) -> Path:
    """
    Ensure that `path` exists and is a directory.
    If path is relative, resolve it relative to PACKAGE_ROOT.
    Creates it (including parents) if necessary.

    Returns the absolute path for convenience.
    """
    if not path.is_absolute():
        path = PACKAGE_ROOT / path
    
    path = path.resolve()
    
    if path.exists():
        if not path.is_dir():
            raise NotADirectoryError(f"{path} exists but is not a directory")
    else:
        path.mkdir(parents=True, exist_ok=True)

    return path
