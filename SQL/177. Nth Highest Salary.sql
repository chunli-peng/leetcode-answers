/*
 Approach 1: Single Table Query
 */
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT BEGIN
SET N := N -1;
-- LIMIT cannot accept expression
RETURN (
      # Write your MySQL query statement below.
      SELECT salary
      FROM employee
      GROUP BY salary
      ORDER BY salary DESC
      LIMIT N, 1
);
END
/*
 Approach 2: Subquery
 */
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT BEGIN RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT e.salary
      FROM employee AS e
      WHERE (
                  SELECT COUNT(DISTINCT salary)
                  FROM employee
                  WHERE salary > e.salary
            ) = N -1
);
END
/*
 Approach 2.2: Cartesian Product
 detail: similar to Approach 2: Subquery
 */
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT BEGIN RETURN (
      # Write your MySQL query statement below.
      SELECT e1.salary
      FROM employee AS e1,
            employee AS e2
      WHERE e1.salary <= e2.salary
      GROUP BY e1.salary
      HAVING COUNT(DISTINCT e2.salary) = N
);
END
/*
 Approach 3: Window Function
 */
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT BEGIN RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT salary
      FROM (
                  SELECT salary,
                        DENSE_RANK() over(
                              ORDER BY salary DESC
                        ) AS rnk
                  FROM employee
            ) AS tmp
      WHERE rnk = N
);
END