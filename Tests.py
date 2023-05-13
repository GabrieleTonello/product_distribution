import unittest
from main import  product_allocation, GLOBAL_MODULE

class Product_allocation_tests(unittest.TestCase):
    def test_example_1(self):
        """ Tests the first example given"""
        array_1 = [5,2]
        array_2 = [1,5,4,2,3]
        self.assertEqual(product_allocation(array_1, array_2), 27, "Should be equal to 27")

    def test_example_2(self):
        """ Tests the second example given"""
        array_1 = [11,3]
        array_2 = [1,2,3,4,5,6,7,8,9,10,11]
        self.assertEqual(product_allocation(array_1, array_2), 171, "Should be equal to 171")

    def test_max_n_0(self):
        """ Tests the function with the max n values, correct output is calculated with math (mathematical series)"""
        array_1 = [1000000, 5]
        array_2 = [0 for i in range(0,1000000)]
        self.assertEqual(product_allocation(array_1, array_2), 0, "Should be equal to 0")

    def test_max_n_1(self):
        """ Tests the function with the max n values, correct output is calculated with math (mathematical series)"""
        array_1 = [1000000, 1]
        array_2 = [1 for i in range(0,1000000)]
        self.assertEqual(product_allocation(array_1, array_2), 500000500000 % GLOBAL_MODULE, "Should be equal to 496500")

    def test_max_n_3(self):
        """ Tests the function with the max n values, correct output is calculated with math (mathematical series)"""
        array_1 = [1000000, 1]
        array_2 = [1/2 for i in range(0,1000000)]
        self.assertEqual(product_allocation(array_1, array_2), 250000250000 % GLOBAL_MODULE, "Should be equal to 248250")

    def test_max_n_4(self):
        """ Tests the function with the max n values, correct output is calculated with math (mathematical series)"""
        array_1 = [1000000, 2]
        array_2 = [1/2 for i in range(0,1000000)]
        self.assertEqual(product_allocation(array_1, array_2), 125000250000 % GLOBAL_MODULE, "Should be equal to 249125")

    def test_Error(self):
        """ Tests if the funxtion throwns a ValueError if m > n """
        array_1 = [3, 5]
        array_2 = [1, 2, 3]
        self.assertRaises(ValueError, product_allocation, array_1, array_2)

    def test_random_values(self):
        """ Test the function with random values"""
        array_1 = [6, 2]
        array_2 = [2, 6, 8, 4, 10, 15] 
        self.assertEqual(product_allocation(array_1, array_2), 109 % GLOBAL_MODULE, "Should be equal to 109")
    

if __name__ == '__main__':
    unittest.main()