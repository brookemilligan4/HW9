import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        lover = BookLover("Test User", "test@example.com", "fantasy")
        lover.add_book("Harry Potter", 5)
        self.assertIn("Harry Potter", lover.book_list['book_name'].values)

    def test_2_add_book(self):
        lover = BookLover("Test User", "test@example.com", "fantasy")
        lover.add_book("Harry Potter", 5)
        lover.add_book("Harry Potter", 5)  # Adding the same book again
        self.assertEqual(lover.num_books_read(), 1)  # Should still be 1

    def test_3_has_read(self): 
        lover = BookLover("Test User", "test@example.com", "fantasy")
        lover.add_book("Harry Potter", 5)
        self.assertTrue(lover.has_read("Harry Potter"))

    def test_4_has_read(self): 
        lover = BookLover("Test User", "test@example.com", "fantasy")
        self.assertFalse(lover.has_read("Nonexistent Book"))
        
    def test_5_num_books_read(self): 
        lover = BookLover("Test User", "test@example.com", "fantasy")
        lover.add_book("Harry Potter", 5)
        lover.add_book("The Hobbit", 4)
        self.assertEqual(lover.num_books_read(), 2)

    def test_6_fav_books(self):
        lover = BookLover("Test User", "test@example.com", "fantasy")
        lover.add_book("Harry Potter", 5)
        lover.add_book("The Hobbit", 4)
        lover.add_book("Bad Book", 2)
        fav_books = lover.fav_books()
        self.assertTrue(all(rating > 3 for rating in fav_books['book_rating']))

if __name__ == '__main__':
    unittest.main(verbosity=3)