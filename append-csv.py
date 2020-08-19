# Append as many CSV files are in a directory into a single csv file.

import os, fnmatch
import pandas as pd

ls_files = os.listdir('.')
ls_files.remove('NCDC-all.csv')
extension = "*.csv"
read_rows = 0
sum_rows = 0

for read_file in ls_files :

    if read_file == 'append-csv.py' :
        None

    elif fnmatch.fnmatch(read_file, extension) :
        read_rows = pd.read_csv(read_file, dtype=str, index_col=0)
        read_rows.to_csv('NCDC-all.csv', mode='a', header=False)
        rows =len(read_rows)
        sum_rows = rows + sum_rows
        print('Appending ' +str(rows), "rows from file: ", read_file, "to the dataset...")

    else :
        print("Rows from other files:", read_file, "was not appended, does not have csv extension.")

print("")
print("Total rows appended to the dataset: " +str(sum_rows))