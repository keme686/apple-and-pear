
import pandas as pd


class CSVFileManager(object):
    """
    provides interface to intact with data in a csv file
    """

    def __init__(self, filename, headerrow, sep=","):
        '''
        Initializes file manager with basic access interfaces
        - data: pandas DataFrame that contains the content of csv file
        - iterator: CSVFileIterator object that can be used to iterate over rows or columns of 'data' DataFrame
        :param filename: path to .csv file  :String
        :param headerrow: row number that corresponds to the header (column names) of the file :int
        :param sep: separator of column values :string, regex
        '''
        self.filename = filename
        self.headerrow = headerrow
        self.sep = sep

        self.data = self.readdata()
        self.iterator = self.getiterator()

    def getiterator(self):
        return CSVFileIterator(self.data)

    def readdata(self):
        '''
        Load csv file to panda DataFrame object
        :return: panda DataFrame object
        '''
        data = pd.read_table(self.filename, sep=self.sep, skip_blank_lines=True)
        return data


class CSVFileIterator(object):
    """
    Provided Iteration over csv file loaded to pandas DataFrame
    """
    def __init__(self, csvfile):
        """
        initializes row and column pointers
        - columnnames: header of csv file
        - rowpointer: current location of row pointer
        - columnpointer: current location of column pointer

        :param csvfile: panda DataFrame object
        """
        self.csvfile = csvfile
        self.columnnames = self.csvfile.columns
        self.rowpointer = -1
        self.columnpointer = -1

    def hasnextrow(self):
        """
        Check if there is next row in the 'csvfile'
        :return: True if there exist more row values, False otherwise
        """
        if len(self.csvfile) > self.rowpointer + 1:
            return True
        else:
            return False

    def nextrow(self):
        """
        Gets next row values
        :return: row values as panda Series object.
        Raise EndOfRowException if end of rows reached.
        """
        self.rowpointer += 1
        if len(self.csvfile) > self.rowpointer:
            rrow = self.csvfile.ix[self.rowpointer]
            return rrow
        else:
            raise EndOfRowException("End of rows reached! No more rows found!")

    def hasnextcolumn(self):
        """
        Check if there exist next column in csvfile
        :return: True if there exist more column(s), False otherwise
        """
        if len(self.columnnames) > self.columnpointer + 1:
            return True
        else:
            return False

    def nextcolumn(self):
        """
        Get the next column values
        :return: column values as panda Series object.
        Raise EndOfColumnException if end of columns has reached!
        """
        self.columnpointer += 1
        if len(self.columnnames) > self.columnpointer:
            return self.csvfile[self.columnnames[self.columnpointer]]
        else:
            raise EndOfColumnException("End of Column reached! No more columns found!")


class OutOfDataException(Exception):
    pass


class EndOfRowException(OutOfDataException):
    pass


class EndOfColumnException(OutOfDataException):
    pass



