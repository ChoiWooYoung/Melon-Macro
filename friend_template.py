//멜론 친구를 이용한 공유 매크로
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('PATH')
driver.get("https://accounts.kakao.com/login?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fclient_id%3D6cfb479f221a5adc670fe301e1b6690c%26redirect_uri%3Dhttps%253A%252F%252Fmember.melon.com%252Foauth.htm%26response_type%3Dcode%26state%3DmKzaPWr6tQ%2540OGJOvAySTa5yj17LsGml7R2aIIWp5Zbiz83zd0Y5xLqBn5611Imzk3UfLqFb2D%252F5Iig%252F7KHSRQw%253D%253D%26encode_state%3Dtrue")
driver.find_element_by_name('email').send_keys('KAKAO ID')
driver.find_element_by_name('password').send_keys('PW')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/fieldset/div[8]/button').click()
time.sleep(0.5)
driver.get("https://www.melon.com")
driver.switch_to.window(driver.window_handles[1])           
driver.close()
driver.switch_to.window(driver.window_handles[0])

//Album Share
driver.get("ALBUM PATH")
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/div[4]/dl/dd[3]/div/button[1]').click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div[1]/div[1]/p/button/span/span').click()
driver.switch_to.window(driver.window_handles[2])
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/ul/li[1]/div/div[2]/table/tbody/tr[1]/td[1]/div/input').click()
driver.find_element_by_xpath('/html/body/div/div/p/button[1]/span/span').click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div[2]/div[2]/textarea').send_keys("SEND MSG")
driver.find_element_by_xpath('/html/body/div/div/div[2]/button[1]/span/span').click()
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

//Video View & Share
driver.get("VIDEO PATH")
driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div[3]/div[1]/div[2]/button[1]').click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div[1]/div[1]/p/button/span/span').click()
driver.switch_to.window(driver.window_handles[2])
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/ul/li[1]/div/div[2]/table/tbody/tr[1]/td[1]/div/input').click()
driver.find_element_by_xpath('/html/body/div/div/p/button[1]/span/span').click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div[2]/div[2]/textarea').send_keys("SEND MSG")
driver.find_element_by_xpath('/html/body/div/div/div[2]/button[1]/span/span').click()
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

//Photo View & Share
//Set First Path
driver.get("PHOTO PATH")
//LOOP THIS METHOD
driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div[4]/div[3]/div/div[1]/div[2]/div[3]/ul/li[1]/button').click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div[1]/div[1]/p/button/span/span').click()
driver.switch_to.window(driver.window_handles[2])
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/ul/li[1]/div/div[2]/table/tbody/tr[1]/td[1]/div/input').click()
driver.find_element_by_xpath('/html/body/div/div/p/button[1]/span/span').click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div[2]/div[2]/textarea').send_keys("SEND MSG")
driver.find_element_by_xpath('/html/body/div/div/div[2]/button[1]/span/span').click()
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
