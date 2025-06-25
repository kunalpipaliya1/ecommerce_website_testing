from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//*[@name='q']").clear()
element = driver.find_element(By.XPATH, "//*[@name='q']")
element.send_keys("5g mobile")
element.send_keys(Keys.ENTER)
driver.implicitly_wait(10)

print("mobile searched")

# Price
xpath_price_list = "//*[@class='Nx9bqj _4b5DiR']"
price_element = driver.find_elements(By.XPATH, xpath_price_list)
prices = []

for i in price_element:
    text = i.text.strip().replace('₹', '') .replace(',','')
    if text.isdigit():
        prices.append(int(text))

if prices:
    highest = max(prices)
    lowest = min(prices)
    print(lowest, "Lowest value of mobile")
    print(highest, "Highest value of mobile")
else:
    print("No prices found.")
    
# Model find name

xpath_model_list = "//*[@class='KzDlHZ']"
model_element = driver.find_elements(By.XPATH, xpath_model_list)

model = []

for mo in model_element:
    textmo = mo.text.strip()
    if textmo:
        model.append(textmo)
    
if model:
    high = max(model)
    low = min(model)
    print(high, "Highest model number")
    print(low, "Lowest model number")

else:
    print("No model found.")
