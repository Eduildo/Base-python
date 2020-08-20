import sys
from gestion_etudiant.Etudiants import persistance
from gestion_etudiant.Modules.core import ModuleServices
from gestion_etudiant.Modules.models import Module

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
            print("2. AJOUTER UN GROUPE")
            print("3. MODIFIER UN GROUPE")
            print("4. QUITTER")
            print()
            while True:
                choix = int(input("votre choix: "))
                if choix == 1:
                    print("a developer")
                elif choix == 2:
                    print("a developer")
                elif choix == 3:
                    print("a developer")
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
            print("4. SUPRIMMER UN MODULE")
            print("5. QUITTER")
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
                    module = Module(1, "Python", 20, 1)
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
            print("je suis la gestion de cours")
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