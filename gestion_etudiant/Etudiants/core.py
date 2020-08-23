"""
La logique de l'application 
"""

from abc import ABC, abstractmethod

from gestion_etudiant.Etudiants.persistance import EtudiantDBAPI

class IServices(ABC):

    @abstractmethod
    def add(self, data):
        pass
   
    @abstractmethod
    def edit(self, id, data):
        pass

    @abstractmethod
    def delete(self, id):
        pass
    
    @abstractmethod
    def get_by_id(self, data_id):
        pass
    
    @abstractmethod
    def get_all(self):
        pass


class EtudiantServices(IServices):
    """Les services de gestion des etudiants"""

    def __init__(self):
        self._etudiant_dbapi = EtudiantDBAPI()

    def add(self, etudiant):
        """Permet de créer un nouveau etudiant dans la base"""
        self._etudiant_dbapi.add(etudiant)
    
    def edit(self, id, etudiant):
        self._etudiant_dbapi.edit(id, etudiant)

    def delete(self, id):
        self._etudiant_dbapi.delete(id)
    
    def get_by_id(self, id):
        return self._etudiant_dbapi.get_by_id(id)
    
    def get_all(self):
        return self._etudiant_dbapi.get_all()
            