import unittest

from circleci.python_package.python_code import add_it


class PackageTest(unittest.TestCase):
    """
    Tests.
    """

    def test_add_it(self):
        """
        Test 1+1=2.
        """
        result = add_it(1, 1)
        self.assertEqual(result, 2)
