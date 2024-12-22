from pydantic import BaseModel, EmailStr
from typing import Optional

# Fichier de définition des models ,et possiblement, de DAO

# Pydantic models
class SequenceBase(BaseModel):
    name: str
    info: str

class SequenceCreate(SequenceBase):
    pass

class SequenceRead(SequenceBase):
    id: int

    class Config:
        orm_mode = True  # Permet à Pydantic de lire les données SQLAlchemy
