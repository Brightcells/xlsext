# -*- coding: utf-8 -*-

import xlwt

from xlsext import xlsext


class TestXlsExtCommands(object):

    def setup_class(self):
        self.link_location = 'http://a.com'
        self.friendly_name = '测试'
        self.formula1 = 'HYPERLINK("http://a.com"\r)'
        self.formula2 = 'HYPERLINK("http://a.com", "测试"\r)'

    def test_hyperlink(self):
        formula1 = xlsext.hyperlink(self.link_location)
        assert isinstance(formula1, xlwt.ExcelFormula.Formula)
        assert formula1.text() == self.formula1
        formula2 = xlsext.hyperlink(self.link_location, self.friendly_name)
        assert isinstance(formula2, xlwt.ExcelFormula.Formula)
        assert formula2.text() == self.formula2
