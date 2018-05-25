
import unittest
import math

def exam_log(base, exp):
	if (base < 0):
		raise ValueError('base must be positive')
	if type(base) is str:
		raise TypeError('base and exp must be positive')
	return math.log(base, exp)


class Testexam(unittest.TestCase):

    def test_log(self):
        self.assertEquals(exam_log(100,10), 2.0)
 
    def test_blog(self):
        self.assertEquals(exam_log(8,2), 3)
 
    def test_abs(self):
        self.assertRaises(TypeError, exam_log, 'prince')




if __name__ == '__main__':
    unittest.main()