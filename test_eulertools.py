'''
Test eulertools

'''
import unittest
import gmpy2

import mock

import eulertools


class EulerToolsTestCase(unittest.TestCase):
    @mock.patch('eulertools.sum')
    def test_sum_of_digits(self, mock_sum):
        mock_sum.return_value = 1
        r = eulertools.sum_of_digits(123)
        mock_sum.assert_called_once()
        self.assertEqual(1, r, 'sum_of_digits returns the result of the sum function')

    def test_divisorGenerator(self):
        divisors_of_30 = [1, 2, 3, 5, 6, 10, 15, 30]
        self.assertEqual(eulertools.divisorGenerator(30),divisors_of_30)
        p= int( gmpy2.next_prime(97))
        for _ in xrange(10):
            p = int (gmpy2.next_prime(p))
            self.assertEqual([1,p] ,eulertools.divisorGenerator(p) )
        try:
            eulertools.divisorGenerator('a')
            raise AssertionError('eulertools.divisorGenerator should raise exception for str input')
        except:
            pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
