#working with excel
#openpyxl => package used for working with excel
# import openpyxl

# """ while working with excel there is need to create a worksheet object """

# import openpyxl

# wb = openpyxl.load_workbook("Hydra project pt 2.xlsx")
# print(wb.sheetnames)

# wb1 = wb['FY 2020 Final Products ']
# cell = wb1["A1"]
# for row in range(1, wb1.max_row + 1):
#     for column in range(1, wb1.max_column + 1):
#         cell = wb1.cell(row, column)
#         # print(cell.value)
# wb.save("messed.xlsx")

# """ important principle in programming, command query separation
# methods should either be commands or query, but not both

# """

import numpy as np #heavily used in scientific computation
#takes less memory than the built in python list

array = np.array([[1,2,3], [2,3,3]])
array2 = np.random.random((3,4))
print(array2)
print(array.shape)

#creating joins
# working with financial data


