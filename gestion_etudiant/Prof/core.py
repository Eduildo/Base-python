"""
La logique de l'application 
"""

from abc import ABC, abstractmethod

from gestion_etudiant.Prof.persistance import ProfDBAPI

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


class ProfServices(IServices):
    """Les services de gestion des Modules"""

    def __init__(self):
        self._professeur_dbapi = ProfDBAPI()

    def add(self, prof):
        """Permet de créer un nouveau module dans la base"""
        self._professeur_dbapi.add(prof)
    
    def edit(self, id, prof):
        self._professeur_dbapi.edit(id, prof)

    def delete(self, id):
        self._professeur_dbapi.delete(id)
    
    def get_by_id(self, id):
        return self._professeur_dbapi.get_by_id(id)
    
    def get_all(self):
        return self._professeur_dbapi.get_all()
            
        
        