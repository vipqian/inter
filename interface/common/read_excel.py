# coding=utf-8
"""
author:
time:
brief:
"""
import xlrd


class ReadExcel():
    """
    读取xlsx文件返回多个字典列表
    """
    def __init__(self, xlsxpath, sheetname):
        self.data = xlrd.open_workbook(xlsxpath)
        self.table = self.data.sheet_by_name(sheetname)
        self.key = self.table.row_values(0)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols

    def data_list(self):
        if self.rowNum < 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                valuse = self.table.row_values(j)
                s = {}
                for x in range(self.colNum):
                    s[self.key[x]] = valuse[x]
                r.append(s)
                j += 1
            return r

if __name__ == '__main__':
    excelpath = r"F:\automation\interface\parameterization\password.xlsx"
    sheet = "Sheet2"
    data = ReadExcel(excelpath, sheet).data_list()
    print(data)
