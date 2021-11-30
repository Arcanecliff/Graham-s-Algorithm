# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calc_design.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 210)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"color:#887;")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setStyleSheet(u"border: none;")
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEdit)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_29 = QPushButton(self.centralwidget)
        self.pushButton_29.setObjectName(u"pushButton_29")

        self.gridLayout.addWidget(self.pushButton_29, 4, 3, 1, 1)

        self.pushButton_16 = QPushButton(self.centralwidget)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.gridLayout.addWidget(self.pushButton_16, 0, 5, 1, 1)

        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout.addWidget(self.pushButton_13, 0, 2, 1, 1)

        self.pushButton_25 = QPushButton(self.centralwidget)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.gridLayout.addWidget(self.pushButton_25, 3, 0, 1, 1)

        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout.addWidget(self.pushButton_14, 0, 3, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 3, 1, 1, 1)

        self.pushButton_22 = QPushButton(self.centralwidget)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.gridLayout.addWidget(self.pushButton_22, 2, 3, 1, 1)

        self.pushButton_18 = QPushButton(self.centralwidget)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.gridLayout.addWidget(self.pushButton_18, 2, 0, 1, 1)

        self.pushButton_20 = QPushButton(self.centralwidget)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.gridLayout.addWidget(self.pushButton_20, 1, 4, 1, 1)

        self.pushButton_26 = QPushButton(self.centralwidget)
        self.pushButton_26.setObjectName(u"pushButton_26")

        self.gridLayout.addWidget(self.pushButton_26, 4, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.centralwidget)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout.addWidget(self.pushButton_15, 0, 4, 1, 1)

        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout.addWidget(self.pushButton_11, 2, 2, 1, 1)

        self.pushButton_21 = QPushButton(self.centralwidget)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.gridLayout.addWidget(self.pushButton_21, 1, 3, 1, 1)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 3, 4, 1, 1)

        self.pushButton_17 = QPushButton(self.centralwidget)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.gridLayout.addWidget(self.pushButton_17, 1, 0, 1, 1)

        self.pushButton_19 = QPushButton(self.centralwidget)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.gridLayout.addWidget(self.pushButton_19, 1, 5, 1, 1)

        self.pushButton_23 = QPushButton(self.centralwidget)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.gridLayout.addWidget(self.pushButton_23, 2, 4, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 3, 3, 1, 1)

        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout.addWidget(self.pushButton_10, 3, 2, 1, 1)

        self.pushButton_28 = QPushButton(self.centralwidget)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.gridLayout.addWidget(self.pushButton_28, 4, 4, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout.addWidget(self.pushButton_12, 1, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 2)

        self.pushButton_24 = QPushButton(self.centralwidget)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.gridLayout.addWidget(self.pushButton_24, 2, 5, 1, 1)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy2)
        self.pushButton_7.setBaseSize(QSize(0, 0))

        self.gridLayout.addWidget(self.pushButton_7, 3, 5, 2, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421alculator", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Mod", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"tan", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"n!", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u00b1", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"sin", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"1/x", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"=", None))
    # retranslateUi

