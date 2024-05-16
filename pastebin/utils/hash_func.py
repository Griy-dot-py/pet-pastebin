from base64 import urlsafe_b64encode


def hash_id(id: int) -> str:
    byte_int = id.to_bytes(8)
    encoded_bytes = urlsafe_b64encode(byte_int)
    return encoded_bytes.decode()
