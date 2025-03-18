from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



driver = webdriver.Firefox()

driver.get('https://ais.usvisa-info.com/tr-tr/niv/schedule/65987944/appointment')


close_button = driver.find_element(By.CSS_SELECTOR, ".ui-dialog-titlebar-close")
close_button.click()



username = driver.find_element(By.NAME , "user[email]")
username.send_keys() ## YOUR E MAIL ADRESS GOES HERE

password = driver.find_element(By.NAME , "user[password]")
password.send_keys() ## YOUR PASSWORD GOES HERE

checkbox = driver.find_element(By.NAME,"policy_confirmed")
driver.execute_script("arguments[0].click();", checkbox)

sendbox = driver.find_element(By.NAME,"commit")
driver.execute_script("arguments[0].click();", sendbox )    

ankara = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//select[@id='appointments_consulate_appointment_facility_id']"))
)

ankara = driver.find_element(By.XPATH,"//select[@id='appointments_consulate_appointment_facility_id']/option[text()='Ankara']")

ankara.click()


date_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "appointments_consulate_appointment_date"))
)

date_input.click()

next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='ui-datepicker-next ui-corner-all']"))
)
next_button.click()

