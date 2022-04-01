-- Probar conexión
SELECT *
FROM Lider;

--Obtener la edad promedio de los líderes
-- Funciones de agregación: AVG, COUNT, SUM, MAX, MIN

-- Obtener la edad de los líderes
SELECT DATETIME('now') - Fecha_Nacimiento as Edad
FROM Lider;

-- Requerimiento completo
SELECT AVG(DATETIME('now') - Fecha_Nacimiento) as Edad_Promedio
FROM Lider;

-- Ampliar información de los proyectos (agregando info tipo) -> JOIN
SELECT * FROM Proyecto p
JOIN Tipo t ON p.ID_Tipo = t.ID_Tipo;

-- Ampliar información de los proyectos (agregando tipo, líderes) -> JOIN
SELECT  l.ID_Lider,
        l.Nombre,
        l.Cargo,
        p.ID_Proyecto,
        p.Clasificacion,
        p.Banco_Vinculado,
        t.Area_Max,
        t.Estrato,
        t.Financiable
FROM Proyecto p
JOIN Tipo t ON p.ID_Tipo = t.ID_Tipo
JOIN Lider l ON p.ID_Lider = l.ID_Lider;

-- (Ejemplo de agrupamiento y ordenamiento)
-- Cuántos proyectos tiene cada líder?
-- Presentar el listado ordernado de
-- mayor a menor (desde el que tiene a cargo más proyectos)






