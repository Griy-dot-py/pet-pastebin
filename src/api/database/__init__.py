import config.postgres as config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .base import Base
from .main import Database
from .paste import PasteModel
from .user import UserModel

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
Session = sessionmaker(bind=engine, expire_on_commit=False)


# Base.metadata.drop_all(engine) #Only for development
Base.metadata.create_all(engine)

paste_db = Database[PasteModel](sessionmaker=Session, model=PasteModel)
user_db = Database[UserModel](sessionmaker=Session, model=UserModel)
