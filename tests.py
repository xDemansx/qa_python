import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    #def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
    #    collector = BooksCollector()

        # добавляем две книги
    #    collector.add_new_book('Гордость и предубеждение и зомби')
    #    collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
    #    assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    # Запустить тесты из терминала pytest -v tests.py

    # 1. Тест 1 метода add_new_book. Добавим 1 книгу и проверим добавление книги
    def test_add_new_book_add_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.get_books_genre()
                
    # 1.1. Тест 1 метода add_new_book. У добавленной книги нет жанра.
    def test_add_new_book_add_book_without_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби 2')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби 2': ''}
        
    # 2. Тест 2 метода set_book_genre. Добавим 1 книгу с жанром и проверим её по жанру
    def test_set_book_genre_add_book_with_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Чужие1')
        collector.set_book_genre('Чужие1', 'Фантастика')
        assert collector.get_book_genre('Чужие1') == 'Фантастика'
    
    # 3. Тест 3 метода get_book_genre. Добавим 1 книгу с жанром и проверим её жанр по имени
    def test_get_book_genre_add_book_with_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Чужие2')
        collector.set_book_genre('Чужие2', 'Ужасы')
        assert collector.get_book_genre('Чужие2') == 'Ужасы'

    # 4. Тест 4 метода get_books_with_specific_genre. Добавим 1 книгу с жанром и выведем список книг с данным жанром
    def test_get_books_with_specific_genre_add_book_with_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Чужие3')
        collector.set_book_genre('Чужие3', 'Детективы')
        assert collector.get_books_with_specific_genre('Детективы') == ['Чужие3']

    # 5. Тест 5 метода get_books_genre. Добавим 1 книгу с жанром и проверим словарь books_genre
    def test_get_books_genre_add_book_with_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Чужие4')
        collector.set_book_genre('Чужие4', 'Мультфильмы')
        assert collector.get_books_genre() == {'Чужие4':'Мультфильмы'}

    # 6. Тест 6 метода get_books_for_children. Добавим 1 книгу с жанром, подходящим детям и проверим ее в списке books_for_children
    def test_get_books_for_children_add_book_with_genre_for_children_true(self):
        collector = BooksCollector()
        collector.add_new_book('Чужие5')
        collector.set_book_genre('Чужие5', 'Комедии')
        assert 'Чужие5' in collector.get_books_for_children() 

    # 6.1. Тест 6 метода get_books_for_children. Добавим 1 книгу с жанром, НЕ подходящим детям и проверим ее в списке books_for_children
    def test_get_books_for_children_add_book_with_genre_not_for_children_true(self):
        collector = BooksCollector()
        collector.add_new_book('Кровожадный Пух и Пятак')
        collector.set_book_genre('Кровожадный Пух и Пятак', 'Ужасы')
        assert 'Кровожадный Пух и Пятак' not in collector.get_books_for_children() 

    # 7. Тест 7 метода add_book_in_favorites. Добавим 1 книгу в избранное и проверим ее наличие в избранном
    def test_add_book_in_favorites_add_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Чужие6')
        collector.add_book_in_favorites('Чужие6')
        assert 'Чужие6' in collector.get_list_of_favorites_books()

    # 8. Тест 8 метода delete_book_from_favorites. Добавим 1 книгу в избранное, удалим и проверим ее отсутствие в избранном
    def test_delete_book_from_favorites_add_and_delete_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Чужие7')
        collector.add_book_in_favorites('Чужие7')
        collector.delete_book_from_favorites('Чужие7')
        assert 'Чужие7' not in collector.get_list_of_favorites_books()

    # 9. Тест 9 метода get_list_of_favorites_books. Передадим список из 2х книг в избранное и проверим их наличие в нем
    @pytest.mark.parametrize('books, genre', 
        [['Чунга-Чанга', 'Мультфильмы'], ['Терминатор и Смешарики', 'Фантастика']])
    def test_get_list_of_favorites_books_add_books_true(self, books, genre):
        collector = BooksCollector()
        collector.add_new_book(books)
        collector.add_book_in_favorites(books)
        assert books in collector.get_list_of_favorites_books()
