-- There is a database containing the marks of some students in various subjects. The data may contain any number of subjects for a student.
-- Retrieve the records of students who have a sum of marks greater than or equal to 500. The result should be in the following format: student_id, sum_of_marks
-- sorted descending by student_id.


-- SQL query:
-- SELECT student_id, SUM(marks) AS sum_of_marks
-- FROM marks
-- GROUP BY student_id
-- HAVING SUM(marks) >= 500
-- ORDER BY student_id DESC;


-- SQL query:
-- 