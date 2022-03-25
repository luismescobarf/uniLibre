-- Requerimiento -> Generar los correos electrónicos de los líderes

-- 1) Primera letra en minúscula del nombre
-- 2) Punto
-- 3) Segundo apellido en minúscula
-- 4) El ID_Lider
-- 5) Dominio de la empresa @cons.com.co

SELECT  LOWER(SUBSTR(l.Nombre,1,1)) 
        || '.'
        || LOWER(l.Segundo_Apellido) 
        || l.ID_Lider
        || '@cons.com.co' as email_lider
        l.Nombre,
        l.Segundo_Apellido,
        l.ID_Lider
FROM Lider l;
