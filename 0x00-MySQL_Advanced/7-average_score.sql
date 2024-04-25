-- 7-average_score.sql

-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
-- Note: An average score can be a decimal
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER |
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score INT;
    SELECT (SUM(score) / COUNT(project_id)) INTO avg_score FROM corrections
        WHERE corrections.user_id = user_id;
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END|
DELIMITER ;
