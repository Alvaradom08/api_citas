
-- Crear base de datos (si no existe)
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'CITASBD')
BEGIN
    CREATE DATABASE CITASBD;
END
GO

USE CITASBD;
GO

-- Crear tablas
IF OBJECT_ID('citasTag', 'U') IS NOT NULL DROP TABLE citasTag;
IF OBJECT_ID('citas', 'U') IS NOT NULL DROP TABLE citas;
IF OBJECT_ID('tags', 'U') IS NOT NULL DROP TABLE tags;
IF OBJECT_ID('autores', 'U') IS NOT NULL DROP TABLE autores;
GO

CREATE TABLE autores (
    idAutor INT PRIMARY KEY IDENTITY,
    nombre VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE tags (
    idTag INT PRIMARY KEY IDENTITY,
    Nombre VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE citas (
    id INT PRIMARY KEY IDENTITY,
    texto VARCHAR(MAX) NOT NULL,
    idAutor INT FOREIGN KEY REFERENCES autores(idAutor)
);

CREATE TABLE citasTag (
    idCitaTag INT FOREIGN KEY REFERENCES citas(id),
    tagId INT FOREIGN KEY REFERENCES tags(idTag),
    PRIMARY KEY (idCitaTag, tagId)
);
