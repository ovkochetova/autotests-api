import allure


@allure.step("Building API client")
def build_api_client():
    ...


@allure.step("Create course")
def create_course():
    ...


@allure.step("Deleting course")
def delete_course():
    ...


def test_feature():
    build_api_client()
    create_course()
    delete_course()
