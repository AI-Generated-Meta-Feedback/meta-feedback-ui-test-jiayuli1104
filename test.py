import unittest
from CODE import Book, books_from_tuples, tuples_from_books, sort_books

class TestLibrarySort(unittest.TestCase):

    def test_all_different_shelves(self):
        # a) All books from different shelves
        data = books_from_tuples([(1, 3), (5, 1), (3, 2)])
        expected = [(1, 3), (3, 2), (5, 1)]
        self.assertEqual(tuples_from_books(sort_books(data)), expected)

    def test_same_shelf_stability(self):
        # b) Multiple books from the same shelf (tests stability)
        data = books_from_tuples([(5, 3), (5, 1), (5, 2)])
        expected = [(5, 1), (5, 2), (5, 3)]
        self.assertEqual(tuples_from_books(sort_books(data)), expected)

    def test_already_sorted(self):
        # c) Books already in correct order
        data = books_from_tuples([(2, 1), (3, 2), (4, 3)])
        expected = [(2, 1), (3, 2), (4, 3)]
        self.assertEqual(tuples_from_books(sort_books(data)), expected)

    def test_reverse_order(self):
        # d) Books in reverse order
        data = books_from_tuples([(5, 3), (4, 2), (1, 1)])
        expected = [(1, 1), (4, 2), (5, 3)]
        self.assertEqual(tuples_from_books(sort_books(data)), expected)

    def test_mix_same_and_diff(self):
        # Additional: mix of same shelf and different shelves
        data = books_from_tuples([(2, 5), (1, 2), (2, 1), (1, 1), (3, 7)])
        expected = [(1, 1), (1, 2), (2, 1), (2, 5), (3, 7)]
        self.assertEqual(tuples_from_books(sort_books(data)), expected)


if __name__ == "__main__":
    unittest.main()



