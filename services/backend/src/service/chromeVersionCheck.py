import chromedriver_autoinstaller as ca
import os
import logging

# Set logger
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())


DRIVER_DIR = 'chromeDrivers'


# Get chrome browser version
def getChromeBrowserVersion():

    return ca.get_chrome_version().split('.')[0]


# Install chrome driver
def installChromeDriver():

    chrome_ver = getChromeBrowserVersion()

    # Set driver instll path
    if not os.path.exists(DRIVER_DIR):
        os.mkdir(DRIVER_DIR)

    driver_path = ''

    # Check if chrome driver is installed or not
    if os.path.exists(driver_path):
        logger.info(f'Chrome driver is installed: {driver_path}')
    else:
        logger.info(f'Install the Chrome driver(ver: {chrome_ver})')
        driver_path = ca.install(path=DRIVER_DIR)

    return driver_path
