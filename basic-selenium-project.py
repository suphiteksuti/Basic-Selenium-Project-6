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


toyz_and_hobies_category = browser.find_element(By.LINK_TEXT, 'Erkek')
toyz_and_hobies_category.click()
assert "spx.com.tr/erkek-urunleri/" in browser.current_url

select_product = browser.find_element(By.XPATH, '//*[@alt="Skechers Dyna Air Erkek Ayakkabı"]')
select_product.click()

select_size = browser.find_element(By.CSS_SELECTOR, '#rptSecenek_ctl04_lblSCD_KOD1')
select_size.click()
time.sleep(3)

add_to_card = browser.find_element(By.ID, 'ctl00_u19_ascUrunDetay_dtUrunDetay_ctl00_lbfbtnSepeteAt')
add_to_card.click()
time.sleep(3)
assert "1 Ürün sepete eklendi." in browser.find_element(By.CSS_SELECTOR, 'div.custom-popup-header > span').text

go_to_cart_page = browser.find_element(By.LINK_TEXT, 'Sepete Git')
go_to_cart_page.click()
time.sleep(3)
assert "spx.com.tr/sepet/sepetim.aspx" in browser.current_url

return_homepage = browser.find_element(By.CSS_SELECTOR, '#lblBanner5758 > div > a > img')
return_homepage.click()
time.sleep(3)

browser.close()