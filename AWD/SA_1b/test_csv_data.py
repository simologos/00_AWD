import unittest

from CsvData import CsvData


def check_equal_list(one: [], two: []):
    """
    Compares the items of two lists
    :param one: first list
    :param two: second list
    :return: True if the elements in the lists are equal
    """
    return len(one) == len(two) and sorted(one) == sorted(two)


class TestCsvData(unittest.TestCase):
    def __assert_equal_list(self, one: [], two: []):
        """
        Assert if the passed lists are equal
        :param one: first list
        :param two: second list
        :return: None
        """
        self.assertTrue(check_equal_list(one, two))

    def __assert_not_equal_list(self, one: [], two: []):
        """
             Assert if the passed lists are not equal
             :param one: first list
             :param two: second list
             :return: None
             """
        self.assertFalse(check_equal_list(one, two))

    def test_rows_is_empty_after_initialization(self):
        target = CsvData()
        self.assertEqual(0, len(target.get_header_and_body()))
        self.assertEqual(0, len(target.get_body()))
        self.assertEqual(0, len(target.get_header()))
        self.assertFalse(target.has_rows())

    def test_get_header(self):
        expected = ["lo", "re", "m"]
        target = CsvData()

        self.__assert_not_equal_list(expected, target.get_header())
        target.append(expected)

        self.__assert_equal_list(expected, target.get_header())

        self.assertEqual(0, len(target.get_body()))
        self.assertEqual(1, len(target.get_header_and_body()))
        self.assertTrue(target.has_rows())

    def test_has_rows(self):
        row_one = ["lo", "re", "m"]
        row_two = ["1", "33", "7"]

        target = CsvData()

        self.assertFalse(target.has_rows())

        target.append(row_one)
        self.assertTrue(target.has_rows())

        target.append(row_two)
        self.assertTrue(target.has_rows())

    def test_get_header_and_body(self):
        expected_header = ["lo", "re", "m"]
        expected_body = ["1", "33", "7"]
        target = CsvData()

        self.assertEqual(0, len(target.get_header_and_body()))

        target.append(expected_header)
        self.assertEqual(1, len(target.get_header_and_body()))

        target.append(expected_body)
        self.assertEqual(2, len(target.get_header_and_body()))

        self.__assert_equal_list(expected_header, target.get_header_and_body()[0])
        self.__assert_equal_list(expected_body, target.get_header_and_body()[1])

    def test_get_body(self):
        header = ["lo", "re", "m"]
        expected_body = ["1", "33", "7"]
        target = CsvData()

        self.assertEqual(0, len(target.get_body()))

        target.append(header)
        self.assertEqual(0, len(target.get_body()))

        target.append(expected_body)
        self.assertEqual(1, len(target.get_body()))

        self.__assert_equal_list(expected_body, target.get_body()[0])
