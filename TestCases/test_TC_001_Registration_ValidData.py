from Base import InitiateDriver

def test_ValidataRegistration():
    driver = InitiateDriver.startBrowser()
    driver.find_element_by_name('fld_username').send_keys('hellow')
    driver.close()
