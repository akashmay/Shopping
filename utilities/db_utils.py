import mysql.connector

host="localhost"
username="root"
password="test"



class DbConnect:

    @staticmethod
    def connect_to_db(db_name):
        conn = mysql.connector.connect(host=host,
                                       user=username,
                                       password=password,
                                       database=db_name)
        return conn


