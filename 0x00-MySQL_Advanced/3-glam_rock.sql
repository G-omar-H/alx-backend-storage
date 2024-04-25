-- 3-glam_rock.sql

-- Calculate lifespan using formed and split attributes
SELECT band_name,
       (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;
