from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import FROM, TO, DEPARTURE_DATE, AP_125, SUBMIT, \
COMFORT_TOURIST, BUY_TICKETS, ACCEPT_CONDITIONS, DROPDOWN_PASSANGER, \
PASSANGER_NUMBER, NEXT_PAGE
import time

def get_element(driver, xpath):
    return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))

def make_click(driver, xpath):
    button = get_element(driver, xpath)
    button.click()
    time.sleep(1)
    return 

def input_text(driver, xpath, text):
    input_layer = get_element(driver, xpath)
    input_layer.clear()
    input_layer.send_keys(text)
    time.sleep(1)

def main():
    driver = webdriver.Chrome()

    driver.get("https://www.cp.pt/passageiros/en")
    time.sleep(1)
    
    make_click(driver, BUY_TICKETS)
    input_text(driver, FROM, 'Lisboa Oriente')
    input_text(driver, TO, 'Porto Campanha')
    input_text(driver, DEPARTURE_DATE, '24 September, 2025')


    swich = get_element(driver, COMFORT_TOURIST)
    if "active" not in swich.get_attribute("class"):
        swich.click()
    time.sleep(1)

    make_click(driver, DROPDOWN_PASSANGER)
    make_click(driver, PASSANGER_NUMBER)
    make_click(driver, SUBMIT)
    make_click(driver, AP_125)
    make_click(driver, ACCEPT_CONDITIONS)
    make_click(driver, NEXT_PAGE)

    driver.quit()


if __name__ == "__main__":
    main()
