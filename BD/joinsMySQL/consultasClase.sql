-- Obtener todos los usuarios y los posts, 
-- tengan o no tengan asociación

-- Todos los usuarios y todas las publicaciones sin 
--importar si han realizado publicaciones,
--o si las publicaciones no tienen usuario

-- Todos los usuarios incluyendo los que no han publicado nada
SELECT *
FROM usuarios u
LEFT JOIN posts p ON u.id = p.usuario_id;

-- Todas las publicaciones incluyendo aquellas que no tienen usuario
SELECT *
FROM usuarios u
RIGHT JOIN posts p ON u.id = p.usuario_id;


-- Completo
SELECT *
FROM usuarios u
LEFT JOIN posts p ON u.id = p.usuario_id
UNION
SELECT *
FROM usuarios u
RIGHT JOIN posts p ON u.id = p.usuario_id;


-- Obtener todos los usuarios y posts que no tienen ninguna asociación
SELECT *
FROM usuarios u
LEFT JOIN posts p ON u.id = p.usuario_id
WHERE p.usuario_id IS NULL
UNION
SELECT *
FROM usuarios u
RIGHT JOIN posts p ON u.id = p.usuario_id
WHERE u.id IS NULL;


-- Cuántas y cuáles etiquetas tiene cada post
-- mostrar los posts especificando el título

SELECT  p.titulo,
        COUNT(*) as NumeroPosts,
        GROUP_CONCAT(e.nombre_etiqueta) DetalleEtiquetas,
        GROUP_CONCAT(e.id) IDS_Tags
FROM posts p
JOIN posts_etiquetas pe ON p.id = pe.post_id
JOIN etiquetas e ON pe.etiqueta_id = e.id
GROUP BY p.id
ORDER BY NumeroPosts DESC;

-- Obtener las categorías de los posts y ordernalas
--por aquellas que tengan más publicaciones. Presentar
-- el detalle de las publicaciones (id, titulo)

SELECT 
COUNT(*) as NumeroPosts, e.nombre_etiqueta, 
e.id, GROUP_CONCAT(p.titulo) Titulos, 
GROUP_CONCAT(p.id) IDs
FROM posts p 
JOIN posts_etiquetas pe ON p.id=pe.post_id
JOIN etiquetas e ON pe.etiqueta_id = e.id
GROUP BY e.id 
ORDER BY NumeroPosts DESC;

SELECT 
COUNT(*) as NumeroPosts, c.nombre_categoria, 
c.id, GROUP_CONCAT(p.titulo) Titulos, 
GROUP_CONCAT(p.id) IDs
FROM posts p 
JOIN categorias c ON p.categoria_id=c.id
GROUP BY c.id 
ORDER BY NumeroPosts DESC;












