from sqlalchemy import Column, String

from app.database.database import Base


class Project(Base):

    __tablename__ = "projects"

    project_id = Column(String, primary_key=True, index=True)

    project_name = Column(String)

    workspace = Column(String)

    container_id = Column(String)

    status = Column(String)