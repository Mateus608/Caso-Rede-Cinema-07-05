import sqlite3

class ConnectionFactory:

    @staticmethod
    def get_connection():
        return sqlite3.connect("src/database/cinema.db")
