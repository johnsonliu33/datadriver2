# encoding=utf-8
import os
from selenium import webdriver
import time
import traceback

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")) as fp:
    data = fp.readlines()

driver = webdriver.Chrome()
test_result = []
for i in range(len(data)):
    try:
        driver.get("http://www.baidu.com")
        driver.find_element_by_id("kw").send_keys(data[i].split("||")[0].strip())
        driver.find_element_by_id("su").click()
        time.sleep(3)
        assert data[i].split('||')[1].strip() in driver.page_source
        test_result.append(data[i].strip() + u"||成功\n")
        print(data[i].split('||')[0].strip() + u"搜索测试执行成功")
    except AssertionError as e:
        print(data[i].split('||')[1].strip() + u"测试断言失败")
        test_result.append(data[i].strip() + u"||断言失败\n")
        traceback.print_exc()
    except Exception as e:
        print(data[i].split('||')[1].strip() + u"测试执行失败")
        test_result.append(data[i].strip() + u"||异常失败\n")
        traceback.print_exc()

with open(u"result.txt", "w") as fp:
    fp.writelines(test_result)
driver.quit()


