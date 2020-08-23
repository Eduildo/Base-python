"""
Python et la POO
"""
from enum import Enum
from abc import ABC, abstractmethod

class TypeEvaluation(Enum):
    CONTROLE = 1
    EXAMEN = 2

class Module:
    """
    Permet de mémoriser les informations sur un module
    """
    def __init__(self, id=None, nom_module=None, volume_horaire=None, coefficient=None):
        """Initialiseur de la classe Module """
        self.id = id
        self.nom_module = nom_module
        self.volume_horaire = volume_horaire
        self.coefficient = coefficient
    
    def __str__(self):
        return f"Id: {self.id}\nNom: {self.nom_module} \
            \nVolume horaire: {self.volume_horaire} \
            \nCoefficient: {self.coefficient}"