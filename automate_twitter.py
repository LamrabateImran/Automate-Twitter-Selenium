from selenium import webdriver	
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Creating an instance webdriver
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=Options())
driver.get('https://www.twitter.com')

# Sign in
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span'))).click()

print("Login in Twitter")
# Enter User Name
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input'))).send_keys('ImranLamrabate')
# Click on Next
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span'))).click()

# Reads password from a text file because
# saving the password in a script is just silly.
with open('test.txt', 'r') as myfile:
	Password = myfile.read().replace('\n', '')

# Send keys to the Password input
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'))).send_keys(Password)
# Click on Login Button
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/span/span'))).click()
print("Login Successful")

# Click on Explore
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div/div[2]'))).click()
except:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div/div'))).click()

# send keys to search Bar 
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input'))).send_keys("@Torsslayer")
print("Search Successful")
# Click on profil
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="typeaheadDropdown-2"]/div[3]/div/div/div/div[2]/div/div/div/div[1]/div/div[1]/span/span'))).click()
# Follow
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/div/div/span/span'))).click()
print("Follow Successful")

# closing the driver
driver.close()
