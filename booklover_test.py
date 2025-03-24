import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_obj = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_title = 'test_book'
        test_obj.add_book(book_title, 5)

        self.assertTrue(book_title in test_obj.book_list['book_name'].values)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_obj = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_title = 'test_book'
        test_obj.add_book(book_title, 5)
        test_obj.add_book(book_title, 5)

        self.assertEqual(len(test_obj.book_list.loc[test_obj.book_list['book_name'] == book_title, :]), 1)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_obj = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_title = 'test_book'
        test_obj.add_book(book_title, 5)
        
        self.assertTrue(test_obj.has_read(book_title))

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_obj = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_title = 'test_book'
        test_obj.add_book('test_book_no', 5)
        
        self.assertFalse(test_obj.has_read(book_title))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_obj = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_obj.add_book('b1', 5)
        test_obj.add_book('b2', 5)

        self.assertEqual(test_obj.num_books_read(), 2)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test_obj = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_obj.add_book('b1', 3)
        test_obj.add_book('b2', 5)

        self.assertEqual(len(test_obj.fav_books()), 1)
        
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)


    