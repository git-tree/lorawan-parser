# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   main
  Description :
  Author :    崔术森
  Eamil  :    deer_cui@163.com
  date：     2021/8/16
-------------------------------------------------
  Change Activity:
          2021/8/16:
-------------------------------------------------
"""
__author__ = '崔术森'

import sys
from PyQt5.QtWidgets import QApplication
from controller.controller_main import controller_main

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        mainForm = controller_main()
        mainForm.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
