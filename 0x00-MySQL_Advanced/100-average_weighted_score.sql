-- 100-average_weighted_score.sql

--  SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes
-- and store the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser ;
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE average_weighted_score FLOAT;
    SELECT SUM(corrections.score * (projects.weight )) / SUM(projects.weight) INTO average_weighted_score FROM  corrections join projects ON projects.id = project_id WHERE corrections.user_id = user_id;
    UPDATE users  SET average_score = average_weighted_score   WHERE id = user_id;
END|
DELIMITER ;
