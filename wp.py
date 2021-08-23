from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

nombre = "Nano Spector"
msg = "non spam text"
spam = 1

input("Scan qr")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(nombre))

user.click()

msg_box = driver.find_element_by_class_name('_2FbwG')


msg_box.send_keys(msg)
button = driver.find_element_by_class_name('compose-btn-send')
button.click()
