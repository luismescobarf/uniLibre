-- Intro SQL Caso Productos
-- Create Table, Alter Table

--Tiempo_Activo DATETIME GENERATED ALWAYS AS ( datetime('2022-01-01') - Anio_Constitucion ),        
CREATE TABLE Proveedor (    
    ID_Proveedor INTEGER NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Direccion VARCHAR(11),
    Anio_Constitucion DATETIME NOT NULL,    
    NIT VARCHAR(11) NOT NULL,
    PRIMARY KEY(ID_Proveedor)    
);

CREATE TABLE Producto (
    ID_Producto INTEGER NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Precio_Unitario REAL NOT NULL,
    Codigo VARCHAR(10) NOT NULL,
    ID_Proveedor INTEGER,    
    PRIMARY KEY (ID_Producto),
    FOREIGN KEY (ID_Proveedor) REFERENCES Proveedor(ID_Proveedor)
);

-- Crear proveedores
