from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.conf import settings


class SeleniumLiveServerTestCase(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument("--width=1024")
        options.add_argument("--height=768")
        if settings.SELENIUM_TESTS_RUN_HEADLESS:
            options.set_headless()

        cls.selenium = Firefox(options=options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()