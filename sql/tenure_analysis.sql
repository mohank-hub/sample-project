-- Employees grouped by tenure band
-- Helps identify experienced vs new joiners for retention analysis

SELECT
    CASE
        WHEN tenure_years >= 7 THEN 'Senior (7+ yrs)'
        WHEN tenure_years >= 4 THEN 'Mid (4-6 yrs)'
        ELSE 'Junior (<4 yrs)'
    END AS tenure_band,
    COUNT(*) AS employee_count,
    ROUND(AVG(salary), 2) AS avg_salary
FROM employees
GROUP BY tenure_band
ORDER BY avg_salary DESC;