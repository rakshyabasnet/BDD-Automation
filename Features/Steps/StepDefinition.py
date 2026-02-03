from behave import *
from selenium.webdriver import Chrome
from behave.api.pending_step import StepNotImplementedError
@given(u'User is on Registration Page')
def step_imp(context):
    context.driver=Chrome()
    context.driver.get('https://www.facebook.com/r.php')
    context.driver.maximize_window()

@when(u'User enters firstname')
def step_imp(context):
    context.driver.find_element('name','firstname').send_keys('Deekshya')

@when(u'User enters lastname')
def step_imp(context):
    context.driver.find_element('name','lastname').send_keys('Basnet')


@when(u'User enters month')
def step_imp(context):
    context.driver.find_element('xpath', '//select[@name="birthday_month"]').send_keys("Jan")

@when(u'User enters day')
def step_imp(context):
    context.driver.find_element('xpath', '//select[@name="birthday_day"]').send_keys("18")


@when(u'User enters year')
def step_imp(context):
    context.driver.find_element('xpath', '//select[@name="birthday_year"]').send_keys("2003")

@when(u'User click gender')
def step_imp(context):
    context.driver.find_element('xpath', '//input[@value="2"]').click()


@when(u'User enters email')
def step_imp(context):
    context.driver.find_element('xpath', "//input[@name='reg_email__']").send_keys("deek@gmail.com")


@when(u'User enters password')
def step_imp(context):
    context.driver.find_element('xpath', "//input[@name='reg_passwd__']").send_keys("dee123")


@when(u'User click on signup button')
def step_imp(context):
    context.driver.find_element('xpath', "//button[@name='websubmit']").click()


@then(u'User should be registered successfully')
def step_imp(context):
    print("Registered Successfully")


@when(u'User enters duplicate email')
def step_imp(context):
    raise StepNotImplementedError('User enters duplicate email')


@then(u'User should be registered with  duplicate email successfully')
def step_imp(context):
    raise StepNotImplementedError('Then User should be registered with  duplicate email successfully')


