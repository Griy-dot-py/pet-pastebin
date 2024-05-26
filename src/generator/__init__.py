from redis import Redis
from sequence import UniqueNumberSequence


if __name__ == "__main__":
    with Redis() as redis:
        seq = UniqueNumberSequence(storage=redis, recomended_size=5)
        seq.start_loop()
