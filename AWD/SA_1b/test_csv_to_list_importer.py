import os
import unittest

import CsvData
from CsvImporter import CsvImporter


def check_equal_list(one: [], two: []):
    """
      Compares the items of two lists
      :param one: first list
      :param two: second list
      :return: True if the elements in the lists are equal
      """
    return len(one) == len(two) and sorted(one) == sorted(two)


class TestCsvToListImporter(unittest.TestCase):
    def __assert_header(self, csv_data: CsvData, expected:[]):
        """
        Asserts if the header is ecual to the expected list
        :param csv_data: CsvData object, containing the header
        :param expected: expected header
        :return:
        """
        self.__assert_equal_list(csv_data.get_header(), expected)

    def __assert_equal_list(self, one: [], two: []):
        self.assertTrue(check_equal_list(one, two))

    def __assert_specific_csv_row(self, csv_data: CsvData, row_position: int, expected_row: []):
        actual_row = csv_data.get_body()[row_position]

        self.assertTrue(len(actual_row) >= len(expected_row))

        for i in range(0, len(expected_row)):
            actual = actual_row[i]
            expected = expected_row[i]
            self.assertEqual(actual, expected, expected)

    def __assert_has_min_one_row(self, csv_data: CsvData):
        self.assertIsNotNone(csv_data)
        self.assertTrue(csv_data.has_rows())

    def __assert_body_has_one_row(self, csv_data: CsvData, expected_row: []):
        actual_body = csv_data.get_body()
        self.assertIsNotNone(actual_body)
        self.assertEqual(1, len(actual_body))

        self.__assert_equal_list(actual_body[0], expected_row)

    def test_import_by_string_list_with_2_lines(self):
        id_name, nr_name, description_name = "Id", "Nr", "Description"
        id_value, nr_value, description_value = "42", "1337", "Leed"

        lines = ["{},{},{}".format(id_name, nr_name, description_name),
                 "{},{},{}".format(id_value, nr_value, description_value)]

        target = CsvImporter(",")
        csv_data = target.load_from_string_list(lines)

        self.__assert_has_min_one_row(csv_data)
        self.__assert_header(csv_data, [id_name, nr_name, description_name])
        self.__assert_body_has_one_row(csv_data, [id_value, nr_value, description_value])

    def test_import_by_string_with_2_lines(self):
        id_name, nr_name, description_name = "Id", "Nr", "Description"
        id_value, nr_value, description_value = "42", "1337", "Leed"

        content = "{},{},{}".format(id_name, nr_name, description_name)
        content += "\n"
        content += "{},{},{}".format(id_value, nr_value, description_value)

        target = CsvImporter(",")
        csv_data = target.load_by_string(content)

        self.__assert_has_min_one_row(csv_data)
        self.__assert_header(csv_data, [id_name, nr_name, description_name])
        self.__assert_body_has_one_row(csv_data, [id_value, nr_value, description_value])

    def test_import_large_file(self):
        current_directory = os.path.dirname(__file__)
        file = os.path.join(current_directory, 'testdata\\valid_data_big_file.csv')

        target = CsvImporter(",")
        csv_data = target.load_from_file(file)

        self.assertTrue(csv_data.has_rows())
        lorem = '","'.join(csv_data.get_header())

        self.__assert_specific_csv_row(csv_data, 19490, ["663572", "FL", "MIAMI DADE COUNTY", "0", "65577.8"])
        self.assertEqual(36634, len(csv_data.get_body()))

    def test_import_string_list_which_is_none(self):
        target = CsvImporter(",")
        csv_data = target.load_from_string_list(None)
        self.assertIsNone(csv_data)

    def test_import_string_list_which_is_empty(self):
        target = CsvImporter(",")
        csv_data = target.load_from_string_list([])
        self.assertIsNone(csv_data)

    def test_passed_delimiter_is_a_word(self):
        self.__check_delimiter("HALLO", "HALLO")

    def test_default_delimiter(self):
        target = CsvImporter()
        self.assertEqual(",", target.get_delimiter())

    def __check_delimiter(self, passed_delimiter, expected_delimiter):
        target = CsvImporter(passed_delimiter)

        actual = target.get_delimiter()
        self.assertEqual(expected_delimiter, actual)
