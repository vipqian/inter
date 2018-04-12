import requests
import unittest
import ddt
from interface.common.read_excel import ReadExcel
from interface.common.logger import logger

excelpath = r"F:\automation\interface\parameterization\password.xlsx"
sheet_register = 'register'
sheet_login = 'login'
sheet_get_code = 'get_code'
# sheet_
data_register = ReadExcel(excelpath, sheet_register).data_list()
data_login = ReadExcel(excelpath, sheet_login).data_list()
data_get_code = ReadExcel(excelpath, sheet_get_code).data_list()


@ddt.ddt
class TestLong(unittest.TestCase):
    """登录页面"""
    log = logger

    @ddt.data(*data_register)
    def test_register(self, data):
        """注册"""
        try:
            url = "http://pc-api.power.com/index.php?c=Login&a=register"
            play_data = {
                "mobile": data['mobile'],
                "code": "445",
                "password": data['password']
            }
            r = requests.post(url, data=play_data, verify=True)
            result = r.json()['errstr']
            self.log.info("\n结果：%s \n测试数据： %s" % (result, data))
            self.assertEqual(data['result'], result)
        except Exception as msg:
            self.log.info(str(msg))
            raise
        # print(data['mobile'])

    @ddt.data(*data_login)
    def test_login(self, data):
        """登录页面"""
        try:
            self.log.info(data)
            url = 'http://pc-api.power.com/index.php?c=Login&a=register'
            play_data = {
                "mobile": data['mobile'],
                "code": data['code'],
                "password": data['password']
            }
            r = requests.post(url, data=play_data, verify=True)
            result = r.json()['errstr']
            self.assertEqual(result, data['result'])
        except Exception as msg:
            self.log.info(str(msg))
            raise

    @ddt.data(*data_get_code)
    def test_get_code(self, data):
        """获取验证码"""
        try:
            self.log.info(data)
            url = "http://pc-api.power.com/index.php?c=Login&a=sendCode"
            play_data = {
                'mobile': data['mobile']
            }
            r = requests.post(url, data=play_data, verify=True)
            result = r.json()['errstr']
            self.assertIn(result, data['result'])
        except Exception as msg:
            self.log.info(str(msg))
            raise

    # @ddt.data()
    # def test_login(self):

if __name__ == '__main__':
    unittest.main()
