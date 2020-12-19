from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver

path = "C:\\Users\\suphi.teksut\\Desktop\\selenium\\chromedriver.exe"
browser = webdriver.Chrome(path)
browser.implicitly_wait(10)
browser.maximize_window()
browser.get("https://www.spx.com.tr")
assert "https://www.spx.com.tr/" in browser.current_url


class Locators:

    def category_erkek(self):
        browser.find_element(By.LINK_TEXT, 'ERKEK').click()

    def cat_page_assert(self):
        assert "https://www.spx.com.tr/erkek/" in browser.current_url

    def select_product(self):
        browser.find_element(By.XPATH, '//*[@alt="Skechers Dyna Air Erkek Ayakkabı"]').click()

    def select_size(self):
        browser.find_element(By.CSS_SELECTOR, '#rptSecenek_ctl04_lblSCD_KOD1').click()

    def add_to_card(self):
        browser.find_element(By.ID, 'ctl00_u19_ascUrunDetay_dtUrunDetay_ctl00_lbfbtnSepeteAt').click()

    def add_to_card_assert(self):
        assert "1 Ürün sepete eklendi." in browser.find_element(By.CSS_SELECTOR, 'div.custom-popup-header > span').text

    def go_to_cart_page(self):
        browser.find_element(By.LINK_TEXT, 'Sepete Git').click()

    def cart_page_assert(self):
        assert "spx.com.tr/sepet/sepetim.aspx" in browser.current_url

    def return_homepage(self):
        browser.find_element(By.CSS_SELECTOR, '#lblBanner5758 > div > a > img').click()

locators = Locators()
locators.category_erkek()
locators.cat_page_assert()
locators.select_product()
locators.select_size()
locators.add_to_card()
locators.add_to_card_assert()
locators.go_to_cart_page()
locators.cat_page_assert()
locators.return_homepage()
time.sleep(3)

browser.close()
