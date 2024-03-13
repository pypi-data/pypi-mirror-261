class WriteNotPermitted(Exception):
    def __init__(self, filename: str):
        Exception(f"Write permission denided, For file: {filename}")


class ReadNotPermitted(Exception):
    def __init__(self, filename: str):
        Exception(f"Read permission denided, For file: {filename}")
