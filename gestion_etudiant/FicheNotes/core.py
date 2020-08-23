"""
La logique de l'application 
"""

from abc import ABC, abstractmethod

from gestion_etudiant.FicheNotes.persistance import FicheNotesDBAPI

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


class FicheNotesServices(IServices):
    """Les services de gestion des Modules"""

    def __init__(self):
        self._fiche_note_dbapi = FicheNotesDBAPI()

    def add(self, note):
        """Permet de créer un nouveau note dans la base"""
        self._fiche_note_dbapi.add(note)
    
    def edit(self, id, note):
        self._fiche_note_dbapi.edit(id, note)

    def delete(self, id):
        self._fiche_note_dbapi.delete(id)
    
    def get_by_id(self, id):
        return self._fiche_note_dbapi.get_by_id(id)
    
    def get_all(self):
        return self._fiche_note_dbapi.get_all()
            
        
        