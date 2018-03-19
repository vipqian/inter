from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.PhantomJS(r'F:\F_lianxi\Scripts\phantomjs.exe')
# driver = webdriver.Firefox()


driver.get("http://www.baidu.com")
driver.implicitly_wait(20)
element = driver.find_element('css', '#u1 > a.pf')
ActionChains(driver).move_to_element(element).perform()
time.sleep(1)
driver.find_element('css', '#wrapper > div.bdpfmenu > a.setpref').click()
time.sleep(2)
s = driver.find_element('css', '#nr')
Select(s).select_by_index(0)
driver.execute_script("window.confirm = function(msg) { return true; }")
js = 'document.querySelector("#gxszButton > a.prefpanelgo").click();'
driver.execute_script(js)
time.sleep(2)
ActionChains(driver).move_to_element(element).perform()
time.sleep(1)
driver.find_element('css', '#wrapper > div.bdpfmenu > a.setpref').click()
time.sleep(2)
a = EC.element_located_to_be_selected(('css', '#nr > option:nth-child(2)'))(driver)
print(a)
print(driver.title)
