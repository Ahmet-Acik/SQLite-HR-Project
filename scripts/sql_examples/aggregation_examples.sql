-- Aggregation and function examples for HR schema

-- Count of employees
SELECT COUNT(*) AS total_employees FROM employees;

-- Average salary by department
SELECT department_id, AVG(salary) AS avg_salary FROM employees GROUP BY department_id;

-- Maximum and minimum salary
SELECT MAX(salary) AS max_salary, MIN(salary) AS min_salary FROM employees;

-- Total dependents per employee
SELECT employee_id, COUNT(*) AS num_dependents FROM dependents GROUP BY employee_id;

-- Employees with salary rounded to nearest thousand
SELECT first_name, last_name, ROUND(salary, -3) AS rounded_salary FROM employees;

-- Departments with more than 2 employees
SELECT department_id, COUNT(*) AS num_employees FROM employees GROUP BY department_id HAVING COUNT(*) > 2;
