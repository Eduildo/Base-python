"""
Ce module permet de faire un couplage 
"""

from abc import ABC, abstractmethod

from mysql.connector import Error

from gestion_etudiant.services.database import DatabaseManager
from gestion_etudiant.Prof.models import Prof




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


class ProfDBAPI(IPersistence):
    """
    Cette classe sert d'interface pour 
    la mannipulation de la base par le module core
    """

    def __init__(self):
        self.db_manager = DatabaseManager()
        self._conn = self.db_manager.get_connection()
        self._cursor = None

    def add(self, prof):
        """Permet d'insérer des données dans la table module"""  
        self.req = "INSERT INTO prof(matricule, nom, prenom, telephone, adresse, email, date_naissance, lieu_naissance, nationalite, specialite) \
        values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.args = (prof.matricule, prof.nom, prof.prenom, prof.telephone, prof.adresse, prof.email, prof.date_naissance, prof.lieu_naissance, prof.nationalite, prof.specialite)
        try:
            self._cursor = self._conn.cursor()
            self._cursor.execute(self.req,self.args)
            self._conn.commit()
        except Error as error:
            print(f"Problème sur l'insertion dans la base: {error}")
        finally:
            self._cursor.close()
            self.db_manager.close_connection()

    def edit(self, id, prof):
        """Permet de modifier des données de la table module """
        self.req = "UPDATE prof SET nom_module = %s, \
                     volume_horaire = %s,  \
                     coefficient = %s WHERE id = %s"
        
        self.args = (prof.nom_module,prof.volume_horaire, \
                        prof.coefficient, id)
        
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
        self.req = "DELETE FROM module WHERE id = %s"
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
        self.prof = Prof()
        self.req = "SELECT * from prof WHERE id = %s"
        self.args = (id,)
        try:
            self._cursor = self._conn.cursor()
            self._cursor.execute(self.req, self.args)
            self.ligne = self._cursor.fetchone()
            if(self.ligne):
                self.prof.id = self.ligne[0]
                self.prof.matricule = self.ligne[1]
                self.prof.nom = self.ligne[2]
                self.prof.prenom = self.ligne[3]
                self.prof.email = self.ligne[4]
                self.prof.specialite = self.ligne[5]
        except Error as error:
            print(f"Problème de la sélection dans la base: {error}")
        finally:
            self._cursor.close()
            self.db_manager.close_connection()

        return self.prof
    
    def get_all(self):
        self.all_professeurs = []
        self.req = "SELECT * from prof"
        try:
            self._cursor = self._conn.cursor()
            self._cursor.execute(self.req)
            self.lignes = self._cursor.fetchall()
            if(self.lignes):
               self.all_professeurs = self.lignes
        except Error as error:
            print(f"Problème de la sélection dans la base: {error}")
        finally:
            self._cursor.close()
            self.db_manager.close_connection()
        
        return self.all_professeurs


