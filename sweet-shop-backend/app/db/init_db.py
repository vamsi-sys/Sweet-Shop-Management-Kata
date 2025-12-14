from app.db.database import engine
from app.db.base import Base
from app.models import user, sweet


def init_db():
    Base.metadata.create_all(bind=engine)
