import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Choose language: en or ru")

@pytest.fixture 
def language(request):
    browser_lang = request.config.getoption("language")
    return browser_lang
    
     
@pytest.fixture 
def browser(name, language):
    browser = None
    if name == "chrome":     
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    
    
    elif name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    yield browser
    browser.quit()  
       
       
