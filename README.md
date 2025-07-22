# 📚 API de Citas - Extracción y Exposición de Datos

Autor: **Miguel Alvarado**  
Repositorio: [https://github.com/Alvaradom08/api_citas](https://github.com/Alvaradom08/api_citas)

---

## 🎯 Objetivo General

Automatizar la extracción de información del sitio [https://quotes.toscrape.com](https://quotes.toscrape.com), almacenarla en una base de datos relacional y exponerla mediante una API REST con filtros.

---

## 🌐 Sitio Objetivo

[https://quotes.toscrape.com](https://quotes.toscrape.com)

---

## 🧱 Requisitos Funcionales

### 1. 🔍 Scraping

- Se extraen: **texto de la cita**, **autor**, y **etiquetas**.
- El scraping se ejecuta desde el script `scraping.py`.

### 2. 💾 Persistencia (SQL Server)

- Los datos se almacenan en una base de datos SQL Server.
- Se evita la duplicación de autores, citas y etiquetas.
- Se modela la relación N:N entre citas y etiquetas con SQLAlchemy.

### 3. 🧭 API REST

**Endpoints disponibles:**

- `GET /quotes` → todas las citas
- `GET /quotes?author=...` → filtra por autor
- `GET /quotes?tag=...` → filtra por etiqueta
- `GET /quotes?search=...` → búsqueda libre en el contenido

> Los filtros pueden combinarse. La API responde en formato JSON.

---

## 💻 Tecnologías Usadas

- Python 3
- FastAPI
- SQLAlchemy
- SQL Server
- BeautifulSoup + Requests (scraping)
- Uvicorn (servidor ASGI)
- [pyodbc](https://github.com/mkleehammer/pyodbc) (driver para conexión a SQL Server)

---

## ⚙ Instalación y Ejecución

### 1. Clonar el repositorio

git clone https://github.com/Alvaradom08/api_citas.git
cd api_citas

### 2. Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

### 3. Instalar dependencias
pip install -r requirements.txt

### 4. Configurar conexión a SQL Server
Crea un archivo .env en el directorio raíz con el siguiente contenido:
- DATABASE_URL=mssql+pyodbc://USUARIO:CONTRASEÑA@SERVIDOR/NOMBRE_BD?driver=ODBC+Driver+17+for+SQL+Server

### 5. Ejecutar el scraping (crear DB y llenar datos)
python scraping.py

### 6. Levantar el servidor FastAPI

uvicorn main:app --reload

## Estructura del Proyecto
api_citas/
├── BD.py                # Modelos SQLAlchemy
├── crud.py              # Operaciones DB
├── estructura.py        # Esquemas Pydantic
├── main.py              # FastAPI con filtros
├── scraping.py          # Script de scraping
├── requirements.txt     # Dependencias
├── .env                 # Config opcional

## Comandos útiles (Linux)
### Activar entorno virtual
source venv/bin/activate

### Ejecutar scraping
python scraping.py

### Iniciar la API
uvicorn main:app --reload
