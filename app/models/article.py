from app.models.base_model import BaseModel
from app.extensions import db


class Article(BaseModel):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    prix = db.Column(db.Float(100))