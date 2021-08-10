# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Edge(r"drivers\msedgedriver.exe")

# get geeksforgeeks.org
driver.get("http://192.168.1.4/elogserver")

# write script
script = 'console.log(document.getElementById("LoginView1_Login1_UserName"))'

# generate a alert via javascript
driver.execute_async_script(script)
