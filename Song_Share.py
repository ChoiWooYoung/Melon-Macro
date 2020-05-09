from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu")
options.add_argument('lang=ko_KR')
options.add_argument('log-level=2')
songcnt = 1;
okboy = str(songcnt)
user_id = "YOUR ACCOUNT"
user_pw = "YOUR PW"
login_url = "https://accounts.kakao.com/login?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fclient_id%3D6cfb479f221a5adc670fe301e1b6690c%26redirect_uri%3Dhttps%253A%252F%252Fmember.melon.com%252Foauth.htm%26response_type%3Dcode%26state%3DmKzaPWr6tQ%2540OGJOvAySTa5yj17LsGml7R2aIIWp5Zbiz83zd0Y5xLqBn5611Imzk3UfLqFb2D%252F5Iig%252F7KHSRQw%253D%253D%26encode_state%3Dtrue"
driver = webdriver.Chrome('CHROMEDRIVER PATH', chrome_options = options)
driver.get(login_url)
driver.find_element_by_name('email').send_keys(user_id)
driver.find_element_by_name('password').send_keys(user_pw)
os.system('cls')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/fieldset/div[8]/button').click()
time.sleep(0.5)
driver.get("https://www.melon.com")
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

#해당 앨범에 있는 노래 개수 설정
songnum = 노래개수


#SONG SHARE

for i in range (1, songnum + 1):
    driver.get('ALBUM URL')
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[3]/form/div/table/tbody/tr[' + okboy + ']/td[3]/div/a').click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/form/div/div/div[2]/div[4]/dl/dd[2]/div/button[1]').click()
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
    songcnt = songcnt + 1
    okboy = str(songcnt)

