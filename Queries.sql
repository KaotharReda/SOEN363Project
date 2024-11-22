SELECT * 
FROM Songs 
WHERE genre = 'Pop'


SELECT artist, COUNT(*) 
FROM Songs 
GROUP BY artist

SELECT genre, COUNT(*)
FROM Songs
GROUP BY genre
HAVING rank<=5




