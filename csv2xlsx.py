import io
import argparse
import csv
import xlsxwriter

#Argument 1: The csv file to be read 
#Argument 2: Where the .xls file is being saved
#Argument 3: Delimeter 

def convert_file():
    xlcol = 0
    xlrow = 0

    parser = argparse.ArgumentParser()
    parser.add_argument("arg1", help="Path to the input file", type=str)
    parser.add_argument("arg2", help="Path where the .xls file is being saved", type=str)
    parser.add_argument("arg3", help="Delimiter", type=str)

    args = parser.parse_args()

    filepath_in = args.arg1

    ifile = io.open(filepath_in, 'r', encoding='UTF-8', errors='ignore')

    workbook = xlsxwriter.Workbook(args.arg2)
    worksheet = workbook.add_worksheet()
    cell_format = workbook.add_format()
    cell_format.set_num_format('0.0###')

    fileline = csv.reader(ifile, dialect='excel', delimiter=args.arg3)

    for row in fileline:
        for xlcol in range(len(row)):
            worksheet.write(xlrow, xlcol, row[xlcol])
        xlrow = xlrow + 1

    workbook.close()

convert_file()