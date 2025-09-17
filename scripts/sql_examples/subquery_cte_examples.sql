-- Subquery and CTE examples for HR schema

-- Employees with above average salary (subquery)
SELECT first_name, last_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Departments with more than 2 employees (subquery in FROM)
SELECT d.department_name, emp_count
FROM departments d
JOIN (
    SELECT department_id, COUNT(*) AS emp_count
    FROM employees
    GROUP BY department_id
) ec ON d.department_id = ec.department_id
WHERE emp_count > 2;

-- CTE: Employees and their manager names
WITH emp_mgr AS (
    SELECT e.employee_id, e.first_name AS emp_first, e.last_name AS emp_last,
           m.first_name AS mgr_first, m.last_name AS mgr_last
    FROM employees e
    LEFT JOIN employees m ON e.manager_id = m.employee_id
)
SELECT * FROM emp_mgr;
