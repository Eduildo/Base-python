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

#Gestion Notes Importation
from gestion_etudiant.Notes.core import NotesServices
from gestion_etudiant.Notes.models import NoteEtudiant


#Gestion Notes Importation
from gestion_etudiant.FicheNotes.core import FicheNotesServices
from gestion_etudiant.FicheNotes.models import FicheNote

from gestion_etudiant.Prof.core import ProfServices
from gestion_etudiant.Prof.models import Prof

def menu():
    print("A D M I N I S T R A C T I O N")
    print("1. GESTION DE GROUPES")
    print("2. GESTION DE MODULES")
    print("3. GESTION DES ETUDIANTS")
    print("4. GESTION DES NOTES")
    print("5. GESTION DES PROFESSEURS")
    print("6. GESTION DES COURS")
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
                    groupe = Groupe()
                    gp_service = GroupeServices()
                    groupe.nom_groupe = str(input("nom_groupe: "))
                    groupe.id_filiere = int(input("id_filiere: "))
                    groupe.id = 1
                    gp_service.edit(groupe.id, groupe)   
                elif choix == 5:
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
                        print(i[1], i[2])
                        
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
                    module = Module()
                    md_service = ModuleServices()
                    module.nom_module = str(input("nom_module: "))
                    module.volume_horaire = int(input("Volume Horaire: "))
                    module.coefficient = int(input("Coefficient"))
                    md_service.edit(12, module)
                elif choix == 4:
                    md_service = ModuleServices()
                    liste_module = md_service.get_all()
                    for i in  liste_module:
                        print(i)
                elif choix == 5:
                    md_service = ModuleServices()
                    liste_module = md_service.get_all()
                    for i in  liste_module:
                        print(i)
                    print("=======================================")
                    id_module = int(input("Veuillez saisir l'id du module a supprimer: "))
                    md_service.delete(id_module)
                    
                elif choix == 6:
                    print("Vous avez choisis quitter le programme")
                    sys.exit()
                else:
                    print("choix inconue")
                    
                    
        elif choix == 3:
            
            print("G E S T I O N  D E S  E T U D I A N T S")
            print("1. LISTE DES EUDIANTS")
            print("2. AJOUTER UN ETUDIANT")
            print("3. MODIFIER LES INFORMATIONS D'UN ETUDIANT")
            print("4. SUPRIMMER UN ETUDIANT")
            print("5. QUITTER")
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
                    etudiant = Etudiant()
                    etudiant.id = 2
                    etudiant.matricule = str(input("Matricule: "))
                    etudiant.prenom = str(input("Prenom: "))
                    etudiant.nom = str(input("Nom: "))
                    etudiant.telephone = str(input("Telephone: "))
                    etudiant.adresse = str(input("Adresse: "))
                    etudiant.email = str(input("Email: "))
                    etudiant.date_naissance = str(input("Date Naissance: "))
                    etudiant.lieu_naissance = str(input("Lieu de Naissance: "))
                    etudiant.nationalite = str(input("Nationalite: "))
                    etudiant.idFiliere = 2
                    etudiant.prenom_contact = str(input("Prenom Contact: "))
                    etudiant.nom_contact = str(input("Nom Contact: "))
                    etudiant.telephone_contact = str(input("Telephone Contact: "))
                    etudiant.email_contact = str(input("Email Contact: "))
                    etudiant_services = EtudiantServices()
                    etudiant_services.add(etudiant)
                elif choix == 3:
                    etudiant = Etudiant()
                    et_service = EtudiantServices()
                    etudiant.nom = str(input("Nom etudiant: "))
                    etudiant.prenom = str(input("Prenom Etudiant: "))
                    etudiant.telephone = str(input("Telephone: "))
                    etudiant.email = str(input("Email: "))
                    et_service.edit(2, etudiant)
                elif choix == 4:
                    list_etudiant = EtudiantServices()
                    etudiants = list_etudiant.get_all()
                    print("============================= Etudiants ==============================|")
                    print("id  Matricule |  Nom  |  Prenom    |   Telephone  |  Adresse ")
                    print("----------------------------------------------------------------------|")
                    for etudiant in etudiants:
        
                        print(etudiant[0], etudiant[1], "|", etudiant[2], "|", etudiant[3],"|", etudiant[4], "|", etudiant[5])
                        print("======================================================================|")
                        
                    id_etudiant = int(input("Suprimer un etudiant par son id: "))
                    list_etudiant.delete(id_etudiant)  
                elif choix == 5:
                    print("Vous avez choisi quitter le programme")
                    sys.exit()  
                else:
                    print("choix inconue")
        elif choix == 4:
            print("G E S T I O N  D E S  NOTES")
            print("1. LANCER LES NOTES")
            print("2. MODIFIER LES NOTES")
            print("3. QUITTER")
            print()
            while True:
                choix = int(input("Votre choix: "))
                if choix == 1:
                    note = NoteEtudiant()
                    fiche_note = FicheNote()
                    fiche_note.type_evaluation = str(input("Type de  evaluation: "))
                    fiche_note.numero_evaluation = int(input("Numero de  evaluation: "))
                    note.id_etudiant = int(input("Id de l'etudiant: "))
                    note.id_fiche_note = int(input("Id Fiche Note: "))
                    note.note = int(input("Note: "))
                    note.remarque = str(input("Remarque: "))
                    fiche_note.id_prof = str(input("Id du prof: "))
                    fiche_note.id_groupe = str(input("Id de groupe: "))
                    fiche_note.id_module = str(input("Id Module: "))
                    fiche_note.date_creation = str(input("Date: "))
                    notes = NotesServices()
                    fiche_notes = FicheNotesServices()
                    fiche_notes.add(fiche_note)
                    notes.add(note)
                    
        elif choix == 5:
            print("G E S T I O N  D E S  P R O F E S S E U R S")
            print("1. LISTE DES PROFESSEURS")
            print("2. AJOUTER UN PROFESSEUR")
            print("3. MODIFIER LES INFORMATIONS D'UN PROFESSEUR")
            print("4. SUPRIMMER UN PROFESSEUR")
            print("5. QUITTER")
            print()
            while True:
                choix = int(input("votre choix: "))
                if choix == 1:
                    list_prof = ProfServices()
                    profs = list_prof.get_all()
                    print("============================= Professeurs ==============================|")
                    print("id  Matricule |  Nom  |  Prenom    |   Telephone  |  Adresse ")
                    print("----------------------------------------------------------------------|")
                    for prof in profs:
        
                        print(prof[0], prof[1], "|", prof[2], "|", prof[3],"|", prof[4], "|", prof[5])
                        print("======================================================================|")

                elif choix == 2:
                    
                    prof = Prof()
                    prof.id = 1
                    prof.matricule = str(input("Matricule: "))
                    prof.prenom = str(input("Prenom: "))
                    prof.nom = str(input("Nom: "))
                    prof.telephone = str(input("Telephone: "))
                    prof.adresse = str(input("Adresse: "))
                    prof.email = str(input("Email: "))
                    prof.date_naissance = str(input("Date Naissance: "))
                    prof.lieu_naissance = str(input("Lieu de Naissance: "))
                    prof.nationalite = str(input("Nationalite: "))
                    prof.specialite = str(input("Specialite: "))
                    
                    prof_service = ProfServices()
                    prof_service.add(prof)
                    
                elif choix == 3:
                    prof = Prof()
                    prof_service = ProfServices()
                    prof.nom = str(input("Nom prof: "))
                    prof.prenom = str(input("Prenom prof: "))
                    prof.telephone = str(input("Telephone: "))
                    prof_service.edit(2, prof)
                elif choix == 4:
                    list_prof = ProfServices()
                    profs = list_prof.get_all()
                    print("============================= Professeurs ==============================|")
                    print("id  Matricule |  Nom  |  Prenom    |   Telephone  |  Adresse ")
                    print("----------------------------------------------------------------------|")
                    for prof in profs:
        
                        print(prof[0], prof[1], "|", prof[2], "|", prof[3],"|", prof[4], "|", prof[5])
                        print("======================================================================|")
                        
                    id_prof = int(input("Suprimer un etudiant par son id: "))
                    list_prof.delete(id_prof)  
                elif choix == 5:
                    print("Vous avez choisi quitter le programme")
                    sys.exit()  
                else:
                    print("choix inconue")
        elif choix == 6:
            print("je suis la gestion de professeurs")
        elif choix == 7:
            print("Vous avez choisis quitter le programme")
            sys.exit()
        else:
            print("Choix inconnue")