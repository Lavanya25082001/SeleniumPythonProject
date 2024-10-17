import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

# this function defines command line option  --browser using pytest_adoption.default value set to chrome, it allows to specify desired browser when running test
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Specify the browser: chrome or firefox or edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
@pytest.fixture()
def setup(browser):
    global driver
    if browser=="chrome":
     driver = webdriver.Chrome()
    elif browser=="firefox":
        driver = webdriver.Firefox()
    elif browser=="edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported Browser")
    driver.maximize_window()
    yield driver
    driver.quit()


################for pytest html reports###############
################hooks for adding environment info in html report##############
def pytest_configure(config):
    config.stash[metadata_key] ['Project Name']= "Ecommerce Project, Blazedemo"
    config.stash[metadata_key]['Module Name'] = "Login Test"
    config.stash[metadata_key]['Tester Name'] = "Lavanya Gorrela"

# hook for delete/remove environment info in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('Packages', None)
    metadata.pop('JAVA_HOME',None)
    metadata.pop('Plugins', None)