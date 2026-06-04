-- Schema SQL MedSOS

CREATE TABLE Usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tipo TEXT CHECK(tipo IN ('Doador', 'Instituicao')),
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE Medicamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    validade DATE,
    doador_id INTEGER,
    FOREIGN KEY(doador_id) REFERENCES Usuarios(id)
);

CREATE TABLE Demandas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    regiao TEXT NOT NULL,
    instituicao_id INTEGER,
    FOREIGN KEY(instituicao_id) REFERENCES Usuarios(id)
);
