from selenium import webdriver
import time
from selenium.common.exceptions import ElementNotVisibleException


options = webdriver.ChromeOptions()

# replace binary path with your own below

options.binary_location = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

options.add_argument('window-size=800x841')

# uncomment line 19 if you want chrome to run without window
# in background

# options.add_argument('headless') 

driver = webdriver.Chrome(chrome_options=options,executable_path="chromedriver")

driver.get('https://readtheory.org/auth/login')


username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys('Enter your username')

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('Enter your password')

login_click = driver.find_element_by_xpath('//*[@id="ajaxLogin"]').click()

x = 1
while True:
	try:
		time.sleep(6)

		answer_click = driver.find_element_by_xpath('//*[@class="answer-card"]').click()
		time.sleep(3)
		submit_click = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[2]/div[2]/div[2]/div[3]/div[2]').click()

		time.sleep(4)

		next_button = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[2]/div[2]/div[2]/div[3]/div[1]').click()

		driver.refresh()

	except ElementNotVisibleException:
		driver.refresh()