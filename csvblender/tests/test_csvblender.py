import unittest
from csvblender.csvblender import CSVBlender


class CSVBlenderTests(unittest.TestCase):

    def setUp(self):
        self.blender = CSVBlender()

    def test_get_fieldnames(self):
        # test = self.blender.getFieldNames("./merge_test.csv")
        # expected = ['KEY', 'Last_Name', 'First_Name', 'Age']
        # self.assertEqual(test, expected)
        pass

    def test_get_fieldnames_missing_file(self):
        self.assertRaises(FileNotFoundError, self.blender.getFieldNames, "./missing_file.csv")

if __name__ == '__main__':
    unittest.main()