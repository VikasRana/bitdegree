import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome("PATH_OF_YOUR_CHROMEDRIVER_HERE e.g. D:\\chromedriver_win32\\chromedriver.exe")

u = 'YOUR_EMAIL_HERE'
p = 'YOUR_PASS_HERE'

driver.get('https://www.bitdegree.org/login')

driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div/div[1]/div/div[3]/button').click()
driver.find_element_by_xpath('//*[@id="input-email"]').click()
driver.find_element_by_xpath('//*[@id="input-email"]').send_keys(u)
driver.find_element_by_xpath('//*[@id="input-password"]').click()
driver.find_element_by_xpath('//*[@id="input-password"]').send_keys(p)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div/div[1]/div/div[3]/button').click()
time.sleep(2)

for rnge in range(1, 13):
	link = 'https://www.bitdegree.org/courses?page={}'.format(rnge)
	driver.get(link)
	for k in range(1, 12):
		enrollLink = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div/div[2]/div[2]/div[1]/div[{}]/div/div[2]/a[2]'.format(k)).click()
		try:
			costly = driver.find_element_by_xpath('//*[@id="app-platform"]/div/div/div[2]/div/div/div[1]/div[2]/div/div/button')
			if costly:
				driver.execute_script("window.history.go(-1)")
			else:
				pass
		except NoSuchElementException as e:
			pass
		try:
			notEnr = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/form/div/div/div[1]/div/div/button').click()
			driver.execute_script("window.history.go(-2)")
		except NoSuchElementException as e:
			driver.execute_script("window.history.go(-1)")