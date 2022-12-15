import allure
from allure_commons.types import Severity

def test_dynamic_labels():
    allure.dynamic.tag("Search Issues")
    allure.dynamic.label("owner","MuradovMaks")
    allure.dynamic.epic('WEB')
    allure.dynamic.link('https://github.com/')
    allure.dynamic.feature('Поиск Ишью в репозитории')
    allure.dynamic.story('Проверка что пользователь не может найти Ишью')
    allure.dynamic.severity(severity_level=Severity.BLOCKER)


@allure.tag('Search Issues')
@allure.label("owner", "MuradovMaks")
@allure.epic('WEB')
@allure.link("https://github.com/")
@allure.feature('Поиск issues в репозитории Selene')
@allure.story('Проверка,что пользователь может найти конкретный номер issues')
@allure.severity(severity_level=Severity.CRITICAL)
def test_static_labels():
    pass