from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config


engine = create_engine(
    "{dialect}+{driver}://{user}:{passw}@{host}/{db}"
    .format(
        dialect="postgresql",
        driver="psycopg2",
        user=config.POSTGRES_USER,
        passw=config.POSTGRES_PASSWORD,
        host=config.POSTGRES_HOST,
        db=config.POSTGRES_DB
    )
)
Session = sessionmaker(bind=engine, expire_on_commit=False)


from .base import Base
from .user import UserModel
from.paste import PasteModel
from .main import Database


# Base.metadata.drop_all(engine) #Only for development
Base.metadata.create_all(engine)

paste_db = Database(sessionmaker=Session, model=PasteModel)
user_db = Database(sessionmaker=Session, model=UserModel)
