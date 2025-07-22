from fastapi import FastAPI, Depends,Query
from sqlalchemy.orm import Session
from .conexcionBD import SessionLocal
from .BD import Cita
from .Scraping import scrape
from typing import Optional, List
from fastapi.responses import JSONResponse

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/quotes")
def get_quotes(
    author: Optional[str] = Query(None),
    tag: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(BD.Cita)

    # Join con autor si se filtra por nombre del autor
    if author:
        query = query.join(BD.Autor).filter(BD.Autor.name.ilike(f"%{author}%"))

    # Join con tags si se filtra por nombre del tag
    if tag:
        query = query.join(BD.Cita.tags).filter(BD.Tag.Nombre.ilike(f"%{tag}%"))

    # Filtro por contenido de la cita
    if search:
        query = query.filter(BD.Cita.texto.ilike(f"%{search}%"))

    citas = query.all()

    results = []
    for cita in citas:
        results.append({
            "texto": cita.texto,
            "autor": cita.autor.name if cita.autor else None,
            "tags": [t.Nombre for t in cita.tags]
        })

    return JSONResponse(content=results)

@app.get("/scrape")
def trigger_scraping():
    scrape()
    return {"message": "Scraping completed"}
