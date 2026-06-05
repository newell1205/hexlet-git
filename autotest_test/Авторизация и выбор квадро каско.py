from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открытие браузера в режиме инкогнито
chrome_options = Options()
chrome_options.add_argument("--incognito")
link = "https://polis-dev.test.astrovolga.ru/"
browser = webdriver.Chrome(options=chrome_options)
browser.get(link)

wait = WebDriverWait(browser, 10)

try:
    # Нажатие кнопки "Войти по логину"
    button_login = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "span.av-button__text"))
    )
    button_login.click()

    # Ввод логина
    login_input = wait.until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    login_input.send_keys("Agent3")

    # Ввод пароля
    password_input = browser.find_element(By.ID, "password-field")
    password_input.send_keys("Agent3")

    # Нажатие кнопки "Войти"
    span_text = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Войти']"))
    )
    button = span_text.find_element(By.XPATH, "./ancestor::button")
    button.click()

    # Выбор КАСКО Квадро
    kasko_link = wait.until(
        EC.element_to_be_clickable((By.ID, "kskkvadro"))
    )
    kasko_link.click()

    # Ввод ГРЗ в поле поиска авто
    search_input = wait.until(
        EC.presence_of_element_located((By.ID, "searchCarInfo"))
    )
    search_input.send_keys("Е335ХК21")

    # Нажатие кнопки "Найти"
    search_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[not(@disabled)]//span[text()='Найти']"))
    )
    search_button.find_element(By.XPATH, "./ancestor::button").click()

    # Ожидание завершения поиска
    wait.until(EC.invisibility_of_element_located((By.ID, "searchCarInfo")))

finally:
    browser.quit()
