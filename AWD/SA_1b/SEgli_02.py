import csv
import os
"""
Semesterarbeit Teil 1b - Implementation

This file contains all Python functions implemented as part of the "Semesterarbeit Teil 1b"
    Available functions:
    read_csv_file(path, seperateHeader)                  
        Reads a CSV file and returns a two dimensional list 

    Open work:
    1.  Verify proper implementation with unit tests

"""
def read_csv_file(path, seperateHeader, removeEmptyLines):
    """
    Reads a CSV File based on the given parameters.

    Args:
        path (string): 
            The path to read the CSV file from
        seperateHeader (boolean): 
            Flag to determine if the header should be separated from the body.
            If set to true, a Dictionary that contains a key for the Header and
            one for the Body
        removeEmptyLines (boolean):
            Flag to determine if empty lines should be added to the body or not.      


    Examples:
        
        >>> print( read_csv_file("simple.csv", False, True) )
        [['a;b;c'], ['d;e;f']]

    """
    #Check if the given path is available
    if os.path.exists(path) == False:
        raise ValueError('The path specified does not exist')
    
    #Check if the file is a file (and not a directory)
    if os.path.isfile(path) == False:
        raise ValueError('The path specified is not a file')    
    
    #Open the CSV file 
    #Ignore encoding since python uses unicode as default charset.   
    with open(path, newline='') as csvfile:

        try:
            # sniff the first line of the file to check its dialect
            dialect = csv.Sniffer().sniff( csvfile.readline() )
        except Exception as e:
            # catching all Exceptions is a bad thing. But the user
            # needs to be properly informed.
            raise ValueError('The path specified is not a valid CSV file. Error: ' + str(e))

        #Check if the csv.Sniffer detected a header line 
        has_header = csv.Sniffer().has_header

        # Don't forget to reset the read position back to the start of
        # the file before reading any entries
        csvfile.seek(0)

        # read csv file according to dialect
        reader = csv.reader( csvfile, dialect )

        # read header, if there is one
        if has_header:
            header = next(reader)
        
        # read data into memory
        if removeEmptyLines:
            #but exclude all empty lines
            data = [row for row in reader if row != []]
        else:
            #read the lines exactly as they are
            data = [row for row in reader]

        # close input file
        csvfile.close()

    if seperateHeader:
        #The user would like to receive a dictonary
        #to be able to process the header of the file differently
        return {
            "Header": header,
            "Body": data
        }

    if removeEmptyLines and header == []:
        #It is possible that there is a header row with actualy no values
        #in this case, do not add the header line
        return data
    
    #add back the header, because the user does not want to separate.
    data.insert(0, header)
    return data