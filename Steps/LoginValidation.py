from behave import *

use_step_matcher("re")


@given("user navigates to Facebook login page")
def step_impl(context):
    context.driver.get('https://www.facebook.com/')


@when('user enter username "karthis7719@gmail\.com" and password "karthis"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When user enter username "karthis7719@gmail.com" and password "karthis"')


@step("click the login button")
def step_impl(context):
    login_button = context.driver.find_element_by_name('login')
    login_button.click()


@when('user enter username "karthi@gmail\.com" and password "abcde"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When user enter username "karthi@gmail.com" and password "abcde"')
