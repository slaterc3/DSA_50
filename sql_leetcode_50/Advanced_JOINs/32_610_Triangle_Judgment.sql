SELECT 
    *,
    CASE 
        WHEN (x+y>z AND x+z>y AND y+z>x) THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;

-- SELECT 
--     t1.*,
--     CASE 
--         WHEN (t1.x + t1.y + t1.z - t2.biggest) > t2.biggest THEN 'Yes'
--         ELSE 'No'
--     END AS triangle
-- FROM Triangle t1
-- INNER JOIN 
-- (SELECT *,
--     CASE
--         WHEN x > y AND x > z THEN x
--         WHEN y > x AND y > z THEN y
--         ELSE z
--     END as biggest
-- FROM Triangle) t2
--     ON t1.x = t2.x;


-- Table: Triangle

-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | x           | int  |
-- | y           | int  |
-- | z           | int  |
-- +-------------+------+
-- In SQL, (x, y, z) is the primary key column for this table.
-- Each row of this table contains the lengths of three line segments.
 

-- Report for every three line segments whether they can form a triangle.

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Triangle table:
-- +----+----+----+
-- | x  | y  | z  |
-- +----+----+----+
-- | 13 | 15 | 30 |
-- | 10 | 20 | 15 |
-- +----+----+----+
-- Output: 
-- +----+----+----+----------+
-- | x  | y  | z  | triangle |
-- +----+----+----+----------+
-- | 13 | 15 | 30 | No       |
-- | 10 | 20 | 15 | Yes      |
-- +----+----+----+----------+