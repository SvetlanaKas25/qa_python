from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_duplicate_not_add(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Гордость и предубеждение')

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize("book_name", [
        "",  # пустая строка
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"  # 41 символ
        ])
    def test_add_new_book_invalid_names_not_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)

        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_valid_book_and_genre_set_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Шерлока Холмса')
        collector.set_book_genre('Приключения Шерлока Холмса', "Детективы")

        assert collector.get_book_genre('Приключения Шерлока Холмса') == "Детективы"

    def test_get_book_genre_nonexistent_book_not_get_genre(self):
        collector = BooksCollector()
        
        assert collector.get_book_genre('Неизвестная книга') is None
    
    def test_get_books_with_specific_genre_valid_genre_returns_matching_books(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Шерлока Холмса')
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Приключения Шерлока Холмса', 'Детективы')
        collector.set_book_genre('Десять негритят', 'Детективы')
        
        result = collector.get_books_with_specific_genre('Детективы')
        assert 'Приключения Шерлока Холмса' in result
        assert 'Десять негритят' in result

    def test_get_books_genre_empty_collection_returns_empty_dictionary(self):
        collector = BooksCollector()
        
        assert collector.get_books_genre() == {}
    
    def test_get_books_for_children_adult_books_not_included(self):
        collector = BooksCollector()
        collector.add_new_book('Пила')
        collector.set_book_genre('Пила', 'Ужасы')
        
        result = collector.get_books_for_children()
        assert "Ужасы" not in result

    def test_add_book_in_favorites_one_book_added_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Шерлока Холмса')
        collector.add_book_in_favorites('Приключения Шерлока Холмса')
        
        assert 'Приключения Шерлока Холмса' in collector.get_list_of_favorites_books()
    
    def test_delete_book_from_favorites_nonexistent_book_no_changes_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book ('Приключения Шерлока Холмса')
        collector.add_book_in_favorites('Приключения Шерлока Холмса')
        collector.delete_book_from_favorites('Неизвестная книга')

        assert 'Приключения Шерлока Холмса' in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 1
    
    def test_get_list_of_favorites_books_with_books_returns_list_of_favorites(self):
        collector = BooksCollector()
        collector.add_new_book ('Книга для Избранного')
        collector.add_book_in_favorites('Книга для Избранного')
        collector.add_new_book('Книга не для Избранного')
        result = collector.get_list_of_favorites_books()
        
        assert 'Книга для Избранного' in result
        assert 'Книга не для Избранного' not in result
    
    