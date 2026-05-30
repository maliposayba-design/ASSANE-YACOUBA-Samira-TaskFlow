import mysql.connector
from mysql.connector import Error

CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "taskflow_db",
    "charset": "utf8mb4"
}

def obtenir_connexion():
    try:
        conn = mysql.connector.connect(**CONFIG)

        if conn.is_connected():
            print("Connexion réussie à MySQL")
            return conn

    except Error as e:
        print(f"Erreur de connexion : {e}")
        return None


def fermer_connexion(conn):
    if conn:
        conn.close()
        print("Connexion fermée")