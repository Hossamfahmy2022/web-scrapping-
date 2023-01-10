from selenium import webdriver
driver = webdriver.Chrome(r'D:/AI-ITI/chromedriver_win32/chromedriver.exe')
driver.get('https://www.amazon.eg/s?k=samsung&rh=p_89%3Asamsung&language=en&ref=SQEG-WEB-SR301')
products = driver.find_elements('xpath',"//span[@class='a-size-base-plus a-color-base a-text-normal']")
prices = driver.find_elements("xpath","//span[@class='a-price-whole']")
for i in products:
    print(i.text)
for i in prices:
    print(i.text)
