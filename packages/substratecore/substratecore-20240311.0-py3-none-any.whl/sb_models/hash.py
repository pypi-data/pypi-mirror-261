def hash_args(*input_strs: str) -> str:
    """
    Hashes input strings using SHA256.
    :param input_strs:
    :return: SHA256 hash of input strings
    """
    import hashlib

    as_str = [str(x) for x in input_strs]

    return hashlib.sha256(",".join(as_str).encode("utf-8")).hexdigest()
