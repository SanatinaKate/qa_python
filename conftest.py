from main import BooksCollector
import pytest


# Создание экземпляра класса BooksCollector
@pytest.fixture(scope="function")
def collector(request):
    collector = BooksCollector()
    return collector
