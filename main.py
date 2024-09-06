from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

X_EMAIL = "YourEmal@email.com"
USER_NAME = "Your_X_User_Name"
X_PASSWORD = "YourXPassword"
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
chrome_options.add_experimental_option("detach", True)


class XPostNews:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.news = ""
        self.news_link = ""

    def get_news(self):
        self.driver.get("https://news.ycombinator.com/news")
        time.sleep(2)

        self.news = self.driver.find_element(By.CSS_SELECTOR, value=".titleline a").text
        self.news_link = self.driver.find_element(By.CSS_SELECTOR, value=".titleline a").get_attribute("href")

    def x_log_in(self):
        self.driver.get("https://x.com")
        time.sleep(2)

        cookies = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div[1]/div/div/div/div[2]'
                                                           '/button[1]/div')
        cookies.click()
        msg_close = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div[2]/div/div/div/button')
        msg_close.click()

        time.sleep(2)
        log_in = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]'
                                                          '/div/div/div[3]/div[3]/a/div')
        log_in.click()
        time.sleep(5)
        email = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/'
                                                         'div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]'
                                                         '/div/input')
        email.click()
        email.send_keys(X_EMAIL)
        time.sleep(2)
        email.send_keys(Keys.ENTER)

        time.sleep(2)
        user_name = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                             'div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/'
                                                             'div/div[2]/div/input')
        user_name.click()
        user_name.send_keys(USER_NAME)
        time.sleep(2)
        user_name.send_keys(Keys.ENTER)

        time.sleep(2)
        password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                            'div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/'
                                                            'label/div/div[2]/div[1]/input')
        password.click()
        password.send_keys(X_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(10)
        post = f"{self.news}\n News link: {self.news_link}"
        x_post = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/'
                                                          'div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div'
                                                          '/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div'
                                                          '/div/div/div[2]/div/div/div/div')
        x_post.click()
        x_post.send_keys(post)
        time.sleep(10)
        post_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
                                                               'div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                               'div[2]/div[2]/div/div/div/button/div/span/span')
        post_button.click()
        self.driver.quit()


bot = XPostNews()
bot.get_news()
bot.x_log_in()
