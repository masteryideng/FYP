#!/usr/bin/env python
# -*- coding:utf8 -*-

from base_tests.base_test import BaseTest
from tests.pages.demo_page import HomePage
import logging


class DemoTest(BaseTest):

    ZERO = 'com.android.calculator2:id/digit_0'
    ONE = 'com.android.calculator2:id/digit_1'
    TWO = 'com.android.calculator2:id/digit_2'
    THREE = 'com.android.calculator2:id/digit_3'
    FOUR = 'com.android.calculator2:id/digit_4'
    FIVE = 'com.android.calculator2:id/digit_5'
    SIX = 'com.android.calculator2:id/digit_6'
    SEVEN = 'com.android.calculator2:id/digit_7'
    EIGHT = 'com.android.calculator2:id/digit_8'
    NINE = 'com.android.calculator2:id/digit_9'

    POINT = 'com.android.calculator2:id/dec_point'
    EQUAL = 'com.android.calculator2:id/eq'
    DELETE = 'com.android.calculator2:id/del'
    DIVIDE = 'com.android.calculator2:id/op_div'
    MULTIPLY = 'com.android.calculator2:id/op_mul'
    MINUS = 'com.android.calculator2:id/op_sub'
    PLUS = 'com.android.calculator2:id/op_add'

    def test_calculator(self):

        self.home = HomePage(self.driver)
        self.home.click_btn(self.ONE)
        self.home.click_btn(self.NINE)
        self.home.click_btn(self.NINE)
        self.home.click_btn(self.SIX)
        self.home.click_btn(self.MULTIPLY)
        self.home.click_btn(self.FIVE)
        self.home.click_btn(self.PLUS)
        self.home.click_btn(self.ONE)
        self.home.click_btn(self.EQUAL)

        self.assertTrue(self.home.is_result_correct(1996*5+1))
