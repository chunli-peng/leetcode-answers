# Write your MySQL query statement below
/*
 Approach 1: Subquery
 */
SELECT s.score,
    (
        SELECT COUNT(DISTINCT score)
        FROM Scores
        WHERE score >= s.score
    ) AS 'rank'
FROM Scores AS s
ORDER BY s.score DESC;
/*
 Approach 1.2: Cartesian Product
 detail: similar to Approach 1: Subquery
 */
SELECT s1.score,
    COUNT(DISTINCT s2.score) as 'rank'
FROM Scores AS s1,
    Scores AS s2
WHERE s1.score <= s2.score
GROUP BY s1.id
ORDER BY s1.score DESC;
/*
 Approach 2: Window Function
 */
SELECT score,
    DENSE_RANK() OVER(
        ORDER BY score DESC
    ) AS 'rank'
FROM Scores