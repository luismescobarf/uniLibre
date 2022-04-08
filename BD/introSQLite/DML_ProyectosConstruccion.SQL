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

SELECT  l.ID_Lider,
        l.Nombre,
        l.Cargo,
        COUNT(*) as Numero_Proyectos
FROM Proyecto p
JOIN Lider l ON p.ID_Lider = l.ID_Lider
GROUP BY l.ID_Lider
ORDER BY    Numero_Proyectos DESC,
            l.Nombre ASC,
            l.ID_Lider ASC;

-- El requerimiento anterior pero para los líderes cuyo cargo 
-- o es Coordinador o es Gerente

SELECT  l.ID_Lider,
        l.Nombre,
        l.Cargo,
        COUNT(*) as Numero_Proyectos
FROM Proyecto p
JOIN Lider l ON p.ID_Lider = l.ID_Lider
WHERE l.Cargo = 'Coordinador' OR l.Cargo = 'Gerente'
GROUP BY l.ID_Lider
ORDER BY    Numero_Proyectos DESC,
            l.Nombre ASC,
            l.ID_Lider ASC;

SELECT  l.ID_Lider,
        l.Nombre,
        l.Cargo,
        COUNT(*) as Numero_Proyectos
FROM Proyecto p
JOIN Lider l ON p.ID_Lider = l.ID_Lider
WHERE l.Cargo IN ('Coordinador', 'Gerente')
GROUP BY l.ID_Lider
ORDER BY    Numero_Proyectos DESC,
            l.Cargo ASC,
            l.Nombre ASC,
            l.ID_Lider ASC;

-- El mismo requerimiento pero para líderes que 
-- manejan entre 7 y 11 proyectos
SELECT  l.ID_Lider,
        l.Nombre,
        l.Cargo,
        COUNT(*) as Numero_Proyectos
FROM Proyecto p
JOIN Lider l ON p.ID_Lider = l.ID_Lider
WHERE   l.Cargo IN ('Coordinador', 'Gerente')
GROUP BY l.ID_Lider
HAVING Numero_Proyectos >= 7 AND Numero_Proyectos <=11        
ORDER BY    Numero_Proyectos DESC,
            l.Cargo ASC,
            l.Nombre ASC,
            l.ID_Lider ASC;

SELECT  l.ID_Lider,
        l.Nombre,
        l.Cargo,
        COUNT(*) as Numero_Proyectos
FROM Proyecto p
JOIN Lider l ON p.ID_Lider = l.ID_Lider
WHERE   l.Cargo IN ('Coordinador', 'Gerente')
GROUP BY l.ID_Lider
HAVING Numero_Proyectos BETWEEN 7 AND 11
ORDER BY    Numero_Proyectos DESC,
            l.Cargo ASC,
            l.Nombre ASC,
            l.ID_Lider ASC;


-- Proyectos con el serial terminado en las letras BP
SELECT p.Serial FROM Proyecto P;

SELECT  p.ID_Proyecto,
        p.Clasificacion,
        p.Serial
FROM Proyecto P
WHERE p.Serial LIKE '%BP';

-- Proyectos realizados en el año 2020
-- que sean de máximo estrato 3 y que tengan 
-- hasta 350 metros cuadrados
--strftime('%Y',Proyecto.Fecha_Inicio) = '2020'

select  p.ID_Proyecto,
        t.Estrato,
        t.Area_Max
from Proyecto p
join Tipo t on p.ID_Tipo = t.ID_Tipo
where strftime('%Y', p.Fecha_Inicio) = '2020'
and t.Estrato <= 3
and t.Area_Max <= 350;

-- Proyectos realizados en el año 2020
-- que sean de estrato 3 o menos y que estén en
-- ciudades diferentes a Bogotá y Pereira

select  p.ID_Proyecto,
        t.Estrato,
        t.Area_Max,
        p.Ciudad
from Proyecto p
join Tipo t on p.ID_Tipo = t.ID_Tipo
where strftime('%Y', p.Fecha_Inicio) = '2020'
and t.Estrato <= 3
and p.Ciudad NOT IN ('Pereira','Bogota')
LIMIT 10;

-- ¿Cuáles son los 10 proyectos ordenados de 
-- mayor a menor donde másdinero se ha invertido 
-- en compra de materiales?
SELECT 
    p.ID_Proyecto,
    p.Clasificacion,
    SUM(c.Cantidad * m.Precio_Unidad) as Gasto_Compras,
    p.Serial
FROM Proyecto p
JOIN Compra c ON 
p.ID_Proyecto = c.ID_Proyecto
JOIN MaterialConstruccion m ON 
c.ID_MaterialConstruccion = m.ID_MaterialConstruccion
GROUP BY p.ID_Proyecto
ORDER BY Gasto_Compras DESC
LIMIT 10;
















