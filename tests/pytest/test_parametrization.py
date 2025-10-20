# import pytest
# from _pytest.fixtures import SubRequest
#
# # @pytest.mark.parametrize("number", [1,2,3, -1])
# # def test_numbers(number: int):
# #     assert number > 0
#
# @pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9), (4, 16)])
# def test_several_numbers(number: int, expected: int):
#     assert number ** 2 == expected
#
# @pytest.mark.parametrize("os", ["macos", "linux", "windows", "debian"])
# @pytest.mark.parametrize("host", ["https://dev.company.com", "http://stable.company.com", "https://preprod.company.com"])
# def test_multiple_parameters(host: str, os: str):
#     assert len (os + host) > 0
#
# @pytest.fixture(params=[
#     "https://dev.company.com",
#     "http://stable.company.com",
#     "https://preprod.company.com"
# ])
# def host(request: SubRequest)->str:
#     return request.param
#
# def test_host(host: str):
#     print(f"Running on host: {host}")
#
# @pytest.mark.parametrize("user", ["Alice", "Zara"])
# class TestOperations:
#     def test_user_with_operations (self, user: str):
#         print(f"user_with_operations: {user}")
#     def test_user_without_operations(self, user: str):
#         print(f"user_without_operations: {user}")
#
# users = {
#     "+7000000011": "user with money",
#     "+7000000022": "user with no money",
#     "+7000000033": "user with bank account",
# }
#
#
# @pytest.mark.parametrize(
#     "phone_number",
#     users.keys(),
#     ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"
# )
# def test_identifiers(phone_number: str):
#     pass