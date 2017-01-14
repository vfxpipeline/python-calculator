"""
Name: 
Author :  Rajiv Sharma
Developer Website : www.technicaldirector.in
Developer Email   : rajiv@technicaldirector.in
Date Started : 
Date Modified :
Description : 

Download Application from : www.technicaldirector.in/downloads
Source Code Website : www.github.com/vfxpipeline/renderbox
Free Video Tutorials : www.youtube.com/vfxpipeline

Copyright (c) 2016, RAJIV SHARMA(www.TechnicalDirector.in) . All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.

    * Neither the name of RAJIV SHARMA(www.TechnicalDirector.in) nor the names of any
      other contributors to this software may be used to endorse or
      promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
__author__ = 'Rajiv Sharma'
import sys
from PyQt4 import QtGui
from ui import main


class Calculator_Class(main.Ui_MainWindow, QtGui.QMainWindow):
    def __init__(self):
        super(Calculator_Class, self).__init__()
        self.setupUi(self)
        self.pb_0.clicked.connect(lambda: self.display_screen('0'))
        self.pb_1.clicked.connect(lambda: self.display_screen('1'))
        self.pb_2.clicked.connect(lambda: self.display_screen('2'))
        self.pb_3.clicked.connect(lambda: self.display_screen('3'))
        self.pb_4.clicked.connect(lambda: self.display_screen('4'))
        self.pb_5.clicked.connect(lambda: self.display_screen('5'))
        self.pb_6.clicked.connect(lambda: self.display_screen('6'))
        self.pb_7.clicked.connect(lambda: self.display_screen('7'))
        self.pb_8.clicked.connect(lambda: self.display_screen('8'))
        self.pb_9.clicked.connect(lambda: self.display_screen('9'))
        self.pb_dot.clicked.connect(lambda: self.display_screen('.'))
        self.pb_add.clicked.connect(lambda: self.display_screen(' + '))
        self.pb_minus.clicked.connect(lambda: self.display_screen(' - '))
        self.pb_divide.clicked.connect(lambda: self.display_screen(' / '))
        self.pb_multiply.clicked.connect(lambda: self.display_screen(' * '))
        self.pb_clear.clicked.connect(self.screen_LE.clear)
        self.pb_back.clicked.connect(self.screen_LE.backspace)
        self.pb_equal.clicked.connect(self.calculation)
        self.screen_LE.setReadOnly(True)

    def display_screen(self, value):
        """
        this function will insert data to screen
        :param value:
        :return:
        """
        self.screen_LE.insert(value)

    def calculation(self):
        """
        this is a calculation function that will take values from screen
        and pass the values to maths function
        :return:
        """
        screen_value = str(self.screen_LE.text()).split(' ')
        val1 = float(screen_value[0])
        operator = screen_value[1]
        val2 = float(screen_value[2])
        result = self.maths(val1, val2, operator)
        self.screen_LE.setText(str(result))

    def maths(self, val1, val2, operator):
        """
        this function will take arguments and return output
        :param val1:
        :param val2:
        :param operator:
        :return:
        """
        val1 = float(val1)
        val2 = float(val2)
        if operator is '+':
            return val1 + val2
        elif operator is '-':
            return val1 - val2
        elif operator is '/':
            return val1 / val2
        elif operator is '*':
            return val1 * val2

if __name__ == '__main__':
    qapp = QtGui.QApplication(sys.argv)
    calc = Calculator_Class()
    calc.show()
    qapp.exec_()
