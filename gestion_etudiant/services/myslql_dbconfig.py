from configparser import ConfigParser

def get_db_config(file='db.ini', section='mysql'):
    """
     Lit le fichier de configuration de base de données
     et retourne un dictionnaire contenant les informations
     récupérées
     """
     #On créé un parseur pour lire le fichier de configuration
    parser = ConfigParser()
    parser.read(file)
    
    # recupere la section mysql du 
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception(f'{section} pas trouvé dans le le fichier {file}')
 
    return db