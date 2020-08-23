"""
La logique de l'application 
"""

from abc import ABC, abstractmethod

from gestion_etudiant.Notes.persistance import NotesDBAPI

class IServices(ABC):

    @abstractmethod
    def add(self, data):
        pass
    
    @abstractmethod
    def add_note(self, data):
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


class NotesServices(IServices):
    """Les services de gestion des Modules"""

    def __init__(self):
        self._note_dbapi = NotesDBAPI()

    def add(self, note):
        """Permet de créer un nouveau note dans la base"""
        self._note_dbapi.add(note)
        
    def add_note(self, note):
        """Permet de créer un nouveau note dans la base"""
        self._note_dbapi.add(note)
    
    def edit(self, id, note):
        self._note_dbapi.edit(id, note)

    def delete(self, id):
        self._note_dbapi.delete(id)
    
    def get_by_id(self, id):
        return self._note_dbapi.get_by_id(id)
    
    def get_all(self):
        return self._note_dbapi.get_all()
            
        
        