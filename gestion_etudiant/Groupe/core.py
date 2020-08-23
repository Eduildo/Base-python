"""
La logique de l'application 
"""

from abc import ABC, abstractmethod

from gestion_etudiant.Groupe.persistance import GroupeDBAPI

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


class GroupeServices(IServices):
    """Les services de gestion de Groupe"""

    def __init__(self):
        self._groupe_dbapi = GroupeDBAPI()

    def add(self, groupe):
        """Permet de créer un nouveau module dans la base"""
        self._groupe_dbapi.add(groupe)
    
    def edit(self, id, groupe):
        self._groupe_dbapi.edit(id, groupe)

    def delete(self, id):
        self._groupe_dbapi.delete(id)
    
    def get_by_id(self, id):
        return self._groupe_dbapi.get_by_id(id)
    
    def get_all(self):
        return self._groupe_dbapi.get_all()
            
        
        