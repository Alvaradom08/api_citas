from pydantic import BaseModel
from typing import List, Optional

class Autor(BaseModel):
    name: str

class Tag(BaseModel):
    Nombre: str

class Cita(BaseModel):
    texto: str
    autor: Autor
    tags: List[Tag]

class CitaSalida(BaseModel):
    texto: str
    autor: str
    tags: List[str]
    
    class Config:
        orm_mode = True
