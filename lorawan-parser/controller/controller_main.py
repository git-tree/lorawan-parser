# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   controller_main
  Description :
  Author :    崔术森
  Eamil  :    deer_cui@163.com
  date：     2021/8/12
-------------------------------------------------
  Change Activity:
          2021/8/12:
-------------------------------------------------
"""
__author__ = '崔术森'

import json
import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import *
from core.lorawan_a2b_hex import a2b_hex
from core.lorawan_parser import parse_phy_pdu
from ui.lorawanui import Ui_MainWindow


class Stream(QObject):
    """Redirects console output to text widget."""
    newText = pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))


class MyEncoder(json.JSONEncoder):
    """
    格式化返回的dict,bytearr,bytes等
    """

    def default(self, obj):
        if isinstance(obj, bytearray):
            return obj.hex()
        if isinstance(obj, bytes):
            return int(obj.hex(),16)
        return json.JSONEncoder.default(self, obj)


class controller_main(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(controller_main, self).__init__(parent)
        self.setupUi(self)
        sys.stdout = Stream(newText=self.onUpdateText)
        self.ap = None
        self.opt = None

    def onUpdateText(self, text):
        """Write console output to text widget."""
        cursor = self.txt_show_pain.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.txt_show_pain.setTextCursor(cursor)
        self.txt_show_pain.ensureCursorVisible()

    @pyqtSlot()
    def on_btn_parse_clicked(self):
        """
        开始解析按钮点击事件
        :return:
        """
        self.startParse()

    @pyqtSlot()
    def on_check_v_clicked(self):
        """
        复选框点击事件
        """
        self.startParse()

    @pyqtSlot(int)
    def on_cmb_version_activated(self,p):
        """
        下拉框change事件
        """
        self.startParse()

    def startParse(self):
        """
        解析报文方法
        """
        if self.txt_phy_pain.toPlainText() == "":
            self.txt_show_pain.setPlainText("请输入报文")
            self.txt_phy_pain.setFocus()
            return
        self.ap = None
        self.ap = ArgumentParser(
            description="""
                LoRaWAN PHY Payload parser.
                The input must be hex strings.
                You can use stdin to pass the string.
                """,
            formatter_class=ArgumentDefaultsHelpFormatter)
        self.ap.add_argument("-d", action="append_const", dest="_f_debug", default=[],
                             const=1, help="increase debug mode.")
        # 清空历史数据
        self.txt_show_pain.setPlainText("")
        # 获取 phy
        phy = self.txt_phy_pain.toPlainText()
        # 获取复选框是否选中
        if self.check_v.isChecked():
            # 选中
            self.ap.add_argument("-v", action="store_true", dest="verbose",
                                 help="enable verbose mode.", default=True)
        else:
            self.ap.add_argument("-v", action="store_true", dest="verbose",
                                 help="enable verbose mode.", default=False)
        # print("PHYPayload: {0}\n".format(phy))
        # 获取nwkskey
        nwkskey = self.txt_nwkskey.text()
        # 获取appskey
        appskey = self.txt_appskey.text()
        # 获取version
        version = self.cmb_version.currentText()
        self.opt = self.ap.parse_args()
        self.opt.debug_level = len(self.opt._f_debug)
        try:
            result = parse_phy_pdu(
                phy_pdu=a2b_hex(phy, string_type=""),
                nwkskey=a2b_hex(None if nwkskey is None or nwkskey == "" else nwkskey),
                appskey=a2b_hex(None if appskey is None or appskey == "" else appskey),
                version=version,
                option=self.opt
            )
            print("\n===json数据展示===")
            print(json.dumps(result, indent=4, cls=MyEncoder, separators=(',', ':')))
            self.moveCursorToStart()
        except:
            info = sys.exc_info()
            self.txt_show_pain.setPlainText(str(info[1]))
            self.moveCursorToStart()

    def moveCursorToStart(self):
        """
        展示的textview焦点在最前
        """
        cursor = self.txt_show_pain.textCursor()
        cursor.movePosition(QTextCursor.Start)
        self.txt_show_pain.setTextCursor(cursor)
