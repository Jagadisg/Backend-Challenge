SELECT teacher_id, COUNT(*) AS grade_a_assignments
FROM assignments
WHERE grade = 'A'
GROUP BY teacher_id;
