#import the CsvReader file in order to use the read_csv_file function
from SEgli_02_CsvReader import *
#import the module os in order to shorten file paths
import os

#Set the current directory to the same as this file
current_directory = os.path.dirname(__file__)
#relative from the python file path, enter the path of the CSV file to read
file = os.path.join(current_directory, 'data\\simple.csv')

#prepare the result variable
data = []
try:
    #read the CSV file
    data = read_csv_file(file, False, False)
except ValueError as err:
    #If anything goes wrong read_csv_file raises a ValueError
    print(err)

#Continue here by accessing the parsed data:
print(data)