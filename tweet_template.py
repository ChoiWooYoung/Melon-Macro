from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('PATH')
driver.get("https://twitter.com/login")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input").send_keys('TWITTER ID')
driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input").send_keys('PW')
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div').click()
time.sleep(1)
driver.get("https://accounts.kakao.com/login?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fclient_id%3D6cfb479f221a5adc670fe301e1b6690c%26redirect_uri%3Dhttps%253A%252F%252Fmember.melon.com%252Foauth.htm%26response_type%3Dcode%26state%3DmKzaPWr6tQ%2540OGJOvAySTa5yj17LsGml7R2aIIWp5Zbiz83zd0Y5xLqBn5611Imzk3UfLqFb2D%252F5Iig%252F7KHSRQw%253D%253D%26encode_state%3Dtrue")
driver.find_element_by_name('email').send_keys('KAKAO ID')
driver.find_element_by_name('password').send_keys('PW')
time.sleep(1)
driver.get("https://melon.com")
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

//Album Share
driver.get("Album URL")
driver.find_element_by_xpath('//*[@id="albumTwitter"]').click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath('/html/body/div[2]/form/div[3]/fieldset/input').click()
driver.switch_to.window(driver.window_handles[0])

//Video View and Share
driver.get("Video URL")
driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div[3]/div[1]/div[2]/button[3]').click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath('/html/body/div[2]/form/div[3]/fieldset/input').click()
driver.switch_to.window(driver.window_handles[0])

//Photo View and Share
driver.get("https://www.melon.com/artist/photo_detail.htm?artistId=2398653&photoId=80093498&orderBy=NEW")
//LOOP THIS
driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div[4]/div[3]/div/div[1]/div[2]/div[3]/ul/li[3]/button/span').click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath('/html/body/div[2]/form/div[3]/fieldset/input').click()
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div[4]/div[3]/button[2]/span').click()
driver.switch_to.window(driver.window_handles[0]) 

