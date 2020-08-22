"""
Python et la POO
"""
from enum import Enum
from abc import ABC, abstractmethod

class TypeEvaluation(Enum):
    CONTROLE = 1
    EXAMEN = 2


class Groupe:
    """Permet de mémoriser les informations d'un groupe"""

    def __init__(self, id=0, nom_groupe=None,cycle=None, 
                    niveau=None, filiere=None, date_creation=None):
        """Initialiseur de la classe Groupe"""
        self.id = id
        self.nom_groupe = nom_groupe
        self.cycle = cycle
        self.niveau = niveau
        self.filiere = filiere
        self.date_creation = date_creation
    
    def __str__(self):
        """Affichage formaté des données"""
        return f"Id: {self.id}\nGroupe: {self.nom_groupe}\nCycle: {self.cycle} \
                \nNiveau: {self.niveau}\nFilière: {self.filiere} \
                \nDate création: {self.date_creation}"
    

