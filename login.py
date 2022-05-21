# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(381, 733)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(LoginDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.w_login = QtWidgets.QWidget(LoginDialog)
        self.w_login.setObjectName("w_login")
        self.v_login = QtWidgets.QVBoxLayout(self.w_login)
        self.v_login.setObjectName("v_login")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.v_login.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.w_login)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.v_login.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.v_login.addItem(spacerItem1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.le_login_account = QtWidgets.QLineEdit(self.w_login)
        self.le_login_account.setMinimumSize(QtCore.QSize(200, 0))
        self.le_login_account.setObjectName("le_login_account")
        self.horizontalLayout_4.addWidget(self.le_login_account)
        self.lb_register = QtWidgets.QLabel(self.w_login)
        self.lb_register.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lb_register.setOpenExternalLinks(False)
        self.lb_register.setObjectName("lb_register")
        self.horizontalLayout_4.addWidget(self.lb_register)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.le_login_psw = QtWidgets.QLineEdit(self.w_login)
        self.le_login_psw.setMinimumSize(QtCore.QSize(200, 0))
        self.le_login_psw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_login_psw.setObjectName("le_login_psw")
        self.horizontalLayout_5.addWidget(self.le_login_psw)
        self.lb_forget = QtWidgets.QLabel(self.w_login)
        self.lb_forget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lb_forget.setOpenExternalLinks(False)
        self.lb_forget.setObjectName("lb_forget")
        self.horizontalLayout_5.addWidget(self.lb_forget)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb_remenber = QtWidgets.QCheckBox(self.w_login)
        self.cb_remenber.setObjectName("cb_remenber")
        self.horizontalLayout.addWidget(self.cb_remenber)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pb_login = QtWidgets.QPushButton(self.w_login)
        self.pb_login.setMinimumSize(QtCore.QSize(200, 0))
        self.pb_login.setObjectName("pb_login")
        self.horizontalLayout_11.addWidget(self.pb_login)
        spacerItem4 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.v_login.addLayout(self.horizontalLayout_10)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.v_login.addItem(spacerItem6)
        self.verticalLayout_2.addWidget(self.w_login)
        self.w_register = QtWidgets.QWidget(LoginDialog)
        self.w_register.setObjectName("w_register")
        self.v_register = QtWidgets.QVBoxLayout(self.w_register)
        self.v_register.setObjectName("v_register")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.v_register.addItem(spacerItem7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.w_register)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.v_register.addLayout(self.horizontalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.v_register.addItem(spacerItem8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_register_account = QtWidgets.QLineEdit(self.w_register)
        self.lb_register_account.setMinimumSize(QtCore.QSize(250, 0))
        self.lb_register_account.setInputMask("")
        self.lb_register_account.setObjectName("lb_register_account")
        self.verticalLayout.addWidget(self.lb_register_account)
        self.lb_register_name = QtWidgets.QLineEdit(self.w_register)
        self.lb_register_name.setMinimumSize(QtCore.QSize(200, 0))
        self.lb_register_name.setInputMask("")
        self.lb_register_name.setObjectName("lb_register_name")
        self.verticalLayout.addWidget(self.lb_register_name)
        self.lb_register_psw = QtWidgets.QLineEdit(self.w_register)
        self.lb_register_psw.setMinimumSize(QtCore.QSize(200, 0))
        self.lb_register_psw.setInputMask("")
        self.lb_register_psw.setText("")
        self.lb_register_psw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lb_register_psw.setObjectName("lb_register_psw")
        self.verticalLayout.addWidget(self.lb_register_psw)
        self.lb_register_psw_again = QtWidgets.QLineEdit(self.w_register)
        self.lb_register_psw_again.setMinimumSize(QtCore.QSize(200, 0))
        self.lb_register_psw_again.setInputMask("")
        self.lb_register_psw_again.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lb_register_psw_again.setObjectName("lb_register_psw_again")
        self.verticalLayout.addWidget(self.lb_register_psw_again)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.w_register)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.rb_man = QtWidgets.QRadioButton(self.w_register)
        self.rb_man.setChecked(True)
        self.rb_man.setObjectName("rb_man")
        self.horizontalLayout_7.addWidget(self.rb_man)
        self.rb_woman = QtWidgets.QRadioButton(self.w_register)
        self.rb_woman.setObjectName("rb_woman")
        self.horizontalLayout_7.addWidget(self.rb_woman)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.pb_register = QtWidgets.QPushButton(self.w_register)
        self.pb_register.setObjectName("pb_register")
        self.verticalLayout.addWidget(self.pb_register)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem11)
        self.lb_login_2 = QtWidgets.QLabel(self.w_register)
        self.lb_login_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lb_login_2.setOpenExternalLinks(False)
        self.lb_login_2.setObjectName("lb_login_2")
        self.horizontalLayout_8.addWidget(self.lb_login_2)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9.addLayout(self.verticalLayout)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem12)
        self.v_register.addLayout(self.horizontalLayout_9)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.v_register.addItem(spacerItem13)
        self.verticalLayout_2.addWidget(self.w_register)
        self.w_forget = QtWidgets.QWidget(LoginDialog)
        self.w_forget.setObjectName("w_forget")
        self.v_login_2 = QtWidgets.QVBoxLayout(self.w_forget)
        self.v_login_2.setObjectName("v_login_2")
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.v_login_2.addItem(spacerItem14)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_5 = QtWidgets.QLabel(self.w_forget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_12.addWidget(self.label_5)
        self.v_login_2.addLayout(self.horizontalLayout_12)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.v_login_2.addItem(spacerItem15)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem16)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.le_forget_account = QtWidgets.QLineEdit(self.w_forget)
        self.le_forget_account.setMinimumSize(QtCore.QSize(200, 0))
        self.le_forget_account.setObjectName("le_forget_account")
        self.verticalLayout_4.addWidget(self.le_forget_account)
        self.le_forget_psw = QtWidgets.QLineEdit(self.w_forget)
        self.le_forget_psw.setMinimumSize(QtCore.QSize(200, 0))
        self.le_forget_psw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_forget_psw.setObjectName("le_forget_psw")
        self.verticalLayout_4.addWidget(self.le_forget_psw)
        self.le_forget_psw_again = QtWidgets.QLineEdit(self.w_forget)
        self.le_forget_psw_again.setText("")
        self.le_forget_psw_again.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_forget_psw_again.setObjectName("le_forget_psw_again")
        self.verticalLayout_4.addWidget(self.le_forget_psw_again)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.pb_modify = QtWidgets.QPushButton(self.w_forget)
        self.pb_modify.setMinimumSize(QtCore.QSize(250, 0))
        self.pb_modify.setObjectName("pb_modify")
        self.horizontalLayout_17.addWidget(self.pb_modify)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem17)
        self.lb_login = QtWidgets.QLabel(self.w_forget)
        self.lb_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lb_login.setOpenExternalLinks(False)
        self.lb_login.setObjectName("lb_login")
        self.horizontalLayout_14.addWidget(self.lb_login)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13.addLayout(self.verticalLayout_4)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem18)
        self.v_login_2.addLayout(self.horizontalLayout_13)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.v_login_2.addItem(spacerItem19)
        self.verticalLayout_2.addWidget(self.w_forget)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Dialog"))
        self.label.setText(_translate("LoginDialog", "电路板缺陷检测-登录"))
        self.le_login_account.setPlaceholderText(_translate("LoginDialog", "学号"))
        self.lb_register.setText(_translate("LoginDialog", "<a href =\" \">注册账号</a>"))
        self.le_login_psw.setPlaceholderText(_translate("LoginDialog", "密码"))
        self.lb_forget.setText(_translate("LoginDialog", "<a href =\" \">忘记密码</a>"))
        self.cb_remenber.setText(_translate("LoginDialog", "记住密码"))
        self.pb_login.setText(_translate("LoginDialog", "登录"))
        self.label_2.setText(_translate("LoginDialog", "电路板缺陷检测-注册"))
        self.lb_register_account.setPlaceholderText(_translate("LoginDialog", "学号"))
        self.lb_register_name.setPlaceholderText(_translate("LoginDialog", "姓名"))
        self.lb_register_psw.setPlaceholderText(_translate("LoginDialog", "密码"))
        self.lb_register_psw_again.setPlaceholderText(_translate("LoginDialog", "确认密码"))
        self.label_3.setText(_translate("LoginDialog", "性别："))
        self.rb_man.setText(_translate("LoginDialog", "男"))
        self.rb_woman.setText(_translate("LoginDialog", "女"))
        self.pb_register.setText(_translate("LoginDialog", "注册"))
        self.lb_login_2.setText(_translate("LoginDialog", "<a href =\" \">已有账号？点击登录</a>"))
        self.label_5.setText(_translate("LoginDialog", "电路板缺陷检测-忘记密码"))
        self.le_forget_account.setPlaceholderText(_translate("LoginDialog", "学号"))
        self.le_forget_psw.setPlaceholderText(_translate("LoginDialog", "密码"))
        self.le_forget_psw_again.setPlaceholderText(_translate("LoginDialog", "确认密码"))
        self.pb_modify.setText(_translate("LoginDialog", "修改"))
        self.lb_login.setText(_translate("LoginDialog", "<a href =\" \">记得密码？点击登录</a>"))
