# 📚 API de Citas — Scraping y API REST

Repositorio oficial: [https://github.com/Alvaradom08/api_citas](https://github.com/Alvaradom08/api_citas)

## ✨ Descripción

Este proyecto automatiza el scraping del sitio [https://quotes.toscrape.com](https://quotes.toscrape.com), extrae citas con sus autores y etiquetas, las almacena en una base de datos relacional (SQL Server) y expone una API REST para consultarlas con filtros combinables.

---

## 🧱 Tecnologías

- 🐍 Python 3.11+
- 🕸️ BeautifulSoup + requests (Scraping)
- ⚡ FastAPI (API REST)
- 🛢️ SQL Server (Base de datos relacional)
- 🐘 SQLAlchemy (ORM)
- 📦 Uvicorn (Servidor ASGI)
- 📄 `.env` (para variables sensibles)

---

## 📂 Estructura del Proyecto

```
api_citas/
│
├──app
    ├── BD.py                # Modelos SQLAlchemy
    ├── CRUD.py              # Operaciones DB
    ├── estructura.py        # Esquemas Pydantic
    ├── API_Citas.py         # FastAPI con 
    ├── conexcionBD.py       # conexcion Base De datos (SQL Server)
    └── scraping.py          # Script de scraping
├── .env                     # Credenciales de conexión
├── requirements.txt         # Dependencias del proyecto
├── README.md                # Este archivo
└── SCRIPBDCITAS.sql         # Script para crear tablas en SQL Server
```

---

## ⚙️ Instalación y ejecución

### 🧰 Requisitos previos

- Python 3.11+
- SQL Server en ejecución local
- Git

---

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/Alvaradom08/api_citas.git
cd api_citas
```

### 2️⃣ Crear entorno virtual e instalar dependencias

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Configurar archivo `.env`

Crea un archivo `.env` en la raíz con tu conexión a SQL Server:

```env
SERVER=localhost
DATABASE=CITASBD
USERNAME=tu_usuario
PASSWORD=tu_contraseña
```

> El archivo ya está incluido como plantilla en el proyecto.

---

### 4️⃣ Crear base de datos y tablas

Abre SQL Server Management Studio y ejecuta el script:

```sql
  SCRIPBDCITAS.sql

-- Tablas: autores, tags, citas, citasTag (relación N:M)
...
```

---

### 5️⃣ Ejecutar scraping (opción manual)

```bash
python scraper.py
```

Esto extraerá todas las citas y las guardará en la base de datos, evitando duplicados.

---

### 6️⃣ Ejecutar la API

```bash
uvicorn main:app --reload
```

La API estará disponible en:  
📍 http://127.0.0.1:8000

---

## 🚀 Endpoints 

###  scraping
```
GET /scrape
```


### ✔️ Obtener todas las citas

```
GET /quotes
```

### 🔍 Filtrar por autor

```
GET /quotes?author=Albert Einstein
```

### 🔖 Filtrar por etiqueta

```
GET /quotes?tag=inspirational
```

### 📝 Búsqueda libre por contenido

```
GET /quotes?search=life
```

### 📌 Combinación de filtros

```
GET /quotes?author=Albert Einstein&tag=inspirational&search=truth
```

---

## 🧪 Ejemplos de uso con `curl`

```bash
curl "http://127.0.0.1:8000/quotes?tag=truth"
curl "http://127.0.0.1:8000/quotes?author=Albert%20Einstein"
curl "http://127.0.0.1:8000/quotes?search=change"
```

---

## 🐧 Comandos útiles en Linux

```bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar scraping
python scraper.py

# Iniciar API
uvicorn main:app --reload
```



## 👤 Autor

** Juan Mateo Alvarado Montoya**  
[https://github.com/Alvaradom08](https://github.com/Alvaradom08)

---

## 📄 Licencia

MIT License – Libre uso académico o personal.

---