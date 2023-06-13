import pytest
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password


def test_show_all_pets():
    '''Проверка карточек питомцев всех пользователей
    на наличие фото, имени и описания (порода и возраст)'''

    pytest.driver.implicitly_wait(10)

    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'

    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    assert names[0].text != ''

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ',' in descriptions[i].text
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0