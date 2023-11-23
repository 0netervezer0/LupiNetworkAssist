from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtWidgets import (QFrame, QLabel, QPushButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(413, 480)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 66, 138, 255), stop:1 rgba(0, 200, 240, 255));")
        self.menu_frame = QFrame(self.centralwidget)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setGeometry(QRect(30, 20, 121, 441))
        self.menu_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255 , 40);\n"
"border-radius: 10px;")
        self.verticalLayout_2 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.NetworkButton = QPushButton(self.menu_frame)
        self.NetworkButton.setObjectName(u"NetworkButton")
        self.NetworkButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-weight: bold;\n"
"	fonr-size: 20pt;\n"
"	background-color: rgba(255, 255, 255, 30);\n"
"	border: 1px solid rgba(255, 255, 255, 40);\n"
"	border-radius: 10px;\n"
"	width: 230px;\n"
"	height: 50px; \n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.verticalLayout_2.addWidget(self.NetworkButton)

        self.VpnButton = QPushButton(self.menu_frame)
        self.VpnButton.setObjectName(u"VpnButton")
        self.VpnButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-weight: bold;\n"
"	fonr-size: 20pt;\n"
"	background-color: rgba(255, 255, 255, 30);\n"
"	border: 1px solid rgba(255, 255, 255, 40);\n"
"	border-radius: 10px;\n"
"	width: 230px;\n"
"	height: 50px; \n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.verticalLayout_2.addWidget(self.VpnButton)

        self.InfoButton = QPushButton(self.menu_frame)
        self.InfoButton.setObjectName(u"InfoButton")
        self.InfoButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-weight: bold;\n"
"	fonr-size: 20pt;\n"
"	background-color: rgba(255, 255, 255, 30);\n"
"	border: 1px solid rgba(255, 255, 255, 40);\n"
"	border-radius: 10px;\n"
"	width: 230px;\n"
"	height: 50px; \n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.verticalLayout_2.addWidget(self.InfoButton)

        self.SettingsButton = QPushButton(self.menu_frame)
        self.SettingsButton.setObjectName(u"SettingsButton")
        self.SettingsButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-weight: bold;\n"
"	fonr-size: 20pt;\n"
"	background-color: rgba(255, 255, 255, 30);\n"
"	border: 1px solid rgba(255, 255, 255, 40);\n"
"	border-radius: 10px;\n"
"	width: 230px;\n"
"	height: 50px; \n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.verticalLayout_2.addWidget(self.SettingsButton)

        self.upload_frame = QFrame(self.centralwidget)
        self.upload_frame.setObjectName(u"upload_frame")
        self.upload_frame.setGeometry(QRect(200, 150, 181, 131))
        self.upload_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 40);\n"
"border: 1px solid rgba(255, 255, 255 , 50);\n"
"border-radius: 10px;\n"
"text-align: center;")
        self.verticalLayout_3 = QVBoxLayout(self.upload_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.upload_text = QLabel(self.upload_frame)
        self.upload_text.setObjectName(u"upload_text")
        self.upload_text.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"fonr-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
"width: 230px;\n"
"height: 50px; ")
        self.upload_text.setScaledContents(False)
        self.upload_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.upload_text)

        self.upload_info = QLabel(self.upload_frame)
        self.upload_info.setObjectName(u"upload_info")
        self.upload_info.setStyleSheet(u"text-align: center;\n"
"color: white;\n"
"font-weight: bold;\n"
"fonr-size: 20pt;\n"
"border-radius: 10px;\n"
"width: 230px;\n"
"height: 50px; \n"
"padding-left: 55px;")
        self.upload_info.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.upload_info)

        self.download_frame = QFrame(self.centralwidget)
        self.download_frame.setObjectName(u"download_frame")
        self.download_frame.setGeometry(QRect(200, 310, 181, 151))
        self.download_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 40);\n"
"border: 1px solid rgba(255, 255, 255 , 50);\n"
"border-radius: 10px;\n"
"text-align: center;")
        self.verticalLayout_4 = QVBoxLayout(self.download_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.download_text = QLabel(self.download_frame)
        self.download_text.setObjectName(u"download_text")
        self.download_text.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"fonr-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
"width: 230px;\n"
"height: 50px; ")
        self.download_text.setScaledContents(False)
        self.download_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.download_text)

        self.download_info = QLabel(self.download_frame)
        self.download_info.setObjectName(u"download_info")
        self.download_info.setStyleSheet(u"text-align: center;\n"
"color: white;\n"
"font-weight: bold;\n"
"fonr-size: 20pt;\n"
"border-radius: 10px;\n"
"width: 230px;\n"
"height: 50px; \n"
"padding-left: 55px;")
        self.download_info.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.download_info)

        self.ip_frame = QFrame(self.centralwidget)
        self.ip_frame.setObjectName(u"ip_frame")
        self.ip_frame.setGeometry(QRect(200, 20, 181, 101))
        self.ip_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 40);\n"
"border: 1px solid rgba(255, 255, 255 , 50);\n"
"border-radius: 10px;\n"
"text-align: center;")
        self.verticalLayout = QVBoxLayout(self.ip_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ip_text = QLabel(self.ip_frame)
        self.ip_text.setObjectName(u"ip_text")
        self.ip_text.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"fonr-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
"width: 230px;\n"
"height: 50px; ")
        self.ip_text.setScaledContents(False)
        self.ip_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.ip_text)

        self.ip_info = QLabel(self.ip_frame)
        self.ip_info.setObjectName(u"ip_info")
        self.ip_info.setStyleSheet(u"text-align: center;\n"
"color: white;\n"
"font-weight: bold;\n"
"fonr-size: 20pt;\n"
"border-radius: 10px;\n"
"width: 230px;\n"
"height: 50px; \n"
"padding-left: 55px;")
        self.ip_info.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.ip_info)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.NetworkButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0448\u0430 \u0441\u0435\u0442\u044c", None))
        self.VpnButton.setText(QCoreApplication.translate("MainWindow", u"VPN", None))
        self.InfoButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.SettingsButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.upload_text.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.upload_info.setText("")
        self.download_text.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.download_info.setText("")
        self.ip_text.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0448 IP", None))
        self.ip_info.setText("")