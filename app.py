from selenium import webdriver
from auth import login,create_account,scrape

page = webdriver.Firefox()

page.get('http://localhost:5000')

# do 

if login(page) == 'login error':
    create_account(page)    
elif login(page) == 'login success':
    data = scrape(page)
    print(data[0].get_attribute('innerHTML'))
    page.quit()