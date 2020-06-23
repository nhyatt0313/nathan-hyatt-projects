import unittest
import DirectoryPrinter as dp

class DirectoryPrinterTest(unittest.TestCase):

    def testFilterItemGitDir(self):
        item = ".git"
        filters = ["*.git/"]
        self.assertTrue(dp.filterItem(item, filters))

    def testFilterItemOneLetterFilterDir(self):
        item = "anythingEndingWitht"
        filters = ["*t/"]
        self.assertTrue(dp.filterItem(item, filters))

    def testFilterItemThreeNumFilterDir(self):
        item = "anythingEndingWith123"
        filters = ["*123/"]
        self.assertTrue(dp.filterItem(item, filters))

    def testFilterItemFilterFile(self):
        item = "thisFile.exe"
        filters = ["*.exe"]
        self.assertTrue(dp.filterItem(item, filters))

    def testFilterItemEndingInOneLetterFilterGenFile(self):
        item = "thisFileExtEndsIny.py"
        filters = ["*y"]
        self.assertTrue(dp.filterItem(item, filters))

    def testFilterItemEndingInOneLetterFilterGenDir(self):
        item = "thisDirEndsInb"
        filters = ["*b"]
        self.assertTrue(dp.filterItem(item, filters))

if __name__ == '__main__':
    unittest.main()