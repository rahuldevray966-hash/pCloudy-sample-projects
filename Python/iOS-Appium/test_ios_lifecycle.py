import os

from appium import webdriver
from appium.options.ios import XCUITestOptions


PCLOUDY_EMAIL = os.environ["PCLOUDY_EMAIL"]
PCLOUDY_ACCESS_KEY = os.environ["PCLOUDY_ACCESS_KEY"]
PCLOUDY_DEVICE = os.environ["PCLOUDY_DEVICE"]
PCLOUDY_APPLICATION_NAME = os.environ["PCLOUDY_APPLICATION_NAME"]

IOS_BUNDLE_ID = os.getenv(
    "IOS_BUNDLE_ID",
    "com.pcloudy.TestmunkDemo"
)


def test_ios_app_launch():

    options = XCUITestOptions()

    # pCloudy authentication
    options.set_capability(
        "pCloudy_Username",
        PCLOUDY_EMAIL
    )

    options.set_capability(
        "pCloudy_ApiKey",
        PCLOUDY_ACCESS_KEY
    )

    # Application uploaded to pCloudy
    options.set_capability(
        "pCloudy_ApplicationName",
        PCLOUDY_APPLICATION_NAME
    )

    # Exact pCloudy device
    options.set_capability(
        "pCloudy_DeviceFullName",
        PCLOUDY_DEVICE
    )

    # Session duration
    options.set_capability(
        "pCloudy_DurationInMinutes",
        15
    )

    # iOS
    options.set_capability(
        "platformName",
        "iOS"
    )

    options.set_capability(
        "automationName",
        "XCUITest"
    )

    # Application bundle ID
    options.set_capability(
        "bundleId",
        IOS_BUNDLE_ID
    )

    driver = None

    try:

        print("----------------------------------------")
        print("Starting iOS Appium session")
        print(f"Device      : {PCLOUDY_DEVICE}")
        print(f"Application : {PCLOUDY_APPLICATION_NAME}")
        print(f"Bundle ID   : {IOS_BUNDLE_ID}")
        print("----------------------------------------")

        driver = webdriver.Remote(
            "https://device.pcloudy.com/appiumcloud/wd/hub",
            options=options
        )

        print("Appium session started successfully")
        print(f"Session ID: {driver.session_id}")

        assert driver.session_id is not None

        print("iOS application launched successfully")

    finally:

        if driver:

            driver.quit()

            print("Appium session closed")
