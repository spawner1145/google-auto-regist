#改解释器ctrl+shift+p
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string
import subprocess 
from selenium.webdriver.chrome.options import Options

file_path = "C:/Users/spawner/Desktop"
TimesToRun = int(input('Input the number of times to run: '))

#随机字符串
def random_str(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

for i in range(TimesToRun):
    random_length = random.randint(3, 5)
    a = random_str(random_length)
    b = random_str(random_length)
    c = random_str(12)

    # 打开浏览器
    
    browser_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    incognito_arg = '--incognito'
    
    subprocess.Popen([browser_path,incognito_arg,'--remote-debugging-port=9222'])
    
    options = Options()
    options.add_argument("--incognito")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    #这里记得改chrome的路径 ，不然会报错
    driver = webdriver.Chrome(executable_path='C:\\Users\\spawner\\Desktop\\edgedriver_win64\\chromedriver-win64\\chromedriver.exe', options=options)

    driver.delete_all_cookies()
    
    driver.get("https://accounts.google.com/signup")

    time.sleep(1)

    # 姓名
    lastname = driver.find_element(By.XPATH, '//*[@id="lastName"]')
    lastname.send_keys(a)
    firstname = driver.find_element(By.XPATH, '//*[@id="firstName"]')      
    firstname.send_keys(b)
    
    next_button = driver.find_element(By.XPATH, '//*[@id="collectNameNext"]/div/button/span')
    next_button.click()

    time.sleep(1)

    # 填信息
    year_select = driver.find_element(By.XPATH, '//*[@id="year"]')
    year_select.click()
    year_select.send_keys("1970")

    month_select = driver.find_element(By.XPATH, '//*[@id="month"]')
    month_select.click()
    month_select.send_keys("1")

    day_select = driver.find_element(By.XPATH, '//*[@id="day"]')
    day_select.click()
    day_select.send_keys("1")

    gender_select = driver.find_element(By.XPATH, '//*[@id="gender"]')
    gender_select.click()
    gender_select.send_keys("男")
    gender_select.click()

    next_button = driver.find_element(By.XPATH, '//*[@id="birthdaygenderNext"]/div/button')
    next_button.click()

    time.sleep(3)

    next_button = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div[1]/div[1]/div/span/div[1]/div/div[1]')
    next_button.click()
    next_button = driver.find_element(By.XPATH, '//*[@id="next"]/div/button')
    next_button.click()
    
    time.sleep(3)

    # 密码
    pwd = driver.find_element(By.XPATH, '//*[@id="passwd"]/div[1]/div/div[1]/input')
    pwd.send_keys(c)
    confirm_pwd = driver.find_element(By.XPATH, '//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
    confirm_pwd.send_keys(c)
    
    next_button = driver.find_element(By.XPATH, '//*[@id="createpasswordNext"]/div/button')
    next_button.click()

    time.sleep(3)

    next_button = driver.find_element(By.XPATH, '//*[@id="recoverySkip"]/div/button')
    next_button.click()
    next_button = driver.find_element(By.XPATH, '//*[@id="next"]/div/button')
    next_button.click()
    time.sleep(1)
    next_button = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div[1]/div/div/button')
    next_button.click()

    with open(file_path, "w") as f:
        f.write(a+b+'@gmail.com','    ',c,'\n')

    # 关闭浏览器
    driver.quit()

