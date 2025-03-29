import pytest


# Класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    # Проверка значения атрибута books_genre после инициализации
    def test_init_check_book_genre_is_empty_dict(self, collector):
        # проверяем, что атрибут books_genre проинициализиоован пустым словарем
        assert collector.books_genre == {}

    # Проверка значения атрибута favortes после инициализации
    def test_init_check_favorites_is_empty_list(self, collector):
        # проверяем, что атрибут favorites проинициализиоован пустым списком
        assert collector.favorites == []

    # Проверка значения атрибута genre после инициализации
    def test_init_check_genre_values(self, collector):
        # проверяем, что атрибут genre проинициализирован нужными значениями
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    # Проверка значения атрибута genre_age_rating после инициализации
    def test_init_check_genre_age_rating_values(self, collector):
        # проверяем, что атрибут genre_age_ratng проинициализирован нужными значениями
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    # Добавление книги с некорректным именем (пустым или слишком длинным) в словарь с жанрами
    @pytest.mark.parametrize("name", ['', 'Чудесное путешествие Нильса с дикими гусями'])
    def test_add_new_book_for_book_with_invalid_name(self, collector, name):
        # добавляем книгу с некорректным именем
        collector.add_new_book(name)

        # проверяем, что книга не добавилась
        assert len(collector.books_genre) == 0

    # Добавление двух различных книг в словарь с жанрами
    def test_add_new_book_for_two_different_books(self, collector):
        # добавляем две различные книги
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Гарри Поттер')

        # проверяем, что добавились две книги
        assert len(collector.books_genre) == 2

    # Добавление двух одинаковых книг в словарь с жанрами
    def test_add_new_book_for_two_identical_books(self, collector):
        # добавляем две одинаковые книги
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')

        # проверяем, что добавилась только одна книга
        assert len(collector.books_genre) == 1

    # Проверка отсутствие жанра у добавленной книги
    @pytest.mark.parametrize("name", ['Бесы', 'Идиот', 'Преступление и наказание'])
    def test_add_new_book_added_book_has_no_genre(self, collector, name):
        # добавляем книгу
        collector.add_new_book(name)

        # проверяем,что у добавленной книги жанр не задан
        assert collector.books_genre[name] == ''

    # Установка существующего жанра для добавленной книги
    @pytest.mark.parametrize("name, genre", [('Дюна', 'Фантастика'), ('Оно', 'Ужасы'), ('Снеговик', 'Детективы')])
    def test_set_book_genre_for_existing_genre(self, collector, name, genre):
        # добавляем книгу
        collector.add_new_book(name)

        # устанавливаем существующий жанр для добавленной книги
        collector.set_book_genre(name, genre)

        # проверяем, что установился заданный жанр
        assert  collector.books_genre[name] == genre

    # Установка неизвестноо жанра для добавленной книги
    @pytest.mark.parametrize("genre", ['Драмы', 'Поэмы', 'Стихи'])
    def test_set_book_genre_for_unknown_genre(self, collector, genre):
        # добавляем книгу
        collector.add_new_book('Евгений Онегин')

        # устанавливаем неизвестный жанр для добавленной книги
        collector.set_book_genre('Евгений Онегин', genre)

        # проверяем, что у добавленной книи жанр по-прежнему не задан
        assert collector.books_genre['Евгений Онегин'] == ''

    # Проверка возврращаемого значения жанра книги
    def test_get_book_genre_check_result(self, books, collector):
        # добавляем книги из тестового словаря
        for name in books.keys():
            collector.add_new_book(name)

        # устанавливаем жанр для каждой добавленной книги
        for name, genre in books.items():
            collector.set_book_genre(name, genre)

        # получаем жанр каждой добавленной книги и проверяем правильность реультата
        for name, genre in books.items():
            genre_expected = genre if genre in collector.genre else ''
            assert collector.get_book_genre(name) == genre_expected

    # Проверка возвращвемого списка книг с заданным жанром
    @pytest.mark.parametrize("specific_genre", ['Детективы', 'Комедии', 'Сказки', 'Ужасы', 'Фантастика'])
    def test_get_books_with_specific_genre_check_result(self, books, collector, specific_genre):
        # добавляем книги из тестового словаря
        for name in books.keys():
            collector.add_new_book(name)

        # устанавливаем жанр для каждой добавленной книги и формируем ожидаемый список книг
        books_expected = []
        for name, genre in books.items():
            collector.set_book_genre(name, genre)
            if (genre == specific_genre) and (genre in collector.genre):
                books_expected.append(name)

        # получаем список книг с заданным жарном и проверям правильность результата
        assert collector.get_books_with_specific_genre(specific_genre) == books_expected

    # Проверка возвращаемого словаря с жанрами книг
    def test_get_books_genre_check_result(self, books, collector):
        # добавляем книги из тестового словаря и формируем ожидаемый словарь
        books_expected = {}
        for name in books.keys():
            collector.add_new_book(name)
            books_expected[name] = ''

        # получаем словарь с пустыми жанрами добавленных книг и проверяем правильность результата
        assert collector.get_books_genre() == books_expected

        # устанавливаем жанр для каждой добавленной книги и обновляем ожидаемый словарь
        for name, genre in books.items():
            collector.set_book_genre(name, genre)
            if genre in collector.genre:
                books_expected[name] = genre

        # получаем словарь с установленными жанрами книг и проверяем правильность результата
        assert collector.get_books_genre() == books_expected

    # Проверка возвращаемоо списка книг, подходящих детям
    def test_get_books_for_children_check_result(self, books, collector):
        # добавляем книги из тестового словаря
        for name in books.keys():
            collector.add_new_book(name)

        # устанавливаем жанр для каждой добавленной книги и формируем ожидаемый список книг
        books_expected = []
        for name, genre in books.items():
            collector.set_book_genre(name, genre)
            if (genre not in collector.genre_age_rating) and (genre in collector.genre):
                books_expected.append(name)

        # получаем список книг, подходящих детям, и проверям правильность результата
        assert collector.get_books_for_children() == books_expected

    # Добавление двух различных книг в список Избранного
    def test_add_book_in_favorites_for_two_different_books(self, collector):
        # добавляем две различные книги в словарь с жанрами
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Гарри Поттер')

        # добавляем книги из словаря с жанрами в список Избранного
        for name in collector.books_genre.keys():
            collector.add_book_in_favorites(name)

        # проверяем, что в список Избранного добавились две книги
        assert len(collector.get_list_of_favorites_books()) == 2

    # Добавление уже добавленной книги в список Избранного
    def test_add_book_in_favorites_for_already_favorite_book(self, collector):
        # добавляем книгу в словарь с жанрами
        collector.add_new_book('Война и мир')

        # добавляем книгу из словаря с жанрами в список Избранного
        collector.add_book_in_favorites('Война и мир')

        # повторно добавляем книгу из словаря с жанрами в список Избранного
        collector.add_book_in_favorites('Война и мир')

        # проверяем, что в список Избранного добавилась одна книга
        assert len(collector.get_list_of_favorites_books()) == 1

    # Удаление избранной книги из списка Избранного
    def test_delete_book_from_favorites_for_favorite_book(self, collector):
        # добавляем две различные книги в словарь с жанрами
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Гарри Поттер')

        # добавляем книги из словаря с жанрами в список Избранного
        for name in collector.books_genre.keys():
            collector.add_book_in_favorites(name)

        # удаляем избранную книгу из списка Избранного
        collector.delete_book_from_favorites('Гарри Поттер')

        # проверяем,что с списке Избранного нет удаленной книги
        assert 'Гарри Поттер' not in collector.get_list_of_favorites_books()

    # Удаление неизбранной книги из списка Избранного
    def test_delete_book_from_favorites_for_unfavorite_book(self, collector):
        # добавляем две различные книги в словарь с жанрами
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Гарри Поттер')

        # добавляем одну книгу из словаря с жанрами в список Избранного
        collector.add_book_in_favorites('Гарри Поттер')

        # удаляем неизбранную книгу из списка Избранного
        collector.delete_book_from_favorites('Властелин колец')

        # проверяем,что с списке Избранного осталась книга
        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()

    # Проверка возаращаемого списка Избранного
    @pytest.mark.parametrize("specific_genre", ['Детективы', 'Комедии', 'Фантастика'])
    def test_get_list_of_favorites_books_check_result(self, books, collector, specific_genre):
        # добавляем книги из тестового словаря
        for name in books.keys():
            collector.add_new_book(name)

        # добавляем книги с заданным жанром в список Избранного и формируем ожидаемый список Избранного
        favorites_expected = []
        for name, genre in books.items():
            if genre == specific_genre:
                collector.add_book_in_favorites(name)
                favorites_expected.append(name)

        # получаем список Избранного и проверям правильность результата
        assert collector.get_list_of_favorites_books() == favorites_expected
