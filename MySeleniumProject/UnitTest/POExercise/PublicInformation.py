class PublicInformation:
    def __init__(self, driver):
        self.driver = driver

    def openurl(self, url):
        self.driver.get(url)

    def closebrower(self):
        self.driver.quit()
