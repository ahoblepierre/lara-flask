from app.extensions import db

# Import de Model
from app.models.user import User
from app.models.role import Role
from app.models.article import Article

def init_db():
    db.create_all()
