from flask import Flask
import os
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask - Docker Compose!"

@app.route("/db-test")
def db_test():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "mysql"),
            user="root",
            password="rootpass",
            database="appdb"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return f"MySQL connection successful: {result[0]}"

    except Exception as e:
        return f"MySQL connection failed: {e}"

app.run(host="0.0.0.0", port=5000)
