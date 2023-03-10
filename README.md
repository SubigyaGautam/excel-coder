pip3 install pandas
pip install openpyxl

22 24

1) The input excel filename should be input.xlsx
2) execute the following command "python index.py"
3) Enter number of columns of the excel file to generate the coding (This column should contain comma separated values)
4) Enter column number (for example 20th column of input file)
5) Wait for the process to finish ,open the excel file 'coded_output' to see the coded table in sheet 'code_sheet'

Example: 

Input table

 |    B|       C               |D    E   F
1|    2|      dog,cat,mice     |4    5   rice,veg
2|    9|     tiger,cat,mice    |4    5   meat,veg
3|    3|      lion             |4    5   rice
4|    4|      cat              |4    5   rice
5|    5|     mice              |4    5   meat,veg
6|    8|     dog,cat,mice      |4    5   veg
7|    6|      dog,cat,mice     |4    5   veg

Output table 

 | dog    cat    mice   tiger   lion    rice   meat    veg
1| TRUE   TRUE   TRUE   FALSE   FALSE   TRUE   FALSE    TRUE
2| FALSE  TRUE   TRUE   TRUE   FALSE   FALSE   TRUE     TRUE
3| FALSE  FALSE  FALSE  FALSE  TRUE   TRUE    FALSE    FALSE
4| FALSE  TRUE   FALSE  FALSE  FALSE   TRUE   FALSE     FALSE
5| FALSE  FALSE  TRUE   FALSE  FALSE  FALSE    TRUE     TRUE
6| TRUE    TRUE  TRUE   FALSE  FALSE  FALSE   FALSE     TRUE
7| TRUE    TRUE  TRUE   FALSE  FALSE  FALSE   FALSE     TRUE

Input sequence for the about input/ output will be
> python index.py
> Enter number of columns to code: 2
> Enter column number to code: 3
> Enter column number tocode: 6

