from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
chrome_browser.implicitly_wait(5)
chrome_browser.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

assert 'Selenium Easy Demo' in chrome_browser.title #checks that we are on correct page
show_message_button = chrome_browser.find_element_by_class_name('btn-default')

assert 'Show Message' in chrome_browser.page_source # page source is the html version of the website
user_message = chrome_browser.find_element_by_id('user-message')
chrome_browser.implicitly_wait(5)
user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(user_button2)
user_message.clear()
user_message.send_keys('i am cool')
chrome_browser.implicitly_wait(5)

show_message_button.click()
chrome_browser.implicitly_wait(5)
output_message = chrome_browser.find_element_by_id('display')
assert 'i am cool' in output_message.text

chrome_browser.quit() # can also use .close()