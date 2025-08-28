class Book:

    material = 'бумага'
    has_text = True

    def __init__(self, name, author, pages_total, isbn, is_reserved=False):
        self.name = name
        self.author = author
        self.pages_total = pages_total
        self.isbn = isbn
        self.is_reserved = is_reserved

    def print_info(self):
        print(f'Название: {self.name}, Автор: {self.author}, страниц: {self.pages_total}, материал: {Book.material}'
              f'{", зарезервирована" if self.is_reserved else ""}')


class SchoolBook(Book):

    def __init__(self, name, author, pages_total, isbn, subject, grade, is_workbook, is_reserved=False):
        super().__init__(name, author, pages_total, isbn, is_reserved)
        self.subject = subject
        self.grade = grade
        self.is_workbook = is_workbook

    def print_info(self):
        print(f'Название: {self.name}, Автор: {self.author}, страниц: {self.pages_total},  предмет: {self.subject},'
              f' класс: {self.grade}{", зарезервирована" if self.is_reserved else ""}')


book1 = Book('Пролетая над гнездом кукушки', 'Кен Кизи', 500, '978-5-7324-1162-3')
book2 = Book('Над пропастью во ржи', 'Джером Сэлинджер', 200, '978-5-7350-1162-3')
book3 = Book('Пятьдесят оттенков серого', 'Э. Л. Джеймс', 500, '978-5-7220-1162-3')
book4 = Book('Изучая Python', 'Эрик Мэтиз', 800, '978-5-7320-1162-3')
book5 = Book('Война и Мир', 'Лев Толстой', 1200, '978-5-7320-1562-3')


book1.is_reserved = True

book1.print_info()
book2.print_info()
book3.print_info()
book4.print_info()
book5.print_info()

school_book1 = SchoolBook('Основы математического анализа', 'Соколов', 500,
                          '978-5-7324-1164-3', 'Математика', 9, True)
school_book2 = SchoolBook('История древнего мира', 'Кун', 500,
                          '978-5-7324-1262-3', 'История', 6, True)

school_book2.is_reserved = True

school_book1.print_info()
school_book2.print_info()
