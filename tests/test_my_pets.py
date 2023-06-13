import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password


def test_show_my_pets():
    '''Проверка того, что переход на страницу со списком
    питомцев пользователя осуществляется'''

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email')))

    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'pass')))

    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))

    pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()

    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'