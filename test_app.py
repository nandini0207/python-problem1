import unittest
from app import getTopMenu, restaurentException

class testGetTopMenu(unittest.TestCase):
    def test_getMenu(self):
        # try:
        #     getTopMenu("resLogFile_Duplicates.txt")
        # except restaurentException as e:
        #     assert False, f"'getTopMenu' raised an exception {e}"
        # self.assertRaises(restaurentException, getTopMenu, "resLogFile_InvalideFormat.txt")
        self.assertEquals(getTopMenu("resLogFile_Duplicates.txt"), None)
        self.assertEquals(getTopMenu("resLogFile_Duplicates.txt"), None)
        self.assertTrue(getTopMenu("resLogFile_NoDuplicates.txt"))
