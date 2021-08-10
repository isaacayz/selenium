from selenium import webdriver

driver = webdriver.Edge("drivers\msedgedriver.exe")

driver.maximize_window()
driver.get("http://192.168.1.108")
driver.find_element_by_name("UserName").send_keys("centraladmin")
driver.find_element_by_name("Password").send_keys("")
driver.implicitly_wait(3)
driver.find_element_by_class_name("btn-add").click()
driver.find_element_by_link_text("User Management").click()

script = 'console.log(document.getElementsByTagName("tr")[10])'

driver.execute_async_script(script)
