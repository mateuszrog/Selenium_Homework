import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from util.base_command import BaseCommand
from util.field import Field


class HelloWorldTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument("headless")

        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
        self.driver.get("https://www.saucedemo.com/")

        self.base_command = BaseCommand(self.driver)

    def test_sauce_login(self):

        self.base_command.clear_element(Field.username_textfield)
        self.base_command.send_text_to_element(Field.username_textfield, "standard_user")

        self.base_command.clear_element(Field.username_passwordfield)
        self.base_command.send_text_to_element(Field.username_passwordfield, "secret_sauce")

        self.base_command.click_element(Field.login_button)

        self.assertEqual("Products".casefold(), self.base_command.get_element_text(Field.product_span).casefold())

        self.base_command.click_element(Field.dropdown)
        self.base_command.click_element(Field.high_to_low)

        self.base_command.click_element(Field.add_first_to_card)
        self.base_command.click_element(Field.add_second_to_card)
        self.base_command.click_element(Field.add_third_to_card)

        self.base_command.click_element(Field.card)
        time.sleep(3)
        self.base_command.click_element(Field.checkout)

        self.base_command.clear_element(Field.first_name)
        self.base_command.send_text_to_element(Field.first_name, "joe")

        self.base_command.clear_element(Field.last_name)
        self.base_command.send_text_to_element(Field.last_name, "black")

        self.base_command.clear_element(Field.postal_code)
        self.base_command.send_text_to_element(Field.postal_code, "585858")

        self.base_command.click_element(Field.cont_page)

        self.assertEqual("53.97", self.base_command.get_value(Field.items))
        self.assertEqual("58.29", self.base_command.get_value(Field.total))
        self.assertEqual("4.32", self.base_command.get_value(Field.get_tax))

        substract = float(self.base_command.get_value(Field.total)) - float(self.base_command.get_value(Field.items))

        self.assertEqual(substract, float(self.base_command.get_value(Field.get_tax)))


        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

