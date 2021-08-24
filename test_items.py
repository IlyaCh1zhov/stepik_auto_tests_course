import pytest
import time
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

@pytest.mark.parametrize('name', ["chrome", "firefox"])
def test_user_should_see_buy_element(browser):       
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(3)
    button_list = browser.find_elements_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(button_list) == 1, f"Button must be present, expected !=0, got {len(button_list)}" 
   
    