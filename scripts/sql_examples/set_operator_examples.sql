-- Set operator examples for HR schema

-- Employees with salary > 15000 or hired after 1999
SELECT employee_id, first_name, last_name FROM employees WHERE salary > 15000
UNION
SELECT employee_id, first_name, last_name FROM employees WHERE hire_date > '1999-01-01';

-- Employees in department 10
SELECT employee_id, first_name, last_name FROM employees WHERE department_id = 10
INTERSECT
SELECT employee_id, first_name, last_name FROM employees WHERE salary > 8000;

-- Employees in department 10 but not with salary > 8000
SELECT employee_id, first_name, last_name FROM employees WHERE department_id = 10
EXCEPT
SELECT employee_id, first_name, last_name FROM employees WHERE salary > 8000;
