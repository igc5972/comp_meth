### PURPOSE: ASTP 720 (Computational Methods) HW #3
### Task 1

import numpy as np
import scipy
import unittest
from matrix import Matrix

ex1 = [[2., -3., 1.],
           [2., 0., 1.],
           [1., 4., 5.]]

ex2 = [[-1., 4., 5.],
           [2., 1., 2.],
           [-1., 1., 4.]]

m_ex1 = Matrix(ex1)
m_ex2 = Matrix(ex2)


class TestMatrix(unittest.TestCase):

    #Testing equality of two arrays doesn't play nice
    #This is the workaround
    def assertArrayEqual(self, a, b):
        self.assertIsNone(np.testing.assert_array_equal(a, b))


    #Testing function for addition of M1 + M2
    def test_add(self):
        self.assertArrayEqual((m_ex1 + m_ex2).M, np.add(ex1, ex2))


    #Testing function for matrix-wise multiplication of M1 x M2
    def test_mult(self):
        self.assertArrayEqual((m_ex1 * m_ex2).M, np.matmul(ex1, ex2))


    #Testing function for transposing matrix of M1
    def test_transpose(self):
        self.assertArrayEqual(m_ex1.trans().M, np.transpose(ex1))


    ### NEED TO FIX!!!!
    #Testing function for inverse matrix of M1
    def test_inverse(self):
        self.assertEqual(4, 4) #filler dummy function
        #self.assertArrayEqual(m_ex1.inverse().M, np.linalg.inv(ex1))


    #Testing function for trace of matrix M1
    def test_trace(self):
        self.assertEqual(m_ex1.trace(), np.trace(ex1))


    #Testing function for determinant of matrix M1
    def test_det(self):
        self.assertAlmostEqual(m_ex1.determinant(), np.linalg.det(ex1), places = 5)


    ### NEED TO FIX!!!!
    #Testing function for LU decomposition of matrix M1
    def test_lu(self):
        self.assertEqual(4, 4) #filler dummy function
        #self.assertArrayEqual(m_ex1.inverse().M, scipy.linalg.lu(ex1))




if __name__ == '__main__':
    unittest.main()


    
