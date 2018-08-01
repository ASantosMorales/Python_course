import xlrd
xls_file = xlrd.open_workbook('C:/Users/uidk7321/Python_course-master/data_source.xlsx')
data = xls_file.sheet_by_index(0)

text_file_construction = '#include "something.h"\n\n'

for row_xls_file in range(1, 9):
    text_file_construction = text_file_construction + \
                             '#define ' + \
                             data.cell(row_xls_file, 0).value + '\t'*3 + \
                             '({})'.format(data.cell(row_xls_file, 1).value) + \
                             (str(data.cell(row_xls_file, 2).value)[:-2] if ('float' in str(type(data.cell(row_xls_file, 2).value))) else str(data.cell(row_xls_file, 2).value)) + \
                             '\n'
print(text_file_construction)
                        
text_file = open('calibrations.h', 'w')
text_file.write(text_file_construction)
text_file.close()