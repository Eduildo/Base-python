from mysql.connector import connect, Error



class DatabaseManager:
    
    
    def __init__(self):
        self.__host = "localhost"
        self.__port = "8889"
        self.__user = "root"
        self.__password = "root"
        self.__db_name = "gestion_etudiant"
        self._db_connection = None
        
    
    def get_connection(self):
        """Permet de d'ouvrir une connexion à la base de données"""
        try:
            if self._db_connection is None:
                self._db_connection = \
                connect(host = self.__host, 
                        port = self.__port,
                        user=self.__user,
                        passwd=self.__password,
                        database=self.__db_name
                )
        except Error as error:
            print("Problème de connexion à la base de données: {}".format(error))

        return self._db_connection

    def close_connection(self):
        """Permet de fermer la connxion à a base de données"""
        if self._db_connection:
            self._db_connection.close()
            self._db_connection = None