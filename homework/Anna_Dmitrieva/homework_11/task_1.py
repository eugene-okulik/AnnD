# Создайте класс book с атрибутами:
#
# материал страниц
# наличие текста
# название книги
# автор
# кол-во страниц
# ISBN
# флаг зарезервирована ли книга или нет (True/False).
# Какие-то из атрибутов будут общими для всех
# книг (материал, наличие текста), какие-то индивидуальными.
# Создайте несколько (штук 5) экземпляров разных книг.
# После создания пометьте одну книгу как зарезервированную.
# Распечатайте детали о каждой книге в таком виде:
# Если книга зарезервирована:
# Название: Идиот, Автор: Достоевский, страниц: 500,
# материал: бумага, зарезервирована
# если не зарезервирована:
# Название: Идиот, Автор: Достоевский, страниц: 500,
# материал: бумага

class Book:
    book_material_page = "бумага"
    book_text = True

    def __init__(self, name_of_book, author, amount_page, isbn,
                 default_reserved=False):
        self.name_of_book = name_of_book
        self.author = author
        self.amount_page = amount_page
        self.isbn = isbn
        self.default_reserved = default_reserved

    def book_reserve(self):
        self.default_reserved = True

    def book_info(self):
        info = (f"Название: {self.name_of_book}, автор: {self.author}, "
                f"страниц: {self.amount_page}, "
                f"материал: {Book.book_material_page}")

        if self.default_reserved:
            info += ", зарезервирована"
        print(info)


book1 = Book("Идиот", "Достоевский", 500, "978-5-389-07435-7")
book2 = Book("Преступление и наказание", "Достоевский", 430,
             "978-5-389-10388-0")
book3 = Book("Анна Каренина", "Толстой", 850, "978-5-699-99859-9")
book4 = Book("Мастер и Маргарита", "Булгаков", 400,
             "978-5-17-118366-5")
book5 = Book("Война и мир", "Толстой", 1225, "978-5-17-118320-7")

book3.book_reserve()

books = [book1, book2, book3, book4, book5]
for book in books:
    book.book_info()

# Второй класс
# Создайте дочерний класс для первого. Это будет класс для
# школьных учебников. В нем будут дополнительные атрибуты:
# предмет (типа математика, история, география),
# класс (школьный класс, для которого этот учебник)(осторожно с
# названием переменной. class - зарезервированное слово),
# наличие заданий (bool)
# Создайте несколько экземпляров учебников.
# После создания пометьте один учебник как
# зарезервированный.
# Распечатайте детали о каждом учебнике в таком виде:
# Если учебник зарезервирован:
# Название: Алгебра, Автор: Иванов, страниц: 200,
# предмет: Математика, класс: 9, зарезервирована
# если не зарезервирован:
# Название: Алгебра, Автор: Иванов, страниц: 200,
# предмет: Математика, класс: 9


class SchoolBook(Book):

    def __init__(self, name_of_book, author, amount_page, isbn, subject,
                 school_klass, has_exercises, default_reserved=False):
        super().__init__(name_of_book, author, amount_page, isbn,
                         default_reserved)
        self.subject = subject
        self.school_klass = school_klass
        self.has_exercises = has_exercises

    def book_info(self):
        exercises_info = "есть задания" if self.has_exercises \
            else "нет заданий"
        info = (f"Название: {self.name_of_book}, автор: {self.author}, "
                f"страниц: {self.amount_page}, предмет: {self.subject}, "
                f"класс: {self.school_klass}, {exercises_info}")
        if self.default_reserved:
            info += ", зарезервирована"
        print(info)


schoolbook1 = SchoolBook("Алгебра и начала анализа", "Иванов", 200,
                         "123-4-56-789012-3", "Математика", 9, True)
schoolbook2 = SchoolBook("Черчение", "Васечкин", 180,
                         "123-4-56-789012-4", "География", 8, True)
schoolbook3 = SchoolBook("История Беларуси", "Копеечкин", 300,
                         "123-4-56-789012-5", "История", 10, False)

schoolbook2.book_reserve()

schoolbooks = [schoolbook1, schoolbook2, schoolbook3]

print("\nУчебники:")
for sb in schoolbooks:
    sb.book_info()
