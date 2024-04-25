import unittest
def extract_column(column_index, data):
    try:
        return [row[column_index] for row in data]
    except (ValueError, IndexError) as e:
        return None    

class TestFunctions(unittest.TestCase):
    data = [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
    ]

    def test_extract_column(self):
        self.assertEqual(extract_column(1, self.data), [2, 5, 8])

    def test_index_error(self):
        result = extract_column(3, self.data)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()