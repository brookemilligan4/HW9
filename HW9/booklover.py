import pandas as pd

class BookLover:
    def __init__(self, name: str, email: str, fav_genre: str, num_books: int = 0, book_list: pd.DataFrame = None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = pd.DataFrame({'book_name': [], 'book_rating': []}) if book_list is None else book_list

    def add_book(self, book_name: str, rating: int):
        if not (0 <= rating <= 5):
            raise ValueError("Rating must be between 0 and 5.")
        
        if book_name in self.book_list['book_name'].values:
            print(f"{book_name} is already in the book list.")
            return
        
        new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
        self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        self.num_books += 1

    def has_read(self, book_name: str) -> bool:
        return book_name in self.book_list['book_name'].values

    def num_books_read(self) -> int:
        return self.num_books

    def fav_books(self) -> pd.DataFrame:
        return self.book_list[self.book_list['book_rating'] > 3]

if __name__ == '__main__':
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    print(test_object.book_list)
    