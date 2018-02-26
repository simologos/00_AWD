from CsvData import CsvData


class CsvImporter:
    def __init__(self, delimiter=","):
        """
        Initializer the importer
        :param delimiter: Optional delimiter of the CSV value. By default it is a ","
        """
        self.__delimiter = delimiter

    def load_by_string(self, data: str):
        """
        Loads CSV data from a string
        :param data: CSV data. Rows are separated by line breaks, The values by a delimiter (see constructor)
        :return: CsvData object containing all data. If an unlikely event of an error happened, None will be returned
        """
        return self.load_from_string_list(data.splitlines())

    def load_from_file(self, file_path: str):
        """
        Loads CSV data from an existing file.
        :param file_path: Path to the CSV file
        :return: CsvData object containing all data. If an unlikely event of an error happened, None will be returned
        """
        with open(file_path, 'r') as file:  # Opens the file
            return self.load_from_string_list(file.readlines())  # Read al lines and call "load from list"

    def get_delimiter(self):
        """
        Gets the CSV delimiter which separates the row values. The delimiter can be passed via constructor parameter
        :return: delimiter
        """
        return self.__delimiter

    def load_from_string_list(self, lines: []):
        """
         Loads CSV data from a string list
        :param lines: CSV data as line array. each array item represents a CSV line
        :return: CsvData object containing all data. If an unlikely event of an error happened, None will be returned
        """

        # Pre check paramter "Lines"
        if lines is None or len(lines) < 1:
            return None  # oh bad!

        # Create Model, which holds all loaded rows
        csv_data = CsvData()

        for line in lines:
            row = line.split(self.__delimiter)  # split lines by delimiter to get the row values
            csv_data.append(row)  # append all found rows to the model

        return csv_data  # return the model including all loaded rows
