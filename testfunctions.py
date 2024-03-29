import unittest

class ListFuncitons(unittest.TestCase):

    def test_custom_shuffle(self):
        # Test custom_shuffle function
        original_list = [1, 2, 3, 4, 5]
        shuffled_list = custom_shuffle(original_list)

        # Check if the length of the shuffled list remains the same
        self.assertEqual(len(original_list), len(shuffled_list))
        # Check if all elements from the original list are present in the shuffled list
        for item in original_list:
            self.assertIn(item, shuffled_list)

    def test_remove_duplicates(self):
        # Test remove_duplicates function
        lst_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
        unique_list = remove_duplicates(lst_with_duplicates)
        for item in unique_list:
            self.assertEqual(unique_list.count(item),1)


if __name__ == '__main__':
    unittest.main()
