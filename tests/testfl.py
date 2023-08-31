import pytest
from selenium.webdriver.support.select import Select

from PageObject.Homepage import Homepage


@pytest.mark.usefixtures("setup")
class testone:

    def test_fl(self):
        homepage = Homepage(self.driver)
        homepage.getName().send_keys("kart hi")
        homepage.getEmail().send_keys("karthi1234@gmail.com")
        homepage.getPassword().send_keys("kart hi123")
        homepage.getCheckbox().click()
        gender = Select(homepage.getGender())
        gender.select_by_index(1)

        homepage.getSubmit().click()

        message = homepage.getMsgSuccess().text
        print(message)
