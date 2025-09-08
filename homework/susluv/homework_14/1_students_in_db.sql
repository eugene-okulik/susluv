INSERT INTO students (name, second_name, group_id) VALUES ('Oleh-S', 'Oleshko-S', null);

INSERT INTO books
(title, taken_by_student_id)
VALUES
('50 shades of Grey', 21179),
('The Lord of the Rings', 21179);

INSERT INTO `groups`
(title, start_date, end_date)
VALUES('1-A-S', 'sept 2025', 'may 2026');

UPDATE students SET group_id =
(SELECT id FROM `groups` where title = '1-A-S')
WHERE name = 'Oleh-S' AND second_name = 'Oleshko-S'

INSERT INTO subjects
(title)
VALUES
('Math-S'),
('Biology-S'),
('Chemistry-S');

INSERT INTO lessons
(title, subject_id)
VALUES
('monday', 12038),
('tuesday', 12038),
('monday', 12039),
('tuesday', 12039),
('monday', 12040),
('tuesday', 12040);

INSERT INTO marks
(value, lesson_id, student_id)
VALUES
('5', 12297, 21179),
('5', 12298, 21179),
('5', 12299, 21179),
('5', 12300, 21179),
('5', 12301, 21179),
('5', 12302, 21179);

SELECT title FROM books WHERE taken_by_student_id =
(SELECT id FROM students WHERE name = 'Oleh-S' AND second_name = 'Oleshko-S');

SELECT value FROM marks WHERE student_id =
(SELECT id FROM students WHERE name = 'Oleh-S' AND second_name = 'Oleshko-S');

SELECT *
FROM students s
JOIN `groups` g on g.id = s.group_id
JOIN books b on b.taken_by_student_id = s.id
JOIN marks m on s.id = m.student_id
LEFT JOIN lessons l on m.lesson_id = l.id
LEFT JOIN subjects sj on l.subject_id = sj.id
WHERE name = 'Oleh-S' AND second_name = 'Oleshko-S'

