from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://accounts.bukalapak.com/login?comeback=https%3A%2F%2Fwww.bukalapak.com%2F")

driver.find_element_by_id("LoginID").send_keys("bagus")
driver.find_element_by_id("submit_button").click()