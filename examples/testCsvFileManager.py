
from C2RM.io.CSVFileManager import CSVFileManager

if __name__ == "__main__":
    fm = CSVFileManager("../data/coins_sept10_dataset_3.csv", 0)
    ir = fm.getiterator()

    while ir.hasnextrow():
        row = ir.nextrow()
        print row
        print "----------------------"
        break
    print len(fm.data)