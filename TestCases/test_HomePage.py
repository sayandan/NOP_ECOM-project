from PageObjects.HomePage import HomePage
from Utilities.BaseTest import BaseTest
from Utilities.TestData import TestData


class TestHomePage(BaseTest):

    def test_01_page_title(self):
        self.logger = self.get_logger()
        self.logger.info('*************** TestHomePage *******')
        self.logger.info('*************** test_01_page_title *******')
        self.logger.info('*************** verifying page title ***********')
        self.home_page = HomePage(self.driver)
        actual_title = self.home_page.get_title(TestData.PAGE_TITLE)
        print(actual_title)
        if actual_title == 'nopCommerce demo store':
            self.logger.info('**********title verified successfully ********')
            assert True
        else:
            self.logger.error('******verifying title failed *********')
            self.driver.save_screenshot('../Reports/test_homePageTitle.png')
            assert False

    def test_02_currency(self):
        self.logger = self.get_logger()
        self.logger.info('******** test_02_currency*****')
        self.logger.info('******** verifying default currency*****')
        self.home_page = HomePage(self.driver)
        default_currency = self.home_page.get_default_currency()
        print(default_currency)
        if default_currency == 'US Dollar':
            self.logger.info('***************verifying default currency successful*******')
            assert True
        else:
            self.logger.error('***********verifying default currency failed *************')
            self.driver.save_screenshot('../Reports/test_defaultCurrency.png')
            assert False

