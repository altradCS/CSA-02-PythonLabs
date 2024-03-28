import unittest

def custom_shuffle(lst):
    shuffled_lst = lst[:]  # Create a copy of the list to avoid modifying the original
    for i in range(len(shuffled_lst)):
        rand_index = random.randint(0, len(shuffled_lst) - 1)
        shuffled_lst[i], shuffled_lst[rand_index] = shuffled_lst[rand_index], shuffled_lst[i]
    return shuffled_lst

def remove_duplicates(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

class TestShuffleAndRemoveDuplicates(unittest.TestCase):

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

        # Check if the length of the unique list is correct
        self.assertEqual(len(unique_list), len(set(lst_with_duplicates)))
        # Check if all elements in the unique list are indeed unique
        for item in unique_list:
            self.assertEqual(lst_with_duplicates.count(item), 1)

if __name__ == '__main__':
    unittest.main()
