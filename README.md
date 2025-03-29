Файл main.py содержит класс BooksCollector

Файл tests.py содержит класс TestBooksCollector со следующими тестами для методов класса BooksCollector: 
- test_init_check_book_genre_is_empty_dict - тест на проверку значения атрибута books_genre после инициализации
- test_init_check_favorites_is_empty_list - тест на проверку значения атрибута favorites после инициализации
- test_init_check_genre_values - тест на проверку значения атрибута genre после инициализации
- test_init_check_genre_age_rating_values - тест на проверку значения атрибута genre_age_rating после инициализации
- test_add_new_book_for_book_with_invalid_name - тест на добавление книги с некорректным именем в словарь с жанрами
- test_add_new_book_for_two_different_books - тест на добавление двух различных книг в словарь с жанрами
- test_add_new_book_for_two_identical_books - тест на добавление двух одинаковых книг в словарь с жанрами
- test_add_new_book_added_book_has_no_genre - тест на проверку отсутствия жанра у добавленной книги
- test_set_book_genre_for_existing_genre - тест на установку существующего жанра для добавленной книги
- test_set_book_genre_for_unknown_genre - тест на установку неизвестного жанра для добавленной книги
- test_get_book_genre_check_result - тест на проверку возвращаемого значения жанра книги
- test_get_books_with_specific_genre_check_result - тест на проверку возвращвемого списка книг с заданным жанром
- test_get_books_genre_check_result - тест на проверку возвращаемого словаря с жанрами книг
- test_get_books_for_children_check_result - тест на проверку возвращаемоо списка книг, подходящих детям
- test_add_book_in_favorites_for_two_different_books - тест на добавление двух различных книг в список Избранного
- test_add_book_in_favorites_for_already_favorite_book - тест на добавление уже добавленной книги в список Избранного
- test_delete_book_from_favorites_for_favorite_book - тест на удаление избранной книги из списка Избранного
- test_delete_book_from_favorites_for_unfavorite_book - тест на удаление неизбранной книги из списка Избранного
- test_get_list_of_favorites_books_check_result - тест на проверку возаращаемого списка Избранного

Файл conftest.py содержит следующие фикстуры для тестов из класса TestBooksCollector:
- books - фикстура на создание тестового словаря с книгами
- collector - фикстура на создание экземпляра класса BooksCollector
