import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

def create_database():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = connection.cursor()

        # Create database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
        print(f"Database '{DB_NAME}' created successfully (if not already existing).")

        # Close connection
        cursor.close()
        connection.close()

        # Connect to the newly created database
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor()

        # Create `User` table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        );
        """)
        print("Table 'user' created.")

        # Create `Patient` table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS patient (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT NOT NULL,
            user_id INT,
            FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
        );
        """)
        print("Table 'patient' created.")

        # Create `HeartRate` table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS heart_rate (
            id INT AUTO_INCREMENT PRIMARY KEY,
            patient_id INT NOT NULL,
            heart_rate INT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (patient_id) REFERENCES patient(id) ON DELETE CASCADE
        );
        """)
        print("Table 'heart_rate' created.")

        connection.commit()
        cursor.close()
        connection.close()
        print("Database setup completed successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    create_database()
