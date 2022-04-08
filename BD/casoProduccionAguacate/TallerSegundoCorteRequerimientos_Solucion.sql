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
    COUNT(*) Numero_Infecciones
FROM Diagnostico d
GROUP





-- 3. ¿Cuál es el árbol que menos se ha fumigado?
-- 4. ¿Quién es el trabajador que tiene el mayor número de recolectas?
-- 5. Listado de los árboles rankeados por su producción de mayor a menor (peso de las recolectas que le han realizado).
-- 6. Las producciones rankeadas de mayor a menor por la proporción entre el peso acumulado de esta y el número de recolectas asociadas.
-- 7. ¿De qué calidad de aguacates se ha producido más?
-- 8. Detalle de cuánto ha producido cada árbol de cada calidad, mostrando de qué calidad produjo más y de qué calidad produjo menos.
-- 9. Los 4 meses del año donde más enfermedades se diagnostican.
-- 10. Los 10 árboles menos productivos que más se han enfermado.




















