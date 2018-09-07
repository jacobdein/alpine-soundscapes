-- Compute the average D2N for each recording site within a range of radii (50, 100, 200, 500)
SELECT
	id,
	name,
	MAX(CASE WHEN radius = 50 THEN d2n ELSE NULL END) AS d2n_50m,
	MAX(CASE WHEN radius = 100 THEN d2n ELSE NULL END) AS d2n_100m,
	MAX(CASE WHEN radius = 200 THEN d2n ELSE NULL END) AS d2n_200m,
	MAX(CASE WHEN radius = 500 THEN d2n ELSE NULL END) AS d2n_500m
	FROM
		(SELECT
		s.id,
		s.name,
		SUM(d2n*ST_Area(s.geom)) / ST_Area(ST_Buffer(ST_GeomFromEWKT('SRID=31264;POINT(0 0)'), s.radius)) AS d2n,
		radius
		FROM site_d2n AS s
		GROUP BY s.id, s.name, s.radius) AS long
	GROUP BY id, name
ORDER BY id;
