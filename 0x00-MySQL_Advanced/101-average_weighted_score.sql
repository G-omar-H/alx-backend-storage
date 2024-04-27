-- 101-average_weighted_score.sql

-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes
-- and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER |

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT;
    DECLARE average_weighted_score FLOAT;

    DECLARE done INT DEFAULT 0;
    -- Cursor to iterate over each user
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    -- Variable to control loop termination

    -- Open cursor
    OPEN user_cursor;

    -- Loop through each user
    user_loop: LOOP
        -- Fetch user ID
        FETCH user_cursor INTO user_id;
        IF done = 1 THEN
            LEAVE user_loop;
        END IF;

        -- Calculate average weighted score for the user
        SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight) INTO average_weighted_score
        FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

        -- Update users table with the calculated average weighted score
        UPDATE users SET average_score = average_weighted_score WHERE id = user_id;
    END LOOP;

    -- Close cursor
    CLOSE user_cursor;
END |

DELIMITER ;
