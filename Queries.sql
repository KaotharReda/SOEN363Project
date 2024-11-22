SELECT * 
FROM Songs 
WHERE genre = 'Pop'


SELECT artist, COUNT(*) 
FROM Songs 
GROUP BY artist

SELECT artist, COUNT(*) 
FROM Songs GROUP BY artist 
HAVING COUNT(*) > 5;





