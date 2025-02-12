from datetime import datetime

from flask import abort
from app.extensions import db

class BaseModel(db.Model):
    """ Modèle de base pour toutes les entités avec Soft Delete """
    __abstract__ = True  # Empêche la création de cette table dans la base
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)  # Soft delete



    @classmethod
    def create(cls, **kwargs):
        """
        Crée un nouvel enregistrement avec les données fournies.
        
        :param kwargs: Dictionnaire contenant les champs du modèle.
        :return: L'instance créée.
        """
        try:
            instance = cls(**kwargs)
            db.session.add(instance)
            db.session.commit()
            return instance.to_dict()
        except Exception as e:
            db.session.rollback()
            abort(500, description=f"Erreur lors de la création de {cls.__name__}: {str(e)}")

    def update(self, **kwargs):
        """
        Met à jour l'instance actuelle avec les données fournies.
        :param kwargs: Dictionnaire contenant les champs à mettre à jour.
        :return: L'instance mise à jour.
        """
        try:
            for key, value in kwargs.items():
                if hasattr(self, key):  # Vérifie si l'attribut existe
                    setattr(self, key, value)
            
            self.updated_at = datetime.utcnow()  # Mise à jour du timestamp
            db.session.commit()
            return self.to_dict()
        except Exception as e:
            db.session.rollback()
            abort(500, description=f"Erreur lors de la mise à jour de {self.__class__.__name__}: {str(e)}")

            
    def soft_delete(self):
        """ Met à jour deleted_at au lieu de supprimer physiquement """
        self.deleted_at = datetime.utcnow()
        db.session.commit()

    def restore(self):
        """ Restaure un élément supprimé """
        self.deleted_at = None
        db.session.commit()

    def delete_permanently(self):
        """ Supprime définitivement l'élément de la base """
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def all(cls):
        """ Retourne uniquement les enregistrements non supprimés """
        return cls.query.filter(cls.deleted_at.is_(None))


    @classmethod
    def query_all(cls):
        """ Retourne tous les enregistrements, y compris supprimés """
        return cls.query
    
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}