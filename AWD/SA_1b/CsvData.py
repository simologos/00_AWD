class CsvData:
    def __init__(self):
        """
        Initialize a new instance of CsvData, which represents a CSV file and it's content
        """
        self.__rows = []

    def append(self, row: []):
        """
        Appends a new row to the existing list of rows.

        Keep in mind, the first row represents the header.
        :param row: array, containing all column values of a specific row. Example: row = ["Key", "Value", "Street"]
        :return: None
        """
        self.__rows.append(row)

    def get_header(self):
        """
        Gets the header of the CSV file.
        The first appended row represents the header of the CSV file.
        :return: header row. Otherwise an empty array.
        """

        # Check if any rows are available
        if not self.has_rows():
            return self.__rows  # empty array

        return self.__rows[0]

    def get_body(self):
        """
        Gets the body of the CSV file (without header)
        :return: body rows(without header)
        """

        # Check if the row list has any rows, except the hedaer
        if self.__get_count() <= 1:
            return []

        return self.__rows[1:]  # all items except the header (at index 0)

    def get_header_and_body(self):
        """
        Geta all rows consists of header and body
        :return: All stored rows
        """
        return self.__rows

    def has_rows(self):
        """
        Determines if any rows are appended
        :return: True if it has rows. Otherwise False
        """
        return self.__get_count() > 0

    def __get_count(self):
        """
        Gets the current row count
        :return: count
        """
        return len(self.__rows)
