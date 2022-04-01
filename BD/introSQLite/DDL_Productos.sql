-- Intro SQL Caso Productos
-- Create Table, Alter Table

        
CREATE TABLE Proveedor (    
    ID_Proveedor INTEGER PRIMARY KEY NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Direccion VARCHAR(11),
    Anio_Constitucion DATETIME NOT NULL,    
    NIT VARCHAR(11) NOT NULL,
    Tiempo_Activo DATETIME GENERATED ALWAYS AS ( datetime('2022-01-01') - Anio_Constitucion )    
);

CREATE TABLE Producto (
    ID_Producto INTEGER PRIMARY KEY NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Precio_Unitario REAL NOT NULL,
    Codigo VARCHAR(10) NOT NULL,
    ID_Proveedor INTEGER,        
    IVA REAL GENERATED ALWAYS AS ( Precio_Unitario * 0.19 ),    
    FOREIGN KEY (ID_Proveedor) REFERENCES Proveedor(ID_Proveedor)
);



        
-- CREATE TABLE Proveedor (    
--     ID_Proveedor INTEGER PRIMARY KEY NOT NULL,
--     Nombre VARCHAR(50) NOT NULL,
--     Direccion VARCHAR(11),
--     Anio_Constitucion DATETIME NOT NULL,    
--     NIT VARCHAR(11) NOT NULL,
--     Tiempo_Activo DATETIME GENERATED ALWAYS AS ( datetime('2022-01-01') - Anio_Constitucion )
-- );



-- Crear proveedores
INSERT INTO Proveedor (Nombre,Anio_Constitucion,NIT) VALUES ('La14','1998-10-10','1234-5');
INSERT INTO Proveedor (ID_Proveedor,Nombre,Anio_Constitucion,NIT) VALUES (89,'Varios','1988-10-10','1554-5');
INSERT INTO Proveedor (ID_Proveedor,Nombre,Anio_Constitucion,NIT) VALUES (89,'Globo','2004-10-10','7777');


-- Crear productos
INSERT INTO Producto () VALUES ();
INSERT INTO Producto    (Nombre,Precio_Unitario,Codigo,ID_Proveedor) 
VALUES                  ('CocaCola',2500,'CCAR',1);