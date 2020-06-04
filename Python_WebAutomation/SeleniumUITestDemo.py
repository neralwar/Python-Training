from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.google.com')





print(driver.title)


driver.find_element_by_xpath("//input[@name='q']").send_keys('Ashish')

driver.implicitly_wait(100)

#driver.quit()





