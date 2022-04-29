-----------------------
-- Taller Segundo Corte
-----------------------
-- 1. ¿Cuáles son las 3 enfermedades más comunes que presentan los árboles?

SELECT 
    e.Nombre,
    COUNT(*) as Numero_Arboles_Infectados
FROM Enfermedad e
JOIN Diagnostico d on e.ID_Enfermedad = d.ID_Enfermedad
GROUP BY d.ID_Enfermedad
ORDER BY  Numero_Arboles_Infectados DESC
LIMIT 3;

-- 2. ¿Cuál es el árbol que más se ha enfermado en la producción?

SELECT
    d.ID_Arbol,
    COUNT(*) as Numero_Infecciones
FROM Diagnostico d
GROUP BY d.ID_Arbol
ORDER BY Numero_Infecciones DESC
LIMIT 1;

-- 3. ¿Cuál es el árbol que menos se ha fumigado?

SELECT 
    f.ID_Arbol,
    COUNT(*) NumeroFumigaciones
FROM Fumiga f
GROUP BY f.ID_Arbol
ORDER BY NumeroFumigaciones
LIMIT 1;

SELECT 
    f.ID_Arbol,
    COUNT(*) NumeroFumigaciones
FROM Fumiga f
GROUP BY f.ID_Arbol
HAVING NumeroFumigaciones IN (
    SELECT         
        COUNT(*) NumeroFumigaciones
    FROM Fumiga f
    GROUP BY f.ID_Arbol    
    ORDER BY NumeroFumigaciones
    LIMIT 1
)
ORDER BY NumeroFumigaciones;

-- 4. ¿Quién es el trabajador que tiene el mayor número de recolectas?

SELECT 
    t.ID_Trabajador,
    t.Nombre,
    COUNT(*) as NumeroRecolectas
FROM Trabajador t
JOIN Recolecta r ON t.ID_Trabajador = r.ID_Trabajador
GROUP BY r.ID_Trabajador
ORDER BY NumeroRecolectas DESC
LIMIT 1;

-- 5. Listado de los árboles rankeados por su producción de mayor a menor (peso de las recolectas que le han realizado).
-- 6. Las producciones rankeadas de mayor a menor por la proporción entre el peso acumulado de esta y el número de recolectas asociadas.
-- 7. ¿De qué calidad de aguacates se ha producido más?
-- 8. Detalle de cuánto ha producido cada árbol de cada calidad, mostrando de qué calidad produjo más y de qué calidad produjo menos.
-- 9. Los 4 meses del año donde más enfermedades se diagnostican.
-- 10. Los 10 árboles menos productivos que más se han enfermado.




















