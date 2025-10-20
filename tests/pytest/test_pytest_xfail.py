# import pytest
#
# @pytest.mark.xfail(reason="Найден баг из-за кот тест фейлится с ошибкой")
# def test_with_bug():
#     assert 1 == 2
#
# @pytest.mark.xfail(reason="Баг испоавлен, но на тесте висит маркировка xfail")
# def test_without_bug():
#     ...
# @pytest.mark.xfail(reason="Внешний сервис пока недоступен")
# def test_external_services_is_unavailable():
#     ...