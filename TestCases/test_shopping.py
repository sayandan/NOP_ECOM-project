import pytest
from PageObjects.Shopping import Shopping
from Utilities.BaseTest import BaseTest


class TestShopping(BaseTest):

    def test_01_laptop(self):
        self.logger = self.get_logger()
        self.logger.info("**************** TEST SHOPPING *************")
        self.logger.info("**************** test_01_laptop *************")
        self.shopping = Shopping(self.driver)
        msg = self.shopping.buy_laptop()
        if msg == 'The minimum quantity allowed for purchase is 2.':
            self.logger.info("*********laptop min qty verified ******** ")
            assert True
        else:
            self.logger.error("**********verifying min qty failed ********")
            self.driver.save_screenshot('../Reports/test_01_laptop.png')
            assert False

    def test_02_desktop(self):
        self.logger = self.get_logger()
        self.logger.info("**************** test_02_desktop *************")
        self.shopping = Shopping(self.driver)
        msg = self.shopping.buy_desktop()
        if msg == 'Please select HDD':
            self.logger.info("**************desktop error verified **********")
            assert True
        else:
            self.logger.error("**************desktop error not verified **********")
            self.driver.save_screenshot('../Reports/test_02_desktop.png')
            assert False

    def test_03_camera(self):
        self.logger = self.get_logger()
        self.logger.info("**************** test_03_camera *************")
        self.shopping = Shopping(self.driver)
        msg = self.shopping.buy_camera()
        if msg == 'Out of stock':
            self.logger.info("************** out of stock msg verified *****")
            assert True
        else:
            self.logger.error("************** out of stock msg not verified *****")
            self.driver.save_screenshot('../Reports/test_03_camera.png')
            assert False

    def test_04_jeans(self):
        self.logger = self.get_logger()
        self.logger.info("**************** test_04_jeans *************")
        self.shopping = Shopping(self.driver)
        self.shopping.buy_jeans()

    def test_05_digital_download(self):
        self.logger = self.get_logger()
        self.logger.info("**************** test_05_digital_download *************")
        self.shopping = Shopping(self.driver)
        self.shopping.download_song()

    def test_06_rent_neckless(self):
        self.logger = self.get_logger()
        self.logger.info("**************** test_06_rent_neckless *************")
        self.shopping = Shopping(self.driver)
        msg = self.shopping.rent_jewellery()
        if msg == 'Rental start date should be the future date':
            self.logger.info('************ verified rental start date should be future **********')
            assert True
        else:
            self.logger.error('************ rental start date should be future not verified **********')
            self.driver.save_screenshot('../Reports/test_06_rent_neckless.png')
            assert False

    @pytest.mark.parametrize("recipient_name, recipient_email, your_name, your_email, message, expected_result",
    [("John", "john email", "123", "as3@email", "", "FAIL"),
     ("", "john@email.com", "David", "as3@email", "Msg", "FAIL"),
     ("John", "john email", "123", "as3@email", "" , "FAIL"),
     ("John", "john@email.com", "David", "as3@email.com", "Happy Birthday", "PASS")])
    def test_07_buy_gift_card(self, recipient_name, recipient_email, your_name, your_email, message, expected_result):
        self.logger = self.get_logger()
        self.logger.info('***************test_07_buy_gift_card************')
        self.shopping = Shopping(self.driver)
        result = self.shopping.buy_gift_card(recipient_name, recipient_email, your_name, your_email, message)
        if result and expected_result == 'FAIL':
            self.logger.info('************* verified required info for giftcard *********** ')
            assert True
        elif result and expected_result == 'PASS':
            self.logger.error('************* not verified required info for giftcard *********** ')
            self.driver.save_screenshot('../Reports/test_07_buy_gift_card.png')
            assert False
        elif not result and expected_result == 'PASS':
            self.logger.info('************* verified required info for giftcard *********** ')
            assert True
        elif not result and expected_result == 'FAIL':
            self.logger.error('************* not verified required info for giftcard *********** ')
            self.driver.save_screenshot('../Reports/test_07_buy_gift_card.png')
            assert False
        self.logger.info(result)

    def test_08_shopping_cart(self):
        self.logger = self.get_logger()
        self.logger.info('*************** test_08_shopping_cart ************')
        self.shopping = Shopping(self.driver)
        if self.shopping.shopping_cart():
            self.logger.info('************** Shopping cart verified ********')
            assert True
        else:
            self.logger.error('************** Shopping cart not verified ********')
            self.driver.save_screenshot('../Reports/test_08_shopping_cart.png')
            assert False





