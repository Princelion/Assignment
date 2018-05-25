"retake exam"
import unittest
import math

def exam_log(base, exp):
    '''argument of logs and return calculated log'''
    if base < 0:
        raise ValueError('base must be positive')
    if isinstance(base, str):
        raise TypeError('base and exp must be positive')
    return math.log(base, exp)


class Testexam(unittest.TestCase):

    def test_log(self):
        '''test log funtion with float'''
        self.assertEqual(exam_log(100.00, 10), 2.0)

    def test_blog(self):
        '''test log funtion with integers'''
        self.assertEqual(exam_log(8, 2), 3)

    def test_abs(self):
        '''test log with strings argument'''
        self.assertRaises(TypeError, exam_log, 'prince')



if __name__ == '__main__':
    unittest.main()
