from importlib import resources

try:
    import tomllib
except ModuleNotFoundError:
    # Third party imports
    import tomli as tomllib


# Version of zurich-parking package
__version__ = "1.0.2"

# Read URL of the Zurich parking feed from config file
_cfg = tomllib.loads(resources.read_text("zurich_parking", "config.toml"))
URL = _cfg["parking_api"]["url"]
