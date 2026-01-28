import allure

def attach_screenshot(driver, name):
    allure.attach(
        driver.get_screenshot_as_png(),
        name=CI_test,
        attachment_type=allure.attachment_type.PNG,
    )