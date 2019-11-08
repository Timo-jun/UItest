import os
import sys

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
from selenium import webdriver
from page.official_website.login_page import LoginPage
from common.AutoLog import AutomationLog
from operation.login_page_op import LoginPageOp
import time
import pytest


# # @pytest.mark.usefixtures('kpp')
# class TestAa:
#     def test_01(self,kpp):
#         print(kpp)
#         assert 0 == 1
#
#     def test_02(self,kpp):
#         print(kpp)
#         assert 0==1


