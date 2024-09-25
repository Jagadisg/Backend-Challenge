SELECT student_id, COUNT(*) AS graded_assignments
FROM assignments
WHERE state = 'GRADED' AND student_id = 1
GROUP BY student_id;
