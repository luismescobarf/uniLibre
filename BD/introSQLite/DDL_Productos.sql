-- Intro SQL Caso Productos
-- Create Table, Alter Table

CREATE TABLE Proveedor (
    PRIMARY KEY(ID_Proveedor),
    ID_Proveedor INTEGER NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Direccion VARCHAR(11),
    Anio_Constitucion DATETIME NOT NULL,
    Tiempo_Activo DATETIME GENERATED ALWAYS AS ( datetime('2022-01-01') - Anio_Constitucion )    
    NIT VARCHAR(11) NOT NULL,
    PRIMARY KEY(NIT)
);

CREATE TABLE Producto (
    ID_Producto INTEGER NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Precio_Unitario REAL NOT NULL,
    Codigo VARCHAR(10) NOT NULL,
    ID_Proveedor INTEGER,
    IVA REAL GENERATED ALWAYS AS (Precio_Unitario*0.19),
    PRIMARY KEY (ID_Producto),
    FOREIGN KEY (ID_Proveedor) REFERENCES Proveedor(ID_Proveedor)
);
