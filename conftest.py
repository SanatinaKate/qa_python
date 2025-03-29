from main import BooksCollector
import pytest


# Создание тестового словаря с книгами
@pytest.fixture(scope="class")
def books(scope="class"):
    books = {'Горе от ума': 'Комедии',
             'Десять негритят': 'Детективы',
             'Дракула': 'Ужасы',
             'Дюна': 'Фантастка',
             'Ревизор': 'Комедии',
             'Оно': 'Ужасы',
             'Cнеговик': 'Детективы',
             'Трое из Простоквашино': 'Мультфильмы',
             'Тысяча и одна ночь': 'Сказки',
             'Чайка': 'Комедии'}
    return books

# Создание экземпляра класса BooksCollector
@pytest.fixture(scope="function")
def collector(request):
    collector = BooksCollector()
    return collector
