from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user_name = ''
password = ''
driver = webdriver.Chrome('') #크롬 실행파일 경로 입력
driver.get("") #사이트 주소 입력
element = driver.find_element_by_id('login_id')
element.send_keys(user_name)
element = driver.find_element_by_id('login_pass')
element.send_keys(password)
element.send_keys(Keys.RETURN)