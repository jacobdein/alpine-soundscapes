--Insert the intersection of rast_d2n with buffers of a range of radii (50, 100, 200, 500) around recording sites into the site_d2n table.
INSERT INTO site_d2n (id, name, d2n, geom, radius)
SELECT id, name, (gval).val as d2n, ST_Multi((gval).geom) as geom, radius
FROM (
	SELECT ST_Intersection(r.rast, b.geom) as gval, b.id, b.name, b.radius
	FROM rast_d2n as r
	JOIN (
		SELECT ST_Buffer(s.geometry, (r.radius).n) as geom, s.id, s.name, (r.radius).n as radius
		FROM database_site as s
		CROSS JOIN (SELECT radius FROM (VALUES (50), (100), (200), (500)) as radius(n)) as r
	) as b
	ON ST_Intersects(r.rast, b.geom)
) as intersection;
