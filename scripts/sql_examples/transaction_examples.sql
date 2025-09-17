-- Transaction examples for HR schema

-- Start a transaction, update salary, and rollback
BEGIN TRANSACTION;
UPDATE employees SET salary = salary + 1000 WHERE employee_id = 100;
ROLLBACK;

-- Start a transaction, insert a new department, and commit
BEGIN TRANSACTION;
INSERT INTO departments (department_name, location_id) VALUES ('Research', 1400);
COMMIT;
