# qa_python
Создан тест: test_add_new_book_duplicate_not_add 
Проверяется, что методом add_new_book одну и ту же книгу можно добавить только один раз.

Тест: test_add_new_book_invalid_names_not_added
Проверяется, что метод add_new_book не добавляет в коллекцию книги с невалидными названиями (пустая строка, 41 символ).

Тест: test_set_book_genre_valid_book_and_genre_set_genre
Проверяется, что метод set_book_genre устанавливает жанр для существующей книги из списка жанров.

Тест: test_get_book_genre_nonexistent_book_not_get_genre
Проверяется, что метод get_book_genre возвращает None для несуществующей книги.

Тест: test_get_books_with_specific_genre_valid_genre_returns_matching_books
Проверяется, что метод get_books_with_specific_genre возвращает список книг для существующего жанра.

Тест: test_get_books_genre_empty_collection_returns_empty_dictionary
Проверяется, что метод get_books_genre метод возвращает пустой словарь, если книги не добавлялись.

Тест: test_get_books_for_children_adult_books_not_included
Проверяется, что метод get_books_for_children книги с возрастным ограничением не включает в результат.

Тест: test_add_book_in_favorites_one_book_added_to_favorites
Проверяется, что метод add_book_in_favorites добавляет книгу в избранное.

Тест: test_delete_book_from_favorites_nonexistent_book_no_changes_to_favorites
Проверяется, что метод delete_book_from_favorites при попытке удалить несуществующую книгу, не изменяет список избранного.

Тест: test_get_list_of_favorites_books_with_books_returns_list_of_favorites
Проверяется, что метод get_list_of_favorites_books возвращает список, включающий в себя только те книги, которые были добавлены в избранное.

Доработки ПОСЛЕ РЕВЬЮ:
Добавлен тест: test_add_new_book_add_one_book
Проверяет позитивный сценарий добавления одной книги в коллекцию для метода add_new_book

