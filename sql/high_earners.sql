-- Get employees earning more than 70000
-- Used to identify high earners across departments

SELECT
    emp_id,
    name,
    department,
    salary,
    bonus,
    total_compensation,
    join_year
FROM employees
WHERE salary > 70000
ORDER BY salary DESC;