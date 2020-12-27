import datetime
import time
from selenium.webdriver.common.by import By
from Utilities.BasePage import BasePage


class Shopping(BasePage):
    """By Locators"""
    COMPUTER_LINK = (By.XPATH, "//ul[@class='top-menu notmobile']//a[contains(text(),'Computers')]")
    ELECTRONICS_LINK = (By.XPATH, "//ul[@class='top-menu notmobile']//a[contains(text(),'Electronics')]")
    APPAREL_LINK = (By.XPATH, "//ul[@class='top-menu notmobile']//a[contains(text(),'Apparel')]")
    DIGITAL_DOWNLOAD_LINK = (By.XPATH, "//ul[@class='top-menu notmobile']//a[contains(text(),'Digital')]")
    JEWELLERY_LINK = (By.XPATH, "//ul[@class='top-menu notmobile']//a[contains(text(),'Jewelry')]")
    GIFT_CARD_LINK = (By.XPATH, "//ul[@class='top-menu notmobile']//a[contains(text(),'Gift')]")
    NOTEBOOK_LINK = (By.XPATH, "//ul[@class='sublist first-level']//a[contains(text(),'Notebooks')]")
    DESKTOP_LINK = (By.XPATH, "//ul[@class='sublist first-level']//a[contains(text(),'Desktops')]")
    CAMERA_LINK = (By.XPATH, "//ul[@class='sublist first-level']//a[contains(text(),'Camera')]")
    CLOTHING_LINK = (By.XPATH, "//ul[@class='sublist first-level']//a[contains(text(),'Clothing')]")
    APPLE_MACBOOK = (By.LINK_TEXT, 'Apple MacBook Pro 13-inch')
    BUILD_YOUR_DESKTOP = (By.LINK_TEXT, 'Build your own computer')
    APPLE_ICAM = (By.LINK_TEXT, 'Apple iCam')
    JEANS = (By.LINK_TEXT, "Levi's 511 Jeans")
    IF_YOU_WAIT = (By.PARTIAL_LINK_TEXT, 'If You Wait')
    NECKLESS = (By.PARTIAL_LINK_TEXT, 'Elegant Gemstone Necklace')
    GIFTCARD = (By.LINK_TEXT, '$25 Virtual Gift Card')

    HDD_RADIO = (By.CSS_SELECTOR, 'input[id=product_attribute_3_7]')
    AVAILABILITY = (By.CSS_SELECTOR, 'div[class=stock] [class=value]')
    ENTER_YOUR_PRICE = (By.CSS_SELECTOR, 'input.enter-price-input')
    QTY_TEXTBOX = (By.CSS_SELECTOR, '.qty-input')
    ADD_TO_CART = (By.CSS_SELECTOR, "input[value='Add to cart']")
    RENT = (By.CSS_SELECTOR, "input[value='Rent']")
    PRICE = (By.CSS_SELECTOR, 'div[class=product-price]>span')
    NOTIFICATION_BAR = (By.CSS_SELECTOR, "div[class='bar-notification error']>p")

    RENTAL_START_PICKER = (By.CSS_SELECTOR, "input[name='rental_start_date_40']")
    RENTAL_END_PICKER = (By.CSS_SELECTOR, "input[name='rental_end_date_40']")
    MONTH_PICKER = (By.CSS_SELECTOR, '.ui-datepicker-month')
    GO_BACK_MONTH = (By.CSS_SELECTOR, '.ui-datepicker-prev')
    GO_FORWARD_MONTH = (By.CSS_SELECTOR, '.ui-datepicker-next')

    RECIPIENT_NAME = (By.CSS_SELECTOR, '#giftcard_43_RecipientName')
    RECIPIENT_EMAIL = (By.CSS_SELECTOR, '#giftcard_43_RecipientEmail')
    YOUR_NAME = (By.CSS_SELECTOR, '#giftcard_43_SenderName')
    YOUR_EMAIL = (By.CSS_SELECTOR, '#giftcard_43_SenderEmail')
    MESSAGE = (By.CSS_SELECTOR, '#giftcard_43_Message')

    SHOPPING_CART = (By.PARTIAL_LINK_TEXT, 'Shopping cart')
    ITEM_ROWS = (By.XPATH, "//table[@class='cart']//tbody/tr")
    ITEM_LINKS = (By.XPATH, "//table[@class='cart']//tbody/tr/td[4]/a")

    SHOPPING_LIST = []
    MONTH_DICT = {'JANUARY': 1, 'FEBRUARY': 2, 'MARCH': 3, 'APRIL': 4, 'MAY': 5, 'JUNE': 6, 'JULY': 7, 'AUGUST': 8,
                  'SEPTEMBER': 9, 'OCTOBER': 10, 'NOVEMBER': 11, 'DECEMBER': 12}

    """Constructor"""
    def __init__(self, driver):
        super().__init__(driver)

    """action methods"""
    def buy_laptop(self):
        self.mouse_over(self.COMPUTER_LINK)
        self.do_click(self.NOTEBOOK_LINK)
        macbook = self.get_element_text(self.APPLE_MACBOOK)
        self.do_click(self.APPLE_MACBOOK)
        price = self.get_element_text(self.PRICE)
        self.do_send_keys(self.QTY_TEXTBOX, '1')
        self.do_click(self.ADD_TO_CART)
        min_qty_error = self.get_element_text(self.NOTIFICATION_BAR)
        self.do_send_keys(self.QTY_TEXTBOX, '2')
        qty = 2
        self.do_click(self.ADD_TO_CART)
        self.SHOPPING_LIST.append([macbook, price, qty])
        print(self.SHOPPING_LIST)
        return min_qty_error

    def buy_desktop(self):
        self.mouse_over(self.COMPUTER_LINK)
        self.do_click(self.DESKTOP_LINK)
        desktop = self.get_element_text(self.BUILD_YOUR_DESKTOP)
        self.do_click(self.BUILD_YOUR_DESKTOP)
        time.sleep(2)
        self.js_click(self.ADD_TO_CART)
        hdd_error = self.get_element_text(self.NOTIFICATION_BAR)
        self.do_click(self.HDD_RADIO)
        time.sleep(2)
        price = self.get_element_text(self.PRICE)
        self.js_click(self.ADD_TO_CART)
        qty = 1
        self.SHOPPING_LIST.append([desktop, price, qty])
        print(self.SHOPPING_LIST)
        return hdd_error

    def buy_camera(self):
        self.mouse_over(self.ELECTRONICS_LINK)
        self.do_click(self.CAMERA_LINK)
        self.do_click(self.APPLE_ICAM)
        stock = self.get_element_text(self.AVAILABILITY)
        return stock

    def buy_jeans(self):
        self.mouse_over(self.APPAREL_LINK)
        self.do_click(self.CLOTHING_LINK)
        jeans = self.get_element_text(self.JEANS)
        self.do_click(self.JEANS)
        self.do_send_keys(self.QTY_TEXTBOX, 3)
        self.js_click(self.ADD_TO_CART)
        self.SHOPPING_LIST.append([jeans, '$40.00', 3])
        print(self.SHOPPING_LIST)

    def download_song(self):
        self.do_click(self.DIGITAL_DOWNLOAD_LINK)
        song = self.get_element_text(self.IF_YOU_WAIT)
        self.do_click(self.IF_YOU_WAIT)
        self.do_send_keys(self.ENTER_YOUR_PRICE, '0.30')
        self.do_click(self.ADD_TO_CART)
        min_price_error = self.get_element_text(self.NOTIFICATION_BAR)
        self.do_send_keys(self.ENTER_YOUR_PRICE, '0.50')
        self.do_click(self.ADD_TO_CART)
        self.SHOPPING_LIST.append([song, '0.50', 1])
        print(self.SHOPPING_LIST)
        return min_price_error

    def rent_jewellery(self):
        self.do_click(self.JEWELLERY_LINK)
        neckless = self.get_element_text(self.NECKLESS)
        self.do_click(self.NECKLESS)
        """ pick two days ago as rental start date """
        rental_start_date = datetime.date.fromordinal(datetime.date.today().toordinal()-2)
        day = rental_start_date.strftime('%d')
        month = int(rental_start_date.strftime('%m'))
        year = rental_start_date.strftime('%Y')
        print(rental_start_date, day, month, year)
        self.do_click(self.RENTAL_START_PICKER)
        time.sleep(2)
        self.date_picker(month, day, self.GO_BACK_MONTH)

        """ pick three days after today as rental end date """
        rental_end_date = datetime.date.fromordinal(datetime.date.today().toordinal() + 3)
        day = rental_end_date.strftime('%d')
        month = int(rental_end_date.strftime('%m'))
        year = rental_end_date.strftime('%Y')
        print(rental_end_date, day, month, year)
        self.do_click(self.RENTAL_END_PICKER)
        time.sleep(2)
        self.date_picker(month, day, self.GO_FORWARD_MONTH)

        self.do_click(self.RENT)
        rental_date_error = self.get_element_text(self.NOTIFICATION_BAR)
        return rental_date_error

    def date_picker(self, month, day, by_locator):
        if month != self.MONTH_DICT[self.get_element_text(self.MONTH_PICKER)]:
            self.do_click(by_locator)
            time.sleep(2)
        DATE_PICKER = (By.XPATH, "//table[@class='ui-datepicker-calendar']//tr/td/a[contains(text(),'" + str(day).lstrip('0') + "')]")
        self.do_click(DATE_PICKER)

    def buy_gift_card(self, recipient_name, recipient_email, your_name, your_email, message):
        self.do_click(self.GIFT_CARD_LINK)
        giftcard = self.get_element_text(self.GIFTCARD)
        self.do_click(self.GIFTCARD)
        self.do_send_keys(self.RECIPIENT_NAME, recipient_name)
        self.do_send_keys(self.RECIPIENT_EMAIL, recipient_email)
        self.do_send_keys(self.YOUR_NAME, your_name)
        self.do_send_keys(self.YOUR_EMAIL, your_email)
        self.do_send_keys(self.MESSAGE, message)
        self.js_click(self.ADD_TO_CART)
        result = self.is_visible(self.NOTIFICATION_BAR)
        if not result:
            self.SHOPPING_LIST.append([giftcard, '25.00', 1])
            print(self.SHOPPING_LIST)
        return result

    def shopping_cart(self):
        self.do_click(self.SHOPPING_CART)
        flag = False
        for i in range(len(self.get_elements(self.ITEM_ROWS))):
            ITEM = (By.XPATH, "//table[@class='cart']//tbody/tr[" + str(i+1) + "]/td[4]/a")
            ITEM_TOTAL_PRICES = (By.XPATH, "//table[@class='cart']//tbody/tr[" + str(i+1) + "]/td[7]/span")
            item = self.get_element_text(ITEM)
            print(i, item)
            total = float(self.get_element_text(ITEM_TOTAL_PRICES).strip('$').replace(',', ''))

            unit_price = float(self.SHOPPING_LIST[i][1].strip('$').replace(',', ''))
            qty = self.SHOPPING_LIST[i][2]
            if item == self.SHOPPING_LIST[i][0]:
                if total == unit_price * qty:
                    print('Total is correct')
                    flag = True
                else:
                    flag = False
            else:
                flag = False
        return flag















