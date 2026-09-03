import os
import pytest

from appium import webdriver
from appium.options.ios import XCUITestOptions


PCLOUDY_EMAIL = os.environ["PCLOUDY_EMAIL"]
PCLOUDY_ACCESS_KEY = os.environ["PCLOUDY_ACCESS_KEY"]
PCLOUDY_DEVICE = os.environ["PCLOUDY_DEVICE"]
PCLOUDY_APPLICATION_NAME = os.environ["PCLOUDY_APPLICATION_NAME"]

BUNDLE_ID = os.getenv(
    "IOS_BUNDLE_ID",
    "com.pcloudy.TestmunkDemo"
)

PERFORMANCE_DATA = (
    os.getenv("PCLOUDY_ENABLE_PERFORMANCE_DATA", "true").lower()
    == "true"
)


@pytest.fixture
def driver():
    options = XCUITestOptions()

    options.set_capability(
        "pCloudy_Username",
        PCLOUDY_EMAIL
    )

    options.set_capability(
        "pCloudy_ApiKey",
        PCLOUDY_ACCESS_KEY
    )

    options.set_capability(
        "pCloudy_ApplicationName",
        PCLOUDY_APPLICATION_NAME
    )

    options.set_capability(
        "pCloudy_DeviceFullName",
        PCLOUDY_DEVICE
    )

    options.set_capability(
        "pCloudy_DurationInMinutes",
        15
    )

    options.set_capability(
        "pCloudy_EnablePerformanceData",
        PERFORMANCE_DATA
    )

    options.set_capability(
        "platformName",
        "iOS"
    )

    options.set_capability(
        "automationName",
        "XCUITest"
    )

    options.set_capability(
        "bundleId",
        BUNDLE_ID
    )

    driver = webdriver.Remote(
        "https://device.pcloudy.com/appiumcloud/wd/hub",
        options=options
    )

    yield driver

    driver.quit()


def test_ios_app_launch(driver):
    print("iOS application launched successfully")

    # Basic validation
    assert driver.session_id is not None

    print("Session ID:", driver.session_id)
