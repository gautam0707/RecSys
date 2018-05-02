"""
csv file helper
"""
import pandas as pd


class CsvReader:
    """
    csv file read helper
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        """
        reads the csv file specified
        :return: data frame related to csv file
        """
        return pd.read_csv(self.file_path)

    def get_file_path(self):
        """
        file path chosen to read csv from
        :return: file path
        """
        return self.file_path

    def __str__(self):
        """
        string representation of the CsvReader class
        :return: string representation of the CsvReader class
        """
        return self.file_path + " file reader instance"
