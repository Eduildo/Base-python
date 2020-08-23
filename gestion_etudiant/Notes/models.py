"""
Python et la POO
"""
from enum import Enum
from abc import ABC, abstractmethod

class TypeEvaluation(Enum):
    CONTROLE = 1
    EXAMEN = 2
    


class NoteEtudiant:
    """Représente les notes des étudiants par module"""

    def __init__(self, id=0, id_etudiant=None, id_fiche_note=None, 
                    note=None, remarque=None):

        self.id = id
        self.id_etudiant = id_etudiant
        self.id_fiche_note = id_fiche_note
        self.note = note
        self.remarque = remarque

    # def __str__(self):
    #    return f"ID: {self.id} \
    #        \nID Fiche de note: {self.fiche_note.id} \
    #        \nModule: {self.fiche_note.nom_module} \
    #        \nType évaluation: {self.fiche_note.type_evaluation} \
    #        \netudiant: {self.etudiant.prenom} {self.etudiant.nom} \
    #        \nNote: {self.note}\nRemarque: {self.remarque}"







            




    

