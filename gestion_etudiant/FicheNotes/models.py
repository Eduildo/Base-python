"""
Python et la POO
"""
from enum import Enum
from abc import ABC, abstractmethod

class TypeEvaluation(Enum):
    CONTROLE = 1
    EXAMEN = 2
    
    
    
class FicheNote:
    """Représente les fiches de notes"""

    def __init__(self, id=0, date_creation=None, type_evaluation=None,
                    date_evaluation=None, id_groupe=None, id_module=None, id_prof=None):
        self.id = id
        self.date_creation = date_creation
        self.type_evaluation = type_evaluation
        self.date_evaluation = date_evaluation
        self.id_groupe = id_groupe
        self.id_module = id_module
        self.id_prof = id_prof
    
    # def __str__(self):
    #     return f"Id: {self.id}\nDate de création: {self.date_creation} \
    #         \nType d'évaluation: {self.type_evaluation} \
    #         \nDate évaluation: {self.date_evaluation} \
    #         \nGroupe: {self.nom_groupe}\nModule: {self.nom_module} \
    #         \nProf: {self.prenom_prof} {self.nom_prof}"

