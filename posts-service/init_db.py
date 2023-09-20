import psycopg2

# Database configuration
DB_HOST = "database"  # Name of the PostgreSQL service in Kubernetes
DB_PORT = 5432
DB_USER = "postgres"
DB_PASSWORD = "password"  # This should be fetched securely, e.g., from environment variables or Kubernetes secrets
DB_NAME = "flaskblog"

def init_db():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()

    # Create the posts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # Insert initial data
    cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", ('First Post', 'Content for the first post'))
    cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", ('Second Post', 'Content for the second post'))

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    init_db()
