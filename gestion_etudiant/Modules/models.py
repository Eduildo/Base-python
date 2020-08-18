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
    

class Etudiant(Personne):
    """Représente un étudiant """

    def __init__(self,id=0, matricule=None, prenom=None, nom=None, 
                    telephone=None,adresse=None, email=None, 
                    date_naissance=None, lieu_naissance=None, 
                    nationalite=None,prenom_contact=None, 
                    nom_contact=None, telephone_contact=None,
                    email_contact=None):
        super().__init__(id=0, matricule=None, prenom=None, nom=None,
                        telephone=None,adresse=None, email=None, 
                        date_naissance=None, lieu_naissance=None, 
                        nationalite=None)
        self.prenom_contact = prenom_contact
        self.nom_contact = nom_contact
        self.telephone_contact = telephone_contact
        self.email_contact = email_contact
    
    def __str__(self):
        return super().__str__() + f"\nPrénom du contact: {self.prenom_contact} \
            \nNom du contact: {self.nom_contact} \
            \nTéléphone du contact: {self.telephone_contact} \
            \nE-mail du contact: {self.email_contact}"


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
        self.etudiants = []
    
    def __str__(self):
        """Affichage formaté des données"""
        return f"Id: {self.id}\nGroupe: {self.nom_groupe}\nCycle: {self.cycle} \
                \nNiveau: {self.niveau}\nFilière: {self.filiere} \
                \nDate création: {self.date_creation}"
    

class FicheNote:
    """Représente les fiches de notes"""

    def __init__(self, id=0, date_creation=None, type_evaluation=None,
                    date_evaluation=None, groupe=None, module=None, prof=None):
        self.id = id
        self.date_creation = date_creation
        self.type_evaluation = type_evaluation
        self.date_evaluation = date_evaluation
        self.nom_groupe = groupe.nom_groupe
        self.nom_module = module.nom_module
        self.prenom_prof = prof.prenom
        self.nom_prof = prof.nom
    
    def __str__(self):
        return f"Id: {self.id}\nDate de création: {self.date_creation} \
            \nType d'évaluation: {self.type_evaluation} \
            \nDate évaluation: {self.date_evaluation} \
            \nGroupe: {self.nom_groupe}\nModule: {self.nom_module} \
            \nProf: {self.prenom_prof} {self.nom_prof}"


class NoteEtudiant:
    """Représente les notes des étudiants par module"""

    def __init__(self, id=0, etudiant=None, fiche_note=None, 
                    note=None, remarque=None):

        self.id = id
        self.etudiant = etudiant
        self.fiche_note = fiche_note
        self.note = note
        self.remarque = remarque

    def __str__(self):
       return f"ID: {self.id} \
           \nID Fiche de note: {self.fiche_note.id} \
           \nModule: {self.fiche_note.nom_module} \
           \nType évaluation: {self.fiche_note.type_evaluation} \
           \netudiant: {self.etudiant.prenom} {self.etudiant.nom} \
           \nNote: {self.note}\nRemarque: {self.remarque}"







            




    

