-- SQL script that creates a trigger that decreases
--the quantity of an item after adding a new order.
DROP TRIGGER IF EXISTS store;
DELIMITER |
CREATE TRIGGER store AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  UPDATE items SET quantity = quantity - (NEW.number * 1) WHERE items.name = NEW.item_name;
END;|
