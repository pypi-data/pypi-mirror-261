import os

USE_MODAL = lambda: os.environ.get("USE_MODAL", "1") == "1"
