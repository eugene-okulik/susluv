import mysql.connector as mysql
import os
import csv
import dotenv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)


def is_in_db(row):
    select_query = f'''
            SELECT s.name, s.second_name, g.title as group_title, b.title as book_title, sj.title as subject_title,
            l.title as lesson_title, m.value as mark_value
            FROM students s
            JOIN `groups` g on g.id = s.group_id
            JOIN books b on b.taken_by_student_id = s.id
            JOIN marks m on s.id = m.student_id
            LEFT JOIN lessons l on m.lesson_id = l.id
            LEFT JOIN subjects sj on l.subject_id = sj.id
            WHERE name = '{row['name']}' AND second_name = '{row['second_name']}' AND g.title = '{row['group_title']}'
            AND b.title = '{row['book_title']}' AND sj.title = '{row['subject_title']}'
            AND l.title = '{row['lesson_title']}' AND m.value = '{row['mark_value']}'
        '''
    cursor.execute(select_query)
    return cursor.fetchone() is not None


homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(file_path, 'r', encoding='utf-8') as csv_file:
    file_data = csv.DictReader(csv_file)
    for row in file_data:
        if not is_in_db(row):
            print(row)
