import config.postgres as config
from sqlalchemy import MetaData, Sequence, create_engine
from sqlalchemy.orm import Session

from .seq import UniqueNumberSequence

engine = create_engine(
    "{dialect}+{driver}://{user}:{passw}@{host}:{port}/{db}".format(
        dialect="postgresql",
        driver="psycopg2",
        user=config.USER,
        passw=config.PASSWORD,
        host=config.HOST,
        port=config.PORT,
        db=config.DB,
    )
)
meta = MetaData()

sequence = UniqueNumberSequence(
    seq=Sequence("unique_number_seq", metadata=meta), session=Session(bind=engine)
)

meta.create_all(engine)
