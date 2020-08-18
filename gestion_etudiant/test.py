"""
Point d'entrée de l'application
"""
from datetime import datetime
import configparser

from gestion_etudiant.Etudiants.models import (Module, Groupe, Prof, Etudiant, 
                                    FicheNote, NoteEtudiant, 
                                    TypeEvaluation)
#from gestion_notes.view import view_main
# from gestion_etudiant.classes_abstraites import Polygone, Triangle
# from gestion_etudiant.interfaces import Panier, CalculImpl

#from gestion_etudiant.models import ModuleService
from gestion_etudiant.services.database import DatabaseManager
from gestion_etudiant.Etudiants.core import EtudiantServices


def main():
    """
    Fonction principale de l'application
    """

    """
    prof = Prof()
    prof.id = 1
    prof.matricule = "PRFG256412"
    prof.prenom = "Ibrahima"
    prof.nom = "Fall"
    prof.telephone = "77 745 76 30"
    prof.adresse = "Sicap Dieupeu II 2411/D "
    prof.email = "iboufall@gmail.fr"
    prof.date_naissance = "25/03/1985"
    prof.lieu_naissance = "Thiès"
    prof.nationalite = "Sénégalaise"
    prof.specialite = "Programmation"
    #print(prof)

    etudiant1 = Etudiant()
    etudiant1.id = 1
    etudiant1.matricule = "PRHT256560"
    etudiant1.prenom = "Albert"
    etudiant1.nom = "Sène"
    etudiant1.telephone = "76 568 24 12"
    etudiant1.adresse = "Sicap Dieupeu II 2411/D "
    etudiant1.email = "iboufall@gmail.fr"
    etudiant1.date_naissance = "25/03/1985"
    etudiant1.lieu_naissance = "Thiès"
    etudiant1.nationalite = "Sénégalaise"
    etudiant1.idFiliere = 2
    etudiant1.prenom_contact = "Jeseph"
    etudiant1.nom_contact = "Ndong"
    etudiant1.telephone_contact = "77 612 35 45"
    etudiant1.email_contact = "joendong@yahoo.fr"
    #print(etudiant1)
    """
    # etudiant2 = Etudiant()
    # etudiant2.id = 2
    # etudiant2.matricule = "PRHT256591"
    # etudiant2.prenom = "Francisco"
    # etudiant2.nom = "Camala"
    # etudiant2.telephone = "77 325 14 42"
    # etudiant2.adresse = "liberte 6 N°61 "
    # etudiant2.email = "franck@gmail.fr"
    # etudiant2.date_naissance = "13/11/2012"
    # etudiant2.lieu_naissance = "Bingnona"
    # etudiant2.nationalite = "Sénégalaise"
    # etudiant2.idFiliere = 2
    # etudiant2.prenom_contact = "Mariama"
    # etudiant2.nom_contact = "Sonko"
    # etudiant2.telephone_contact = "76 522 20 19"
    # etudiant2.email_contact = "sonkomariama@gmail.com"
    #print(etudiant2)

    #groupe1 = Groupe(1, "PR308", "Licence", "Licence 3", "Programmation", "25/03/2020")
    """groupe2 = Groupe()
    groupe2.id = 2
    groupe2.nom_groupe = "PR308"
    groupe2.cycle = "Licence"
    groupe2.niveau = "Licence 3"
    groupe2.filiere = "Programmation"
    groupe2.date_creation =  "25/03/2020"
    """
    
    
    #Ajout d'étudiant dans le groupe 2
    """groupe2.etudiants.append(etudiant1)
    groupe2.etudiants.append(etudiant2)
    print(groupe2)
    print("=================Etudiants du groupe =====================")
    if len(groupe2.etudiants) > 0:
        for etudiant in groupe2.etudiants:
            print(f"Matricule: {etudiant.matricule}\
            \nPrénom et nom : {etudiant.prenom} {etudiant.nom}")
        print("------------------------------------------------------")
    else:
        print("Le groupe ne contient aucun étudiant")
    

    id_fiche = 1
    type_evaluation = TypeEvaluation.CONTROLE.name.capitalize()
    date_evaluation = "12/04/2020"
    date_creation = datetime.strftime(datetime.today(), "%d/%m/%Y")
    
    fiche_note1 = FicheNote(id_fiche,date_creation, type_evaluation,date_evaluation,
           groupe2, module1, prof)"""
    
    #print(fiche_note1)
    
    #id1 = 1
    """note1 = 14
    remarque1 = ""
    note_etudiant1 = NoteEtudiant(id1, etudiant1, fiche_note1, note1, remarque1)"""


    """id2 = 2
    note2 = 12
    remarque2 = ""
    note_etudiant2 = NoteEtudiant(id2, etudiant2, fiche_note1, note2, remarque2)
    print(note_etudiant1)
    print()
    #print(note_etudiant2)

    notes = {}
    notes[note_etudiant1.id] = note_etudiant1
    notes[note_etudiant2.id] = note_etudiant2

    print("==================== Notes obtenues ===================== ")
    for value in notes.values():
        if value.fiche_note.id == 1:
            print(value)
            print("-------------------------------")"""
    

    #e_resident = EtudiantResident("Salif", "Sané", "HL5", "77 456 68 89","PR745GK78")
    #print(e_resident)   
    
    """print(A.mro())
    print(B.mro())
    print(C.mro())
    print(D.mro())

    chaine = ReversableStr("Python")
    print(chaine.inverser())

    mon_tuple = ReversableTuple((5, 8, 10))
    print(mon_tuple.inverser())"""
    
    #view_main()
    """triangle = Triangle("Triangle", 10, 5)
    print(isinstance(triangle, Polygone))

    articles = ["Chocolat", "Savon", "Sucre", "Mangue"]
    panier = Panier(articles)
    print("Savon" in panier)

    calcul = CalculImpl()
    print(calcul.addition(5, 10))
    print(calcul.multiplication(6,3))"""

    """md_service = ModuleService()
    module1 = Module(1, "Python", 20, 1)
    md_service.add_module(module1)
    
    liste_module = md_service.get_all_module()
    for i in  liste_module:
        print(i)"""
  
    #Ajout Module
    
    etudiant_service = EtudiantServices()
    #etudiant_service.add(etudiant2)
    
    
    
    # module2 = Module(2, "Programmation PHP", 30, 1)
    # module_services = ModuleServices()
    #module_services.add(module2)
    
    # Fin Ajout Module
    

    # module2.nom_module = "Programmation PHP POO"
    # module_services.edit(10, module2)

    #module_services.delete(6)

    # module = module_services.get_by_id(10)
    # print(module)
    
    
    

    list_module = etudiant_service.get_all()
    print("============================= Etudiants ==============================|")
    print("id  Matricule |  Nom  |  Prenom    |   Telephone  |  Adresse ")
    print("----------------------------------------------------------------------|")
    for module in list_module:
        
        print(module[0], module[1], "|", module[2], "|", module[3],"|", module[4], "|", module[5])
        print("======================================================================|")
        



if __name__ == "__main__":
    main()