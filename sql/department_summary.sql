-- Department-level salary summary
-- Aggregates headcount, avg/min/max salary, and total compensation per department

SELECT
    department,
    COUNT(*) AS employee_count,
    ROUND(AVG(salary), 2) AS avg_salary,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary,
    SUM(total_compensation) AS total_dept_compensation
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;