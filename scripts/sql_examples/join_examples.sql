-- JOIN query examples for HR schema

-- Employees with their department names
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- Employees with their job titles
SELECT e.first_name, e.last_name, j.job_title
FROM employees e
JOIN jobs j ON e.job_id = j.job_id;

-- Employees with their manager's name
SELECT e.first_name AS employee_first, e.last_name AS employee_last,
       m.first_name AS manager_first, m.last_name AS manager_last
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id;

-- Departments and their locations
SELECT d.department_name, l.city, l.country_id
FROM departments d
JOIN locations l ON d.location_id = l.location_id;

-- Locations with country and region
SELECT l.city, c.country_name, r.region_name
FROM locations l
JOIN countries c ON l.country_id = c.country_id
JOIN regions r ON c.region_id = r.region_id;
