from behave import given, when, then
from pytest_bdd import step
from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Edge()


@given("user navigates to Facebook login page")
def step_impl(context):
    context.driver.get('https://www.facebook.com/')


@when("user enter valid username and password")
def step_impl(context):
    username_field = context.driver.find_element_by_id('email')
    password_field = context.driver.find_element_by_id('pass')
    username_field.send_keys('karthis7719@gmail.com')
    password_field.send_keys('karthis')


@step("click the login button")
def step_impl(context):
    login_button = context.driver.find_element_by_name('login')
    login_button.click()


@then("Successfully logged in")
def step_impl(context):
    print("Login Successful")


@when("user enter invalid username or password")
def step_impl(context):
    print("-------Invalid Login------")


@then("user should see an error message")
def step_impl(context):
    error_message = context.driver.find_element_by_css_selector('.uiContextualLayer .uiPopover .pam')
    assert error_message.is_displayed()


def after_all(context):
    context.driver.quit()
