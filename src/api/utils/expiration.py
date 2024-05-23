from datetime import datetime, timedelta


def calculate_expiration(days: int) -> datetime:
    now = datetime.now()
    limited = min(30, days)
    lifetime = timedelta(days=max(1, limited))
    return now + lifetime
