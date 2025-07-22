from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .conexcionBD import Base

citasTag = Table(
    "citasTag", Base.metadata,
    Column("idCitaTag", ForeignKey("citas.id"), primary_key=True),
    Column("tagId", ForeignKey("tags.idTag"), primary_key=True)
)

class Autor(Base):
    __tablename__ = "autores"
    idAutor = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

class Tag(Base):
    __tablename__ = "tags"
    idTag = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(100), unique=True, nullable=False)
    citas = relationship("Cita", secondary=citasTag, back_populates="tags")

class Cita(Base):
    __tablename__ = "citas"
    id = Column(Integer, primary_key=True, index=True)
    texto = Column(String, nullable=False)
    idAutor = Column(Integer, ForeignKey("autores.idAutor"))
    
    autor = relationship("Autor")
    tags = relationship("Tag", secondary=citasTag, back_populates="citas")
