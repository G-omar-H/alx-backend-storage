--  0-uniq_users.sql
-- QL script that creates a table users following these requirements:
--
--    With these attributes:
--        id, integer, never null, auto increment and primary key
--        email, string (255 characters), never null and unique
--        name, string (255 characters)
--   If the table already exists, the  script should not fail
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email CHAR(255) NOT NULL UNIQUE,
    name CHAR(255)
)
