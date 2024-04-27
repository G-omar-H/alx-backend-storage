-- 101-average_weighted_score.sql

-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes
-- and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
   UPDATE users
   JOIN (
    SELECT user_id, SUM(corrections.score * projects.weight) / SUM(projects.weight) AS weighted_average
    FROM corrections 
    JOIN projects ON projects.id = corrections.project_id
    GROUP BY user_id
   ) AS weighted_average ON users.id = weighted_average.user_id
   SET users.average_score = weighted_average.weighted_average;
END |
DELIMITER ;
