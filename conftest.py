from driver import Driver
import allure

from pluggy import HookspecMarker
hookspec = HookspecMarker("pytest")

def pytest_sessionfinish(session, exitstatus):
    Driver.driver.quit()

def pytest_runtest_teardown(item):
    print("//Test successful Executed//")
    node = item.obj
    image_name = "1.png"
    image = Driver.driver.get_screenshot_as_file(image_name)

    allure.attach.file(
        image_name,
        name=node.__name__+"-step__screenshot",
        attachment_type=allure.attachment_type.PNG,
    )
