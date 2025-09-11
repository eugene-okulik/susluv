import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl')

cursor = db.cursor(dictionary=True)

# создаём студента
cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('Oleh-S', 'Oleshko-S', null)")
student_id = cursor.lastrowid
db.commit()

# создаём книги
insert_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query, [
        ('50 shades of Grey', student_id),
        ('The Lord of the Rings', student_id)
    ])
db.commit()

# создаём группу
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('1-A-S', 'sept 2025', 'may 2026')")
group_id = cursor.lastrowid
db.commit()

# помещаем студента в созданную группу
cursor.execute(f"UPDATE students SET group_id = {group_id} WHERE id = {student_id}")
db.commit()

# создаём предметы
insert_query = "INSERT INTO subjects (title) VALUES (%s)"
cursor.execute(insert_query, ('Math-S',))
subject_ids = [cursor.lastrowid]
cursor.execute(insert_query, ('Biology-S',))
subject_ids.append(cursor.lastrowid)
cursor.execute(insert_query, ('Chemistry-S',))
subject_ids.append(cursor.lastrowid)
db.commit()

# создаём занятия
insert_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
lesson_ids = []
for subject in subject_ids:
    cursor.execute(insert_query, ('monday', subject))
    lesson_ids.append(cursor.lastrowid)
    cursor.execute(insert_query, ('tuesday', subject))
    lesson_ids.append(cursor.lastrowid)
db.commit()

# выставляем оценки
insert_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
seq_params = []
for lesson in lesson_ids:
    seq_params.append(('5', lesson, student_id))
cursor.executemany(insert_query, seq_params)
db.commit()

# получаем книги нашего студента
cursor.execute(f'SELECT title FROM books WHERE taken_by_student_id = {student_id}')
print(cursor.fetchall())

# получаем оценки нашего студента
cursor.execute(f'SELECT value FROM marks WHERE student_id = {student_id}')
print(cursor.fetchall())

# взламываем сервер пентагона жирным джойном
select_query = f'''
SELECT * 
FROM students s
JOIN `groups` g on g.id = s.group_id 
JOIN books b on b.taken_by_student_id = s.id 
JOIN marks m on s.id = m.student_id 
LEFT JOIN lessons l on m.lesson_id = l.id  
LEFT JOIN subjects sj on l.subject_id = sj.id 
WHERE s.id = {student_id}
'''
cursor.execute(select_query)
print(cursor.fetchall())

db.close()
