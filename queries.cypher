
//NOT ACTUAL QUERIES THESE ARE ROUGH DRAFT
MATCH (s:Song)
WHERE (s.spotifyUrl IS NOT NULL)
RETURN count(s) AS TotalSongs



MATCH (s:Song)
RETURN count(s) AS TotalSongs

MATCH (s:Song)
RETURN count(DISTINCT s.title) AS UniqueTitleCount

MATCH (s:Song)
WHERE (s.spotifyURL IS NOT NULL) OR (s.lastFmUrl IS NOT NULL)
WITH s.title AS Title, count(s) AS Count
WHERE Count > 1
RETURN Title, Count

MATCH (s:Song)
DETACH DELETE s

MATCH (s:Song)
WHERE toLower(s.genre) CONTAINS toLower('Pop')
RETURN s

MATCH (s:Song)
WHERE toLower(s.artist) CONTAINS toLower('sabrina carpenter')
RETURN count(s) AS number_of_songs

MATCH (s:Song)
WHERE s.popularityScore IS NOT NULL
RETURN s.title AS Title, s.popularityScore AS PopularityScore
ORDER BY s.popularityScore DESC
LIMIT 10;

MATCH (s:Song)
RETURN s.genre AS Genre, count(s) AS NumberOfSongs
ORDER BY NumberOfSongs;

CALL db.index.fulltext.createNodeIndex("indexName", ["Label"], ["property"])

CALL dbms.components()




