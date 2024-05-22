from base64 import urlsafe_b64decode


def unhash_id(hashed_id: str) -> int:
    byte_str = bytes(hashed_id, "utf-8")
    decoded_bytes = urlsafe_b64decode(byte_str)
    return int.from_bytes(decoded_bytes)
