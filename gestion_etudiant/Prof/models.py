"""
Python et la POO
"""
from enum import Enum
from abc import ABC, abstractmethod

class TypeEvaluation(Enum):
    CONTROLE = 1
    EXAMEN = 2


class Personne:
    """Une classe générique qui sert à l'héritage """
    
    def __init__(self, id=0, matricule=None, prenom=None, 
        nom=None, telephone=None,adresse=None, email=None, 
        date_naissance=None, lieu_naissance=None, nationalite=None):
        """Permet d'initialiser les attributs de la classe"""
        self.id = id 
        self.matricule = matricule
        self.prenom = prenom
        self.nom = nom
        self.telephone = telephone
        self.adresse = adresse
        self.email = email
        self.date_naissance = date_naissance
        self.lieu_naissance = lieu_naissance
        self.nationalite = nationalite

    def __str__(self):
        return f"Id: {str(self.id)}\nMatricule: {self.matricule}\nPrénom: {self.prenom} \
            \nNom: {self.nom}\nTéléphone: {self.telephone}\nAdresse: {self.adresse} \
            \nE-mail: {self.email}\nDate de naissance: {self.date_naissance} \
            \nLieu de naissance: {self.lieu_naissance}\nNationalité: {self.nationalite}"


class Prof(Personne):
    """Représente une personne"""

    def __init__(self, id=0, matricule=None, prenom=None, 
        nom=None, telephone=None,adresse=None, email=None, 
        date_naissance=None, lieu_naissance=None, nationalite=None,
        specialite=None):
        super().__init__(id=0, matricule=None, prenom=None, 
        nom=None, telephone=None,adresse=None, email=None, 
        date_naissance=None, lieu_naissance=None, nationalite=None)
        self.specialite = specialite
    
    def __str__(self):
        return super().__str__() + f"\nSpécialité: {self.specialite}"
    

