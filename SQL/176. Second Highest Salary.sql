# Write your MySQL query statement below.
/*
 Approach 1: Subquery + Limit
 */
SELECT (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET 1
    ) AS SecondHighestSalary;
/*
 Approach 2: IFNULL + Limit
 */
SELECT IFNULL(
        (
            SELECT DISTINCT salary
            FROM Employee
            ORDER BY salary DESC
            LIMIT 1 OFFSET 1
        ),
        NULL
    ) AS SecondHighestSalary;