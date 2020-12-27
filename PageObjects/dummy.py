# import time
#
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
#
# driver.get('https://frontend.nopcommerce.com/')
# time.sleep(5)
#
# driver.switch_to.frame(0)
# select = Select(driver.find_element_by_xpath("//select[@id='customerCurrency']"))
# currency = select.options
# for i in currency:
#     print(i.text)

SHOPPING_LIST = [['Apple MacBook Pro 13-inch', '$1,800.00', 2], ['Build your own computer', '$1,415.00', 1], ["Levi's 511 Jeans", '$40.00', 3], ['If You Wait (donation)', '0.50', 1], ['$25 Virtual Gift Card', '25.00', 1]]
for i in range(len(SHOPPING_LIST)):
    print(SHOPPING_LIST[i][0])
    print(SHOPPING_LIST[i][1])
    print(SHOPPING_LIST[i][2])


