"""
Ce module permet de faire un couplage 
"""

from abc import ABC, abstractmethod

from mysql.connector import Error

from gestion_etudiant.services.database import DatabaseManager
from gestion_etudiant.Notes.models import NoteEtudiant




class IPersistence(ABC): 
    @abstractmethod
    def add(self, data):  
        pass

    @abstractmethod
    def edit(self, id, data):
        pass

    @abstractmethod
    def delete(self, data):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def get_all(self):
        pass


class NotesDBAPI(IPersistence):
    """
    Cette classe sert d'interface pour 
    la mannipulation de la base par le module core
    """

    def __init__(self):
        self.db_manager = DatabaseManager()
        self._conn = self.db_manager.get_connection()
        self._cursor = None

    def add(self, note):
        """Permet d'insérer des données dans la table module"""  
        self.req = "INSERT INTO note(id_etudiant, id_fiche_note, note, remarque) \
        values(%s, %s, %s, %s)"
        self.args = (note.id_etudiant, note.id_fiche_note, note.note, note.remarque)
        try:
            self._cursor = self._conn.cursor()
            self._cursor.execute(self.req,self.args)
            self._conn.commit()
        except Error as error:
            print(f"Problème sur l'insertion dans la base: {error}")
        finally:
            self._cursor.close()
            self.db_manager.close_connection()
            

    def edit(self, id, fiche_note):
        """Permet de modifier des données de la table module """
        self.req = "UPDATE fiche_note SET type_evaluation = %s, \
                     numero_evaluation = %s,  \
                     WHERE id = %s"
        
        self.args = (fiche_note.type_evaluation,fiche_note.numero_evaluation, id)
        
        try:
            self._cursor = self._conn.cursor()
            self._cursor.execute(self.req,self.args)
            self._conn.commit()
        except Error as error:
            print(f"Problème pendant la modification dans la base: {error}")
        finally:
            self._cursor.close()
            self.db_manager.close_connection()
    
    def delete(self, id):
        self.req = "DELETE FROM fiche_note WHERE id = %s"
        self.args = (id,)
        try:
            self._cursor = self._conn.cursor()
            self._cursor.execute(self.req,self.args)
            self._conn.commit()
        except Error as error:
            print(f"Problème pendant la suppression dans la base: {error}")
        finally:
            self._cursor.close()
            self.db_manager.close_connection()

    def get_by_id(self, id):
        self.etudiant = NoteEtudiant()
        self.req = "SELECT * from note WHERE id_etudiant = %s"
        self.args = (id,)
        try:
            self._cursor = self._conn.cursor()
            self._cursor.execute(self.req, self.args)
            self.ligne = self._cursor.fetchone()
            if(self.ligne):
                self.etudiant.id = self.ligne[0]
                self.etudiant.nom_etudiant = self.ligne[1]
                self.etudiant.volume_horaire = self.ligne[2]
                self.etudiant.coefficient = self.ligne[3]
        except Error as error:
            print(f"Problème de la sélection dans la base: {error}")
        finally:
            self._cursor.close()
            self.db_manager.close_connection()

        return self.etudiant
    
    def get_all(self):
        self.all_etudiants = []
        self.req = "SELECT * from fiche_note"
        try:
            self._cursor = self._conn.cursor()
            self._cursor.execute(self.req)
            self.lignes = self._cursor.fetchall()
            if(self.lignes):
               self.all_etudiants = self.lignes
        except Error as error:
            print(f"Problème de la sélection dans la base: {error}")
        finally:
            self._cursor.close()
            self.db_manager.close_connection()
        
        return self.all_etudiants


