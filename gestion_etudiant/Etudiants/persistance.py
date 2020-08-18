"""
Ce module permet de faire un couplage 
"""

from abc import ABC, abstractmethod

from mysql.connector import Error

from gestion_etudiant.services.database import DatabaseManager
from gestion_etudiant.Etudiants.models import Etudiant




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


class EtudiantDBAPI(IPersistence):
    """
    Cette classe sert d'interface pour 
    la mannipulation de la base par le module core
    """

    def __init__(self):
        self.db_manager = DatabaseManager()
        self._conn = self.db_manager.get_connection()
        self._cursor = None

    def add(self, etudiant):
        """Permet d'insérer des données dans la table module"""  
        self.req = "INSERT INTO etudiant(nom, prenom, matricule, telephone, adresse, email, date_naissance, lieu_naissance, nationalite, idFiliere, nom_contact, prenom_contact, telephone_contact, email_contact) \
        values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.args = (etudiant.nom, etudiant.prenom, etudiant.matricule, etudiant.telephone, etudiant.adresse, etudiant.email, etudiant.date_naissance, etudiant.lieu_naissance, etudiant.nationalite, etudiant.idFiliere, etudiant.nom_contact, etudiant.prenom_contact, etudiant.telephone_contact, etudiant.email_contact)
        try:
            self._cursor = self._conn.cursor()
            self._cursor.execute(self.req,self.args)
            self._conn.commit()
        except Error as error:
            print(f"Problème sur l'insertion dans la base: {error}")
        finally:
            self._cursor.close()
            self.db_manager.close_connection()

    def edit(self, id, module):
        """Permet de modifier des données de la table module """
        self.req = "UPDATE etudiant SET nom_module = %s, \
                     volume_horaire = %s,  \
                     coefficient = %s WHERE id = %s"
        
        self.args = (module.nom_module,module.volume_horaire, \
                        module.coefficient, id)
        
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
        self.req = "DELETE FROM etudiant WHERE id = %s"
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
        self.etudiant = Etudiant()
        self.req = "SELECT * from etudiant WHERE id = %s"
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
        self.req = "SELECT * from etudiant"
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


