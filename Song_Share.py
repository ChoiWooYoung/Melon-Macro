try:
    from selenium import webdriver
    import time
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(chrome_options=options, executable_path="/usr/local/share/chromedriver")
    driver.get("https://member.melon.com/muid/web/login/login_inform.htm")
    driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[1]/button').click()
    user_id = "YOUR KAKAO ID"
    user_pw = "YOUR KAKAO PW"
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_name('email').send_keys(user_id)
    driver.find_element_by_name('password').send_keys(user_pw)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/fieldset/div[8]/button').click()
    time.sleep(0.5)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    albumcnt = Song Number in that album
    while True:
        songcnt = 1
        okboy = str(songcnt)
        for i in range (1, albumcnt+1):
            driver.get('ALBUM URL')
            driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[3]/form/div/table/tbody/tr[' + okboy + ']/td[3]/div/a').click()
            driver.implicitly_wait(5)
            driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/form/div/div/div[2]/div[4]/dl/dd[2]/div/button[2]').click()
            driver.switch_to.window(driver.window_handles[1])
            driver.implicitly_wait(5)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            songcnt = songcnt + 1
            okboy = str(songcnt)

except KeyboardInterrupt:
    print("KeyboardInterruption..")
    driver.quit()

except NoSuchElementException:
    driver.quit()
    print("NoSuchElementException")
