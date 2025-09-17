-- Data modification examples for HR schema

-- Insert a new employee
INSERT INTO employees (first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id)
VALUES ('Jane', 'Doe', 'jane.doe@sqltutorial.org', '555.123.4567', '2025-09-17', 1, 5000.00, 100, 1);

-- Update salary for an employee
UPDATE employees SET salary = salary * 1.1 WHERE employee_id = 100;

-- Delete a dependent
DELETE FROM dependents WHERE dependent_id = 1;
