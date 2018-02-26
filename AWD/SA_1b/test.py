from SEgli_02 import *
import os

current_directory = os.path.dirname(__file__)
file = os.path.join(current_directory, 'data\\simple_no_header.csv')

data = []
try:
    data = read_csv_file(file, False, False)
except ValueError as err:
    print(err)

print(data)