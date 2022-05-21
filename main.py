import sys

import numpy as np
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal, QTimer, QDateTime
from PyQt5.QtGui import QPixmap, QImage

from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox

import cv2

from index import Ui_MainWindow
from login import Ui_LoginDialog
import requests
import shutil



class LoginDialog(QDialog, Ui_LoginDialog):
    login_user = pyqtSignal(dict)
    users = dict()

    def __init__(self):
        super(LoginDialog, self).__init__()
        self.setupUi(self)
        self.initLabel()

        self.initButton()

        self.showLogin()

        self.resize(600, 400)
        self.setFixedSize(self.width(), self.height())

        self.read()

    def showLogin(self):
        self.w_login.show()
        self.w_forget.hide()
        self.w_register.hide()
        self.setWindowTitle("登录")

    def showRegister(self):
        self.w_login.hide()
        self.w_forget.hide()
        self.w_register.show()
        self.setWindowTitle("注册")

    def showForget(self):
        self.w_login.hide()
        self.w_forget.show()
        self.w_register.hide()
        self.setWindowTitle("忘记密码")

    def initButton(self):
        def click_pb_login():
            account = self.le_login_account.text()
            psw = self.le_login_psw.text()
            if not account:
                QMessageBox.warning(self, "登录错误", "学号为空！", QMessageBox.Yes)
                return
            if not psw:
                QMessageBox.warning(self, "登录错误", "密码为空！", QMessageBox.Yes)
                return
            self.read()
            print(self.users)
            if account not in self.users.keys():
                QMessageBox.warning(self, "登录错误", "用户不存在！", QMessageBox.Yes)
                return
            if self.users[account]["psw"] != psw:
                QMessageBox.warning(self, "登录错误", "用户密码错误！", QMessageBox.Yes)
                return
            self.login_user.emit(self.users[account])
            self.close()

        self.pb_login.clicked.connect(click_pb_login)

        def click_pb_register():
            account = self.lb_register_account.text()
            name = self.lb_register_name.text()
            psw = self.lb_register_psw.text()
            psw_again = self.lb_register_psw_again.text()
            man = "男" if self.rb_man.isChecked() else "女"
            if not account:
                QMessageBox.warning(self, "注册错误", "学号为空！", QMessageBox.Yes)
                return

            if not name:
                QMessageBox.warning(self, "注册错误", "姓名为空！", QMessageBox.Yes)
                return
            if not psw and not psw_again:
                QMessageBox.warning(self, "注册错误", "密码为空！", QMessageBox.Yes)
                return
            if psw != psw_again:
                QMessageBox.warning(self, "注册错误", "密码不一致！", QMessageBox.Yes)
                return
            self.read()
            if account in self.users.keys():
                QMessageBox.warning(self, "注册错误", "用户已存在！", QMessageBox.Yes)
                return
            self.append({
                "account": account,
                "name": name,
                "psw": psw,
                "sex": man
            })
            QMessageBox.information(self, "注册", "注册成功！")
            self.showLogin()

        self.pb_register.clicked.connect(click_pb_register)

        def click_pb_modify():
            account = self.le_forget_account.text()
            psw = self.le_forget_psw.text()
            psw_again = self.le_forget_psw_again.text()
            if not account:
                QMessageBox.warning(self, "忘记密码错误", "学号为空！", QMessageBox.Yes)
                return

            if psw != psw_again:
                QMessageBox.warning(self, "注册错误", "密码不一致！", QMessageBox.Yes)
                return

            self.read()
            if account not in self.users.keys():
                QMessageBox.warning(self, "注册错误", "用户不存在！", QMessageBox.Yes)
                return
            self.users[account]["psw"] = psw
            self.save()
            self.showLogin()

        self.pb_modify.clicked.connect(click_pb_modify)

    def initLabel(self):
        self.lb_register.linkActivated.connect(self.showRegister)
        self.lb_forget.linkActivated.connect(self.showForget)
        self.lb_login.linkActivated.connect(self.showLogin)
        self.lb_login_2.linkActivated.connect(self.showLogin)

    def save(self):
        with open("user.txt", "w", encoding="utf-8", newline="") as f:
            f.writelines(["{},{},{},{}\n".format(user, data["name"], data["psw"], data["sex"]) for user, data in
                          self.users.items()])

    def read(self):
        try:
            with open("user.txt", "r", encoding="utf-8", newline="") as f:
                self.users = {}
                user_lst = f.readlines()
                for user in user_lst:
                    try:
                        user = user.strip("\n").strip("\r").split(",")
                        self.users.update({user[0]: {
                            "name": user[1],
                            "psw": user[2],
                            "sex": user[3]
                        }})
                    except:
                        pass
        except:
            pass

    def append(self, user):
        with open("user.txt", "a+", encoding="utf-8") as f:
            f.write("{},{},{},{}\n".format(user["account"], user["name"], user["psw"], user["sex"]))
            self.users.update({user["account"]: {
                "name": user["name"],
                "psw": user["psw"],
                "sex": user["sex"]
            }})


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    original_img = np.ndarray((0, 0))
    result_img = np.ndarray((0, 0))
    logout = pyqtSignal()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # 初始化界面
        self.initWidget()
        # 初始化按钮控制
        self.initButton()
        # 初始化ComboBox
        self.initComboBox()
        # 初始化计时器
        self.initTimer()

    def initWidget(self):
        self.w_main.show()
        self.w_history.hide()
        if self.cb_show_info.checkState():
            self.gb_info.show()
            self.resize(900, 700)
        else:
            self.gb_info.hide()
            self.resize(900, 500)
        # 不可改变窗口大小
        self.setFixedSize(self.width(), self.height())

    def initButton(self):
        self.pb_main.setEnabled(False)
        self.pb_history.setEnabled(True)

        def click_pb_import():
            self.file, _ = QFileDialog.getOpenFileName(self, "打开图像", ".\\", "图像文件 (*.jpg *.bmp *.png)")
            if self.file:
                self.le_path.setText(self.file)
                try:
                    self.original_img = cv2.imread(self.file)
                    pixmap = QPixmap(self.file)
                    width = pixmap.width()  ##获取图片宽度
                    height = pixmap.height()  ##获取图片高度
                    if width / self.lb_original.width() >= height / self.lb_original.height():  ##比较图片宽度与label宽度之比和图片高度与label高度之比
                        ratio = width / self.lb_original.width()
                    else:
                        ratio = height / self.lb_original.height()
                    new_width = width / ratio  ##定义新图片的宽和高
                    new_height = height / ratio
                    pixmap = pixmap.scaled(new_width, new_height)  ##调整图片尺寸
                    self.lb_original.setPixmap(pixmap)  # 在label上显示图片
                    self.lb_original.setScaledContents(True)  # 让图片自适应label大小
                    self.lb_original.show()
                except Exception as e:
                    print(e)

        self.pb_import.clicked.connect(click_pb_import)

        def click_pb_start():
            #save array to file object

            files = {'file':open(self.file,'rb')}
            r = requests.post('https://b0bf-137-148-143-182.ngrok.io/items', files=files, stream=True)
            with open('image.jpg', 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)     

            processed_img = cv2.imread('image.jpg')
            width, height = processed_img.shape[1], processed_img.shape[0]
            bytesPerLine = 3 * width
       

            qImg = QImage(processed_img, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()

            pixmap = QPixmap(qImg)
            width = pixmap.width()  ##获取图片宽度
            height = pixmap.height()  ##获取图片高度
            if width / self.lb_original.width() >= height / self.lb_original.height():  ##比较图片宽度与label宽度之比和图片高度与label高度之比
                ratio = width / self.lb_original.width()
            else:
                ratio = height / self.lb_original.height()
            new_width = width / ratio  ##定义新图片的宽和高
            new_height = height / ratio
            pixmap = pixmap.scaled(new_width, new_height)  ##调整图片尺寸

            self.lb_result.setPixmap(pixmap)  # 在label上显示图片
            self.lb_result.setScaledContents(True)  # 让图片自适应label大小
            self.lb_result.show()

        self.pb_start.clicked.connect(click_pb_start)

        def click_pb_show(status):
            if status:
                self.w_main.show()
                self.w_history.hide()
                self.pb_main.setEnabled(False)
                self.pb_history.setEnabled(True)
            else:
                self.w_main.hide()
                self.w_history.show()
                self.pb_main.setEnabled(True)
                self.pb_history.setEnabled(False)
            # 不可改变窗口大小
            self.setFixedSize(self.width(), self.height())

        self.pb_main.clicked.connect(lambda: click_pb_show(True))
        self.pb_history.clicked.connect(lambda: click_pb_show(False))

        def click_pb_save():
            file, _ = QFileDialog.getSaveFileName(self, "保存图像", ".\\result.jpg", "图像文件 (*.jpg *.bmp *.png)")
            try:
                cv2.imwrite(file, self.result_img)
                QMessageBox.information(self, "保存结果", "保存成功！", QMessageBox.Yes)
            except Exception as e:
                QMessageBox.warning(self, "保存结果", "保存失败！" + str(e), QMessageBox.Yes)

        self.pb_save.clicked.connect(click_pb_save)

        def click_pb_logout():
            self.close()
            self.logout.emit()

        self.pb_logout.clicked.connect(click_pb_logout)

    def initComboBox(self):
        def click_cb_show_info(status):
            if status:
                self.gb_info.show()
                self.resize(900, 700)
                self.setFixedSize(900, 700)
            else:
                self.gb_info.hide()
                self.resize(900, 500)
                # 不可改变窗口大小
                self.setFixedSize(900, 500)

        self.cb_show_info.clicked.connect(click_cb_show_info)

        self.cb_way.addItems(["方法1", "方法2", "方法3", "方法4"])

    def initTimer(self):
        def timeOut():
            current_date_time = QDateTime.currentDateTime()
            self.lb_time.setText(current_date_time.toString("yyyy.MM.dd hh:mm:ss ddd"))

        self.now_timer = QTimer()
        self.now_timer.timeout.connect(timeOut)
        self.now_timer.start(30)

    def setLoginUser(self, user):
        self.lb_welcome.setText(user["name"])

    def convertImg(self, frame):
        QtImgBuf = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

        QtImg = QtGui.QImage(QtImgBuf.data, QtImgBuf.shape[1], QtImgBuf.shape[0], QtGui.QImage.Format_RGB32)
        px = QtGui.QPixmap.fromImage(QtImg)
        return px



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = LoginDialog()
    main = MainWindow()
    login.login_user.connect(main.setLoginUser)
    login.login_user.connect(lambda: main.show())
    main.logout.connect(lambda: login.show())

    # main.show()
    login.show()
    sys.exit(app.exec_())
