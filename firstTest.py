from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)
#driver = webdriver.Chrome(options=chrome_options)

#driver = webdriver.Chrome(r"C:\\Users\ALVAC LIMITED\\Videos\Data science charts\\Learnings\Selenium Test\\chromedriver.exe")
driver = webdriver.Edge(r"C:\Users\ALVAC LIMITED\Videos\Data science charts\Learnings\Selenium Test\msedgedriver.exe")

driver.set_page_load_timeout(60)
driver.get("https://google.com")
input = driver.find_element_by_name("q").send_keys("Isaac Ige")

driver.find_element_by_name("btnK").click()

title = driver.getTitle()

#driver.implicitly_wait(10)
#ActionChains(driver).move_to_element(button).click(button).perform()

#find element by name
""" element = driver.find_element_by_name("btnK")
  
# create action chain object
action = ActionChains(driver)

# send keys
action.send_keys(input)
  
# click the item
action.click(on_element = element)
  
# perform the operation
action.perform() """

#driver.maximize_window()
#driver.refresh()

