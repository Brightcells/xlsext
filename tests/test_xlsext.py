# -*- coding: utf-8 -*-

import xlwt

from xlsext import xlsext


class TestXlsExtCommands(object):

    def setup_class(self):
        self.link_location = 'http://a.com'
        self.friendly_name = '测试'

    def test_hyperlink(self):
        formula = xlsext.hyperlink(self.link_location)
        assert isinstance(formula, xlwt.ExcelFormula.Formula)
        formula = xlsext.hyperlink(self.link_location, self.friendly_name)
        assert isinstance(formula, xlwt.ExcelFormula.Formula)
