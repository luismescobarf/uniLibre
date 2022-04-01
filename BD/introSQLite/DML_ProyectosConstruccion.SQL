SELECT *
FROM Lider;
--Obtener la edad promedio de los líderes

-- Obtener la edad de los líderes
SELECT DATETIME('now') - Fecha_Nacimiento as Edad
FROM Lider;

-- Requerimiento completo
SELECT AVG(DATETIME('now') - Fecha_Nacimiento) as Edad_Promedio
FROM Lider;