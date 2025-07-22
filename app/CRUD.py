from sqlalchemy.orm import Session
from . import BD, estructura 
from typing import List

def get_or_create_autor(db: Session, name: str):
    autor = db.query(BD.Autor).filter_by(name=name).first()
    if not autor:
        autor = BD.Autor(name=name)
        db.add(autor)
    return autor

def get_or_create_tag(db: Session, nombre: str):
    tag = db.query(BD.Tag).filter_by(Nombre=nombre).first()
    if not tag:
        tag = BD.Tag(Nombre=nombre)
        db.add(tag)
    return tag

def create_autor(db: Session, nombre: str):
    autor = db.query(BD.Autor).filter(BD.Autor.name == nombre).first()
    if autor:
        return autor
    autor = BD.Autor(name=nombre)
    db.add(autor)
    db.commit()
    db.refresh(autor)  # <-- Esto es clave, refresca el objeto para obtener su .id
    return autor

def create_cita(db: Session, texto: str, nombre_autor: str, tags: List[str]):
    # Evitar duplicados de cita por texto
    cita_existente = db.query(BD.Cita).filter(BD.Cita.texto == texto).first()
    if cita_existente:
        return cita_existente

    # Obtener o crear autor
    autor_obj = db.query(BD.Autor).filter(BD.Autor.name == nombre_autor).first()
    if not autor_obj:
        autor_obj = BD.Autor(name=nombre_autor)
        db.add(autor_obj)
        db.commit()
        db.refresh(autor_obj)

    # Crear nueva cita
    cita_obj = BD.Cita(texto=texto, idAutor=autor_obj.idAutor)

    # Obtener o crear tags, y asociarlos a la cita
    for tag_nombre in tags:
        tag = db.query(BD.Tag).filter(BD.Tag.Nombre == tag_nombre).first()
        if not tag:
            tag = BD.Tag(Nombre=tag_nombre)
            db.add(tag)
            db.commit()
            db.refresh(tag)
        cita_obj.tags.append(tag)  # ✅ Asocia el tag a la cita correctamente

    db.add(cita_obj)
    db.commit()
    db.refresh(cita_obj)

    return cita_obj