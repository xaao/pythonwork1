from selenium import webdriver
import pytest
import os

driver = None


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """


    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
    if (report.skipped and xfail) or (report.failed and not xfail):
        dirpng = r'./report1/png/'
    if os.path.exists(dirpng) and os.path.isdir(dirpng):
        pass
    else:
        os.mkdir(dirpng)
    file_name = dirpng + report.nodeid.replace("::", "_") + ".png"
    file_name1 = r'./png/' + report.nodeid.replace("::", "_") + ".png"
    _capture_screenshot(file_name)
    if file_name:
        html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                'onclick="window.open(this.src)" align="right"/></div>' % file_name1
        extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver

    if driver is None:
        driver = webdriver.Firefox()
    return driver