# append-csv
Append as many CSV files are in a directory into a single csv file.

This script is useful when:
- Have more than one CSV file with many rows and need to consolidate those rows in a single file.
- Your device does not have enough resources to have Excel appending the quantity of rows.
- Your connection is too low or it is used for another thing different to upload the CSV files to Excel online.

### Guidelines

The script does not append the columns name of the files wich rows you going to append. The columns should be in the new file as is explained in the following lines.

I included the following files in the repo in case you want to test:
- NCDC-TT.csv: rows to be appended.
- NCDC-S-Lucia.csv: rows to be appended.
- NCDC-all.csv: file where rows of NCDC-TT.csv and NCDC-S-Lucia.csv will be appended.

1. Create a new CSV file with only 1 row that contains the name of the columns. See the file NCDC-all.csv included in the repo. If you are in macOS or Linux, it is simple by using head. Copy the first line (or row) of one of the CSV files that you going to append, into the new file NCDC-all.csv.

`mike@DS42T:~$head -n 1 NCDC-TT.csv > NCDC-all.csv`

2. Now your file where you going to append the rows of every CSV file is ready. I am using the name NCDC-all.csv for this example only, you can name this file as you desire.

3. In the script, just replace the the NCDC-all.csv with the name you give to the file in the step 1.

4. Try to have only the CSV files you going to append and the file you created in the step 1, in the same directory together with the script.

5. Now you can run the script in the directory where you have the CSV files:

`mike@DS42T:~$python append-csv.py`

The example:
```
mike@macOS append-csv % rm NCDC-all.csv 
mike@Miguels-MacBook-Pro append-csv % head -n 1 NCDC-TT.csv > NCDC-all.csv
mike@Miguels-MacBook-Pro append-csv % python append-csv.py                
Appending 6852 rows from file:  NCDC-TT.csv to the dataset...
Rows from other files: README.md was not appended, does not have csv extension.
Rows from other files: .git was not appended, does not have csv extension.
Appending 3693 rows from file:  NCDC-S-Lucia.csv to the dataset...

Total rows appended to the dataset: 10545
(base) miguelramirez@Miguels-MacBook-Pro append-csv % 
```

### Notes

1. I has read in somewhere that CSV files are not intended to be for more than 2 GB. I think more than this it could be better other type of resource.

Hope this script could be useful for you.