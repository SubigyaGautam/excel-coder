import pandas as pd

df = pd.read_excel('./input.xlsx')

codeTable = pd.DataFrame()
firstRowOfCodeTable = codeTable.head(0)

print('================================')
numberOfColumnsToCode = int (input("Enter number of columns to code: "))

columnIndexes = []
for i in range(numberOfColumnsToCode):
    columnIndex = int(input("Enter index of column to code: ")) - 1
    columnIndexes.append(columnIndex)

dataframeToCode = []
for indx in columnIndexes:
    dataframeToCode.append(df.iloc[1:, indx])

for df in dataframeToCode:
    columnToCode = df
    for index,value in enumerate(columnToCode):
        # print(index, value)
        userValues = (str) (value).split(',')
        # print(userValues)
        for value in userValues:
            print('==================== Processing ====================')
            if value not in firstRowOfCodeTable:
                codeTable.loc[index, value] = True
            else:
                codeTable.loc[codeTable[value] == value, value] = True
    # print(codeTable)

filledTable = codeTable.mask(codeTable == '').fillna(False)

filledTable.to_excel("coded_output.xlsx",sheet_name='code_sheet') 
print('==================== Excel file has been created with coded table ====================')




