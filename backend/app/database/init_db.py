from app.database.database import Base, engine

import app.database.models

Base.metadata.create_all(bind=engine)

print("Database created successfully!")