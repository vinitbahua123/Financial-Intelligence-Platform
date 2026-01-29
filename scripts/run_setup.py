"""Database Setup Script"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.database import get_db_engine
from sqlalchemy import text

def run_setup():
    """Execute the database setup SQL file"""
    try:
        print("🔧 Starting database setup...")
        print("-" * 50)
        
        engine = get_db_engine()
        print("✅ Connected to database")
        
        sql_file_path = os.path.join(os.path.dirname(__file__), 'setup_database.sql')
        with open(sql_file_path, 'r') as f:
            sql_commands = f.read()
        print("✅ SQL file loaded")
        
        with engine.begin() as conn:
            conn.execute(text(sql_commands))
        
        print("-" * 50)
        print("✅ Database setup complete!")
        print("\n📊 Created:")
        print("   Schemas: bronze, silver, gold")
        print("   Tables:")
        print("      - bronze.stock_prices")
        print("      - bronze.company_info")
        print("   Indexes: 3 indexes")
        print("-" * 50)
        
    except Exception as e:
        print(f"\n❌ Setup failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_setup()
