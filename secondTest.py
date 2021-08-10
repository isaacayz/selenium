from selenium import webdriver
#Password="Ayo08180"



path = "drivers\msedgedriver.exe"
driver = webdriver.Edge(path)
driver.get("http://192.168.1.4/elogserver")
driver.find_element_by_name("LoginView1$Login1$UserName").send_keys("general")
driver.find_element_by_name("LoginView1$Login1$Password").send_keys("")
driver.find_element_by_name("LoginView1$Login1$LoginButton").click()
driver.implicitly_wait(5)
driver.find_element_by_link_text("Customer Management").click()
driver.find_element_by_link_text("Create").click()
driver.find_element_by_link_text("GIT").click()
driver.implicitly_wait(5)
driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtName").send_keys("Layo's Closet")
driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtAddress").send_keys('Ikosi-Ketu, Lagos')
driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtPhoneNumber").send_keys("08071982054")
driver.implicitly_wait(5000)
driver.maximize_window()
driver.refresh()
#title = driver.get()
#print(title)
#driver.find_element_by_id("ctl00_LoginView2_LoginStatus2").click()






