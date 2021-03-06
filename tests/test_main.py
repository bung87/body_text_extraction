# -*- coding:utf-8 -*-

import unittest
from body_text_extraction import BodyTextExtraction
import os 
from pathlib import Path

data_path = Path(os.path.join(os.path.dirname(__file__),"data"))
# python3 -m unittest tests.main_test
class TestMain(unittest.TestCase):
    def test_fsight(self):
        extractor = BodyTextExtraction()
        html_content = (data_path / "fsight.raw" ).read_text()
        text = extractor.extract(html_content)
        # print(text)
        output = (data_path / "fsight.txt" ).read_text()
        self.assertEqual(output, text)
    
    def test_yahoo(self):
        extractor = BodyTextExtraction()
        html_content = (data_path / "yahoo.raw" ).read_text()
        text = extractor.extract(html_content)
        # print(text)
        output = (data_path / "yahoo.txt" ).read_text()
        self.assertEqual(output, text)

    def test_sina(self):
        extractor = BodyTextExtraction()
        html_content = (data_path / "sina.raw" ).read_text()
        text = extractor.extract(html_content)
        print(text)
        output = (data_path / "sina.txt" ).read_text()
        self.assertEqual(output, text)


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestMain))
    return suite

if __name__ == '__main__':
    unittest.main()