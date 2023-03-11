from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from allure import step


def test_wiki_app():
    with step('Starter screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(have.text('The Free Encyclopedia'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/option_label')).should(have.text('English'))

    with step('Add language'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/addLangContainer')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/section_header_text')).should(have.text('Your languages'))
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.LinearLayout'))[2].click()
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.LinearLayout'))[5].click()
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/wiki_language_title')).should(have.size_greater_than(1))

    with step('Go to Explore screen'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Navigate up')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_card_header_title')).should(have.text('Today on Wikipedia'))

    with step('Go to Main page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/footerActionButton')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_wiki_error_text')).should(have.exact_text('An error occurred'))

