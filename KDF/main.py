from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from yaml_function import Arun_yaml

yaml_file = "C:\\Users\\aruns\\Desktop\\KDF\\config.yaml"

a = Arun_yaml(yaml_file)
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
action = ActionChains(driver)
driver.get(a.yaml_reader()['url'])
driver.implicitly_wait(10)
driver.find_element(by=By.NAME, value=a.yaml_reader()['username_Locator']).send_keys(a.yaml_reader()['username'])
driver.find_element(by=By.NAME, value=a.yaml_reader()['password_locator']).send_keys(a.yaml_reader()['password'])
driver.find_element(by=By.XPATH, value=a.yaml_reader()['submitbuttonLocator']).click()
dropdown = driver.find_element(by=By.XPATH, value=a.yaml_reader()['dropdown_locator'])
action.click(on_element=dropdown).perform()
driver.find_element(by=By.LINK_TEXT, value=a.yaml_reader()['logout_locator']).click()
driver.quit()