from selenium import webdriver

username = 'username'
password = 'password'

url = 'https://www.facebook.com/'

driver = webdriver.Chrome("/Users/main_dir/Downloads/chromedriver")

driver.get(url)

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()
