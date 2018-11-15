import unittest
import cap

'''
This is the test script which tests the cap.py file.
'''
class TestCap(unittest.TestCase):
    def test_one_word(self):
        '''
        It checks if the tet python is capitalised to python by calling from cap.py fn.
        '''
        text='python'
        result=cap.cap_text(text)
        self.assertEqual(result,'Python')
    def test_multiple_word(self):
        text='my python'
        result=cap.cap_text(text)
        self.assertEqual(result,'My Python')
if __name__=='__main__':
    unittest.main()
