import time
from captcha import get_capcha
from PIL import Image, ImageEnhance
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def process_captcha_image(image_path):
    """Функция для изменения экспозиции и яркости капчи."""
    img = Image.open(image_path)

    enhancer_exp = ImageEnhance.Brightness(img)
    img = enhancer_exp.enhance(1.30)

    enhancer_bright = ImageEnhance.Brightness(img)
    img = enhancer_bright.enhance(1)
    img.save(image_path)


driver = webdriver.Chrome()
driver.get("https://issaold.beltelecom.by/main.html")
time.sleep(10)

element1 = driver.find_element(
    By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/form/div/div[3]/img"
)
image_path = "capcha_temp/image1.png"
element1.screenshot(image_path)

process_captcha_image(image_path)

element2 = driver.find_element(
    By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/form/div/div[3]/input"
)
element2.clear()
element2.send_keys(get_capcha())
time.sleep(10)

element3 = driver.find_element(
    By.XPATH,
    '//*[@id="root"]/div[2]/main/div/div/div[1]/section/div/form/div[2]/button[1]',
)
element3.click()

input()
