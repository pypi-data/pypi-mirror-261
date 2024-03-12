from sb_models.logger import log


def print_dir(root_dir, level=0):
    """
    Print the contents of a directory up to MAX_DEPTH
    """
    import os

    MAX_DEPTH = 2

    if level > MAX_DEPTH:
        return
    for entry in os.listdir(root_dir):
        path = os.path.join(root_dir, entry)
        log.info("  " * level + path)
        if os.path.isdir(path):
            print_dir(path, level + 1)
