# import random
#
# import pytest
#
# PLATFORM = "Windows"
#
#
# @pytest.mark.flaky(reruns=3, reruns_delay=2)
# def test_reruns():
#     assert random.choice([True, False])
#
# @pytest.mark.flaky(reruns=3, reruns_delay=2)
# class TestReruns:
#     def test_reruns1(self):
#         assert random.choice([True, False])
#
#     def test_reruns2(self):
#         assert random.choice([True, False])
#
#
# @pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PLATFORM=="Windows")
# def test_rerun_with_condition():
#     assert random.choice([True, False])
