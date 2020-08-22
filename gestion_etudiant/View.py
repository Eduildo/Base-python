import sys

#Gestion etudiants importations
from gestion_etudiant.Etudiants.core import EtudiantServices
from gestion_etudiant.Etudiants.models import Etudiant

#Gestion Module importations
from gestion_etudiant.Modules.core import ModuleServices
from gestion_etudiant.Modules.models import Module

#Gestion groupes importations
from gestion_etudiant.Groupe.core import GroupeServices
from gestion_etudiant.Groupe.models import Groupe

def menu():
    print("A D M I N I S T R A C T I O N")
    print("1. GESTION DE GROUPES")
    print("2. GESTION DE MODULES")
    print("3. GESTION DES COURS")
    print("4. GESTION DES NOTES")
    print("5. GESTION DES ETUDIANTS")
    print("6. GESTION DES PROFESSEURS")
    print("7. QUITTER")
    print()
    
    while True:
        choix = int(input("Votre choix: "))
        if choix == 1:
            print("G E S T I O N  D E  G R O U P E S")
            print("1. LISTE DE TOUS LE GROUPES")
            print("2. LISTE DES GROUPE PAR FILIERE")
            print("3. AJOUTER UN GROUPE")
            print("4. MODIFIER UN GROUPE")
            print("5. QUITTER")
            print()
            while True:
                choix = int(input("votre choix: "))
                if choix == 1:
                    gp_service = GroupeServices()
                    list_groupe = gp_service.get_all()
                    for groupe in list_groupe:
                        print(groupe)
                elif choix == 2:
                    gp_service = GroupeServices()
                    list_groupe = gp_service.get_by_id(1)
                    for groupe in list_groupe:
                        print(groupe)
                elif choix == 3:
                    gp_service = GroupeServices()
                    nom_groupe = str(input("nom_groupe,    : "))
                    cycle = int(input("cycle: "))
                    niveau = str(input("niveau: "))
                    id_filiere = int(input("id_filiere: "))
                    date_creation = str(input("date_creation: "))
                    groupe = Groupe()
                    groupe.id = 1
                    groupe.nom_groupe = nom_groupe
                    groupe.cycle = cycle
                    groupe.niveau = niveau
                    groupe.id_filiere = id_filiere
                    groupe.date_creation = date_creation
                    gp_service.add(groupe)
                    
                elif choix == 4:
                    print("Vous avez choisis quitter le programme")
                    sys.exit()
                else:
                    print("choix inconue")
        elif choix == 2:
            print("G E S T I O N  D E  M O D U L E S")
            print("1. LISTE DE TOUS LE MODULES")
            print("2. AJOUTER UN MODULE")
            print("3. MODIFIER UN MODULE")
            print("4. INFORMATIONS D'UN MODULE")
            print("5. SUPRIMMER UN MODULE")
            print("6. QUITTER")
            print()
            while True:
                choix = int(input("votre choix: "))
                if choix == 1:
                    md_service = ModuleServices()
                    liste_module = md_service.get_all()
                    for i in  liste_module:
                        print(i)
                        
                elif choix == 2:
                    md_service = ModuleServices()
                    nom_module = str(input("Nom de module: "))
                    volume_horaire = int(input("Volume horaire: "))
                    coefficient = int(input("Coefficient: "))
                    module = Module()
                    module.id = 1
                    module.nom_module = nom_module
                    module.volume_horaire = volume_horaire
                    module.coefficient = coefficient
                    md_service.add(module)
                elif choix == 3:
                    print("a developer")
                elif choix == 4:
                    print("Vous avez choisis quitter le programme")
                    sys.exit()
                else:
                    print("choix inconue")
                    
                    
        elif choix == 3:
            
            print("G E S T I O N  D E S  E T U D I A N T S")
            print("1. LISTE DES EUDIANTS")
            print("2. AJOUTER UN ETUDIANT")
            print("3. MODIFIER LES INFORMATIONS D'UN ETUDIANT")
            print("4. INFORMATION D'UN ETUDIANT")
            print("5. SUPRIMMER UN ETUDIANT")
            print("6. QUITTER")
            print()
            while True:
                choix = int(input("votre choix: "))
                if choix == 1:
                    list_etudiant = EtudiantServices()
                    etudiants = list_etudiant.get_all()
                    print("============================= Etudiants ==============================|")
                    print("id  Matricule |  Nom  |  Prenom    |   Telephone  |  Adresse ")
                    print("----------------------------------------------------------------------|")
                    for etudiant in etudiants:
        
                        print(etudiant[0], etudiant[1], "|", etudiant[2], "|", etudiant[3],"|", etudiant[4], "|", etudiant[5])
                        print("======================================================================|")

                elif choix == 2:
                    print("a developer")
                elif choix == 3:
                    print("a developer")
                elif choix == 4:
                    print("Vous avez choisis quitter le programme")
                    sys.exit()
                else:
                    print("choix inconue")
        elif choix == 4:
            print("je suis la gestion de notes")
        elif choix == 5:
            print("je suis la gestion de etudiants")
        elif choix == 6:
            print("je suis la gestion de professeurs")
        elif choix == 7:
            print("Vous avez choisis quitter le programme")
            sys.exit()
        else:
            print("Choix inconnue")