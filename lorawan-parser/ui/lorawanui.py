# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lorawanUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QDateTime, Qt
from PyQt5.QtGui import QTextCursor, QCursor
from PyQt5.QtWidgets import QLabel, QMenu
from frameUtils.Utils import BubbleLabel


class My_QPainTextEdit(QtWidgets.QPlainTextEdit):
    def __init__(self, parent=None):
        super(My_QPainTextEdit, self).__init__(parent)

    def leaveEvent(self, QMouseEvent):
        self.setPlainText(self.toPlainText().strip().replace(" ", "").replace("\n", "").replace("\t", ""))
        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.setTextCursor(cursor)


class My_QLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(My_QLineEdit, self).__init__(parent)
        self.setClearButtonEnabled(True)

    def leaveEvent(self, QMouseEvent):
        self.setText(self.text().strip().replace(" ", "").replace("\n", "").replace("\t", ""))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txt_appskey = My_QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.txt_appskey.setFont(font)
        self.txt_appskey.setObjectName("txt_appskey")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_appskey)
        self.gridLayout.addLayout(self.formLayout_3, 4, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 368, 155))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.txt_show_pain = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.txt_show_pain.setFont(font)
        self.txt_show_pain.setObjectName("txt_show_pain")
        self.txt_show_pain.setReadOnly(True)
        self.gridLayout_3.addWidget(self.txt_show_pain, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 8, 1)
        # self.txt_phy_pain = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_phy_pain = My_QPainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.txt_phy_pain.setFont(font)
        self.txt_phy_pain.setObjectName("txt_phy_pain")
        self.txt_phy_pain.setFocus()
        self.gridLayout.addWidget(self.txt_phy_pain, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.btn_parse = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.btn_parse.setFont(font)
        self.btn_parse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_parse.setObjectName("btn_parse")
        self.gridLayout.addWidget(self.btn_parse, 7, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.cmb_version = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_version.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cmb_version.setObjectName("cmb_version")
        self.horizontalLayout_3.addWidget(self.cmb_version)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txt_nwkskey = My_QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.txt_nwkskey.setFont(font)
        self.txt_nwkskey.setObjectName("txt_nwkskey")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_nwkskey)
        self.gridLayout.addLayout(self.formLayout, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.check_v = QtWidgets.QCheckBox(self.centralwidget)
        self.check_v.setText("")
        self.check_v.setChecked(False)
        self.check_v.setObjectName("check_v")
        self.horizontalLayout.addWidget(self.check_v)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.appkey_layout = QtWidgets.QFormLayout()
        self.appkey_layout.setObjectName("appkey_layout")
        self.lbl_appkey = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.lbl_appkey.setFont(font)
        self.lbl_appkey.setObjectName("lbl_appkey")
        self.appkey_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_appkey)
        self.input_appkey = My_QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.input_appkey.setFont(font)
        self.input_appkey.setObjectName("input_appkey")
        self.appkey_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input_appkey)
        self.gridLayout.addLayout(self.appkey_layout, 2, 0, 1, 1)
        self.txt_phy_pain.setContextMenuPolicy(Qt.CustomContextMenu)
        self.input_appkey.setContextMenuPolicy(Qt.CustomContextMenu)
        self.txt_nwkskey.setContextMenuPolicy(Qt.CustomContextMenu)
        self.txt_appskey.setContextMenuPolicy(Qt.CustomContextMenu)
        self.txt_phy_pain.customContextMenuRequested.connect(lambda: self.textEdit_generateMenu(QCursor.pos(),self.txt_phy_pain))
        self.input_appkey.customContextMenuRequested.connect(lambda: self.lineEdit_generateMenu(QCursor.pos(),self.input_appkey))
        self.txt_nwkskey.customContextMenuRequested.connect(lambda: self.lineEdit_generateMenu(QCursor.pos(),self.txt_nwkskey))
        self.txt_appskey.customContextMenuRequested.connect(lambda: self.lineEdit_generateMenu(QCursor.pos(),self.txt_appskey))

        MainWindow.setStatusBar(self.statusbar)
        self.statusShowTime()
        self.retranslateUi(MainWindow)
        self.initcombox()
        # ICON 图标
        try:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            MainWindow.setWindowIcon(icon)
        except:
            pass
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LoRaWAN报文解析器V1.0.5"))
        self.label_2.setText(_translate("MainWindow", "APPSKEY："))
        self.label.setText(_translate("MainWindow", "PHYPayload:"))
        self.btn_parse.setText(_translate("MainWindow", "开始解析"))
        self.label_8.setText(_translate("MainWindow", "VERSION："))
        self.label_3.setText(_translate("MainWindow", "NWKSKEY："))
        self.label_9.setText(_translate("MainWindow", "详细显示："))
        self.statusbar.setToolTip(_translate("MainWindow", "LoRaWAN报文解析器V1.0.5"))
        self.lbl_appkey.setText(_translate("MainWindow", " APPKEY："))

    def showCurrentTime(self, timeLabel):
        # 获取系统当前时间
        time = QDateTime.currentDateTime()
        # 设置系统时间的显示格式
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        # print(timeDisplay)
        # 状态栏显示
        timeLabel.setText(timeDisplay)

    def statusShowTime(self):
        self.timer = QTimer()
        self.timeLabel = QLabel()
        self.statusbar.addPermanentWidget(self.timeLabel, 0)
        self.timer.timeout.connect(lambda: self.showCurrentTime(self.timeLabel))  # 这个通过调用槽函数来刷新时间
        self.timer.start(1000)  # 每隔一秒刷新一次，这里设置为1000ms  即1s

    def initcombox(self):
        """
        填充版本combox
        """
        lorawan_version_list = ["1.0", "1.0.3", "1.1"]
        for i in range(len(lorawan_version_list)):
            self.cmb_version.addItem(lorawan_version_list[i])
        self.cmb_version.setCurrentText("1.0.3")

    def textEdit_generateMenu(self, pos,widget):
        """
        textedit的邮件菜单
        """
        # print(pos,widget)
        menu = QMenu()
        copyTob = menu.addAction("复制(Ctrl+A&&Ctrl+C)")
        pasteToContent = menu.addAction("粘贴(Ctrl+A&&Ctrl+V)")
        clearAllContent = menu.addAction("清空(Ctrl+A&&Delete)")
        # 使菜单在正常位置显示
        # screenPos = widget.mapToGlobal(pos)

        # 单击一个菜单项就返回，使之被阻塞
        action = menu.exec(pos)
        if action == copyTob:
            pyperclip.copy(widget.toPlainText())
            self.onMsgShow("复制成功")

        elif action == pasteToContent:
            widget.setPlainText(pyperclip.paste())
            self.onMsgShow("粘贴成功")

        elif action == clearAllContent:
            widget.clear()
            self.onMsgShow("清空成功")
        else:
            return

    def lineEdit_generateMenu(self, pos,widget):
        """
        lineEdit 的右键菜单
        """
        # print(pos,widget)
        menu = QMenu()
        copyTob = menu.addAction("复制(Ctrl+A&&Ctrl+C)")
        pasteToContent = menu.addAction("粘贴(Ctrl+A&&Ctrl+V)")
        clearAllContent = menu.addAction("清空(Ctrl+A&&Delete)")
        # 使菜单在正常位置显示
        # screenPos = widget.mapToGlobal(pos)

        # 单击一个菜单项就返回，使之被阻塞
        action = menu.exec(pos)
        if action == copyTob:
            pyperclip.copy(widget.text())
            self.onMsgShow("复制成功")
        elif action == pasteToContent:
            widget.setText(pyperclip.paste())
            self.onMsgShow("粘贴成功")
        elif action == clearAllContent:
            widget.clear()
            self.onMsgShow("清空成功")
        else:
            return

    def onMsgShow(self, msg):
        """
        右下角提示框
        :param msg:
        :return:
        """
        if hasattr(self, "_blabel"):
            self._blabel.stop()
            self._blabel.deleteLater()
            del self._blabel
        self._blabel = BubbleLabel()
        self._blabel.setText(msg)
        self._blabel.show()