import ddt
import unittest
from interface.common.read_excel import ReadExcel

excelpath = r"F:\automation\interface\parameterization\password.xlsx"
sheet = "Sheet2"
data = ReadExcel(excelpath, sheet).data_list()
# print(data[0])
# print(data)


@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(*data)
    def test(self, data):
        print(data['class'])
        # pass

if __name__ == '__main__':
    unittest.main()


