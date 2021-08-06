import time

name = 'Mwelwa Bot'
email = 'mwelwabot@gmail.com'
password = 'mwelwabot'

def login(page):
    if page.title == 'Login':
        email_input = page.find_element_by_id('email')
        password_input = page.find_element_by_id('password')
        login = page.find_element_by_xpath('/html/body/div/div/form/button')
        
        email_input.send_keys(email)
        password_input.send_keys(password)
        login.click()
        time.sleep(3)
        print('clicked ')
        
        try:
            login_error = page.find_element_by_xpath('/html/body/div/div/form/p')
            if login_error:
                return 'login error'
            else:
                return 'login success'
        except:
            return 'login success'
        
    else:
        return 'login success'
    
def create_account(page):
    print(page.title)
    go_to_sign_up = page.find_element_by_xpath('/html/body/div/div/p[2]/span/a')
    go_to_sign_up.click()
    time.sleep(2)
    
    if page.title == 'Create Account':
        name_input = page.find_element_by_name('name')
        email_input = page.find_element_by_name('email')
        password_input = page.find_element_by_name('password')
        confirm_input = page.find_element_by_name('confirm')
        sign_up = page.find_element_by_xpath('/html/body/div/div/form/button')
        
        name_input.send_keys(name)
        email_input.send_keys(email)
        password_input.send_keys(password)
        confirm_input.send_keys(password)
        
        sign_up.click()
        time.sleep(4)
        print('clicked sign up')
        
        continue_btn = page.find_element_by_xpath('/html/body/div/a')
        if continue_btn:
            continue_btn.click()
        
        sign_up_error = page.find_element_by_xpath('/html/body/div/div/form/p')
        if sign_up_error:
            return 'ERROR OCCURRED IN SIGN UP'
        else:
            scrape(page)
        
def scrape(page):
    elements = page.find_elements_by_xpath('//*[@id="post"]')
    return elements