import os.path

from  datetime import datetime
import pytest
import webdriver_manager.chrome
from selenium import webdriver
@pytest.fixture()
def setup(browser,headless):

    try:
        if browser == "chrome":
            from selenium.webdriver.chrome.service import Service
            from selenium.webdriver import ChromeOptions

            service = Service(executable_path=webdriver_manager.chrome.ChromeDriverManager().install())
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Chrome(service=service,options=options)


        elif browser =="edge":
            from selenium.webdriver.edge.service import Service
            from webdriver_manager.microsoft import EdgeChromiumDriverManager
            from selenium.webdriver import EdgeOptions

            options=EdgeOptions()
            if headless:
                options.add_argument("--headless")
            service=Service(executable_path=EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service,options=options)


        elif browser == "firefox":
            from selenium.webdriver.firefox.service import Service
            from webdriver_manager.firefox import GeckoDriverManager
            from selenium.webdriver import FirefoxOptions

            options=FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            service = Service(executable_path=GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service,options=options)

        driver.implicitly_wait(10)  # Wait before throwing an exception
        print(f"Launching {browser} browser{' in headless mode' if headless else ''}...")
        yield driver
        driver.quit()  # Quit to clean up

    except Exception as e:
        pytest.fail(f"WebDriver setup failed: {e}")


def pytest_addoption(parser):
    """add command line argument for selecting browser"""
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     choices=["chrome", "firefox", "edge"],
                     help="choose browser : chrome,firefox,edge")
    parser.addoption("--headless",
                     action="store_true",
                     help="Run browser in headless mode")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def headless(request):
    return request.config.getoption("--headless")

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath=os.path.abspath(os.path.curdir)+"\\reports\\report_"+ datetime.now().strftime("%d-%m-%Y %H-%M-%S"+".html")


