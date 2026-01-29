"""
Database connection utilities for PostgreSQL
"""

import os
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from dotenv import load_dotenv

load_dotenv()

def get_db_engine() -> Engine:
    """Create and return a SQLAlchemy engine for PostgreSQL"""
    host = os.getenv('POSTGRES_HOST')
    port = os.getenv('POSTGRES_PORT', '5432')
    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD', '')
    database = os.getenv('POSTGRES_DB')
    
    if not all([host, user, database]):
        raise ValueError("Missing database credentials in .env file")
    
    # Use postgresql+psycopg (works with both psycopg2 and psycopg3)
    connection_string = f"postgresql+psycopg://{user}:{password}@{host}:{port}/{database}"
    
    engine = create_engine(connection_string, echo=False, pool_pre_ping=True)
    return engine


def test_connection():
    """Test database connection"""
    try:
        engine = get_db_engine()
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            version = result.fetchone()[0]
            print("✅ Connected successfully!")
            print(f"PostgreSQL version: {version}")
            return True
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False


if __name__ == "__main__":
    test_connection()
