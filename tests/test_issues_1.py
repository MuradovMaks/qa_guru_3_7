import pytest
from selene.support.shared import browser
from selene.support import by
from selene import be
import allure
from allure_commons.types import Severity


@allure.tag('Search Issues(Selene)')
@allure.label("owner", "MuradovMaks")
@allure.epic('WEB')
@allure.link("https://github.com/")
@allure.feature('Поиск issues в репозитории Selene')
@allure.story('Проверка,что пользователь может найти конкретный номер issues')
@allure.severity(severity_level=Severity.CRITICAL)
def test_github_issues_selene():
    browser.config.window_height = 1920
    browser.config.window_width = 1620
    browser.open('https://github.com/')
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys('MuradovMaks/qa_hm_3_3')
    browser.element('.header-search-input').submit()
    browser.element(by.link_text('MuradovMaks/qa_hm_3_3')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text('#6')).should(be.visible)

    browser.quit()


@allure.tag('Search Issues(lambda)')
@allure.label("owner", "MuradovMaks")
@allure.epic('WEB')
@allure.link("https://github.com/")
@allure.feature('Поиск issues в репозитории (lambda)')
@allure.story('Проверка,что пользователь может найти конкретный номер issues')
@allure.severity(severity_level=Severity.BLOCKER)
def test_github_issues_lambda():
    with allure.step('Открыть GitHub и задать размеры окна браузера'):
        browser.config.window_height = 1920
        browser.config.window_width = 1620
        browser.open('https://github.com/')

    with allure.step('Клик на окно поиска и ввод MuradovMaks/qa_hm_3_3 '):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').send_keys('MuradovMaks/qa_hm_3_3')
        browser.element('.header-search-input').submit()

    with allure.step('Ищем название issue по тексту в котором находится номер з'):
        browser.element(by.link_text('MuradovMaks/qa_hm_3_3')).click()
        browser.element('#issues-tab').click()
        browser.element(by.partial_text('#6')).should(be.visible)

    with allure.step('Выход из браузера'):
        browser.quit()


@allure.tag('Search Issues(decorator)')
@allure.label("owner", "MuradovMaks")
@allure.epic('WEB')
@allure.link("https://github.com/")
@allure.feature('Поиск issues в репозитории (decorator)')
@allure.story('Проверка,что пользователь может найти конкретный номер issues(decorator)')
@allure.severity(severity_level=Severity.BLOCKER)
def test_selene_decorator():
    open_github('https://github.com/')
    search_repository('MuradovMaks/qa_hm_3_3')
    search_issues_with_repository('MuradovMaks/qa_hm_3_3', '#6')
    quit_this_browser()


@allure.step('Открыть GitHub и задать размеры окна браузера')
def open_github(url):
    browser.config.window_height = 1920
    browser.config.window_width = 1620
    browser.open(url)


@allure.step('Клик на поиск и ввод репозитория')
def search_repository(repo):
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys(repo)
    browser.element('.header-search-input').submit()


@allure.step('Поиск названия задачи по тексту в котором находится видимый номер')
def search_issues_with_repository(repo, number):
    browser.element(by.link_text(repo)).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text(number)).should(be.visible)


@allure.step('Закрытие браузера')
def quit_this_browser():
    browser.quit()
