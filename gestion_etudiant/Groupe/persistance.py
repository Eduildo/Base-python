"""
Ce module permet de faire un couplage 
"""

from abc import ABC, abstractmethod

from mysql.connector import Error

from gestion_etudiant.services.database import DatabaseManager
from gestion_etudiant.Groupe.models import Groupe




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


class GroupeDBAPI(IPersistence):
    """
    Cette classe sert d'interface pour 
    la mannipulation de la base par le module core
    """

    def __init__(self):
        self.db_manager = DatabaseManager()
        self._conn = self.db_manager.get_connection()
        self._cursor = None

    def add(self, groupe):
        """Permet d'insérer des données dans la table module"""  
        self.req = "INSERT INTO groupe(nom_groupe, cycle, niveau, id_filiere, date_creation) \
        values(%s, %s, %s, %s, %s)"
        self.args = (groupe.nom_groupe, groupe.cycle, groupe.niveau, groupe.id_filiere, groupe.date_creation)
        try:
            self._cursor = self._conn.cursor()
            self._cursor.execute(self.req,self.args)
            self._conn.commit()
        except Error as error:
            print(f"Problème sur l'insertion dans la base: {error}")
        finally:
            self._cursor.close()
            self.db_manager.close_connection()

    def edit(self, id, groupe):
        """Permet de modifier des données de la table module """
        self.req = "UPDATE groupe SET nom_groupe = %s, \
                     id_filiere = %s,  \
                     WHERE id = %s"
        
        self.args = (groupe.nom_groupe,groupe.id_filiere, id)
        
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
        self.req = "DELETE FROM groupe WHERE id = %s"
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
        #self.groupe = Groupe()
        self.all_groupes = []
        self.req = "SELECT * from groupe WHERE id_filiere = %s"
        self.args = (id,)
        try:
            self._cursor = self._conn.cursor()
            self._cursor.execute(self.req, self.args)
            self.ligne = self._cursor.fetchall()
            if(self.ligne):
                self.all_groupes = self.ligne
                # self.groupe.id = self.ligne[0]
                # self.groupe.nom_groupe = self.ligne[1]
                # self.groupe.cycle = self.ligne[2]
                # self.groupe.niveau = self.ligne[3]
                # self.groupe.date_creation = self.ligne[4]
        except Error as error:
            print(f"Problème de la sélection dans la base: {error}")
        finally:
            self._cursor.close()
            self.db_manager.close_connection()

        return self.all_groupes
    
    def get_all(self):
        self.all_groupes = []
        self.req = "SELECT * from groupe"
        try:
            self._cursor = self._conn.cursor()
            self._cursor.execute(self.req)
            self.lignes = self._cursor.fetchall()
            if(self.lignes):
               self.all_groupes = self.lignes
        except Error as error:
            print(f"Problème de la sélection dans la base: {error}")
        finally:
            self._cursor.close()
            self.db_manager.close_connection()
        
        return self.all_groupes


