import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from utilities import ReadConfig

@pytest.fixture()

def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Screenshot on Failure",
            attachment_type=AttachmentType.PNG
        )

@pytest.hookimpl(hookwrapper=True,tryfirst=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item,"rep_" + rep.when,rep)
    #return rep

@pytest.fixture()
def setup_and_teardown(request):

    browser = ReadConfig.read_configurations("basic info","browser")
    global driver
    driver =  None

    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()

    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()

    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("provide a valid browser name ")


    driver.maximize_window()
    app_url = ReadConfig.read_configurations("basic info","url")

    driver.get(app_url)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield
    driver.quit()