import mysql.connector
from mysql.connector import Error
from config import db_config

class MySQLDB:
    def __init__(self):
        self.connection = self.create_connection()

    def create_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(**db_config)
            if connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error: '{e}'")
        return connection

    def add_vehicle(self, vehicle):
        cursor = self.connection.cursor()
        query = """
            INSERT INTO vehicle ( manufacturer, model,`year`, color, mileage)
            VALUES (%s, %s, %s, %s, %s);
        """

        cursor.execute(query, (
            vehicle.manufacturer,
            vehicle.model,
            vehicle.year,
            vehicle.color,
            vehicle.mileage)
        )
        self.connection.commit()
        print("Vehicle created successfully")

    def get_users(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM users"
        cursor.execute(query)
        users = cursor.fetchall()
        for user in users:
            print(user)

    def update_user_email(self, user_id, new_email):
        cursor = self.connection.cursor()
        query = "UPDATE users SET email = %s WHERE id = %s"
        cursor.execute(query, (new_email, user_id))
        self.connection.commit()
        print("User email updated successfully")

    def delete_user(self, user_id):
        cursor = self.connection.cursor()
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        self.connection.commit()
        print("User deleted successfully")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")