-- SELECT query examples for HR schema

-- Select all employees
SELECT * FROM employees;

-- Select specific columns
SELECT first_name, last_name, salary FROM employees;

-- Select employees with salary greater than 10000
SELECT * FROM employees WHERE salary > 10000;

-- Select employees hired after 1995
SELECT * FROM employees WHERE hire_date > '1995-01-01';

-- Select all departments
SELECT * FROM departments;

-- Select all jobs
SELECT * FROM jobs;

-- Select all dependents
SELECT * FROM dependents;
