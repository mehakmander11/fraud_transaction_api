# init_db.py

from app.database.connection import engine
from app.models.db_models import Base

print("🔧 Creating tables manually...")
Base.metadata.create_all(bind=engine)
print(" Table creation done.")
