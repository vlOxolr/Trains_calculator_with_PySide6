# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(338, 313)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblequ = QLabel(Form)
        self.lblequ.setObjectName(u"lblequ")
        font = QFont()
        font.setPointSize(20)
        self.lblequ.setFont(font)
        self.lblequ.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.lblequ)

        self.lblans = QLabel(Form)
        self.lblans.setObjectName(u"lblans")
        self.lblans.setFont(font)
        self.lblans.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.verticalLayout.addWidget(self.lblans)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.b1 = QPushButton(Form)
        self.b1.setObjectName(u"b1")
        self.b1.setMinimumSize(QSize(0, 0))
        self.b1.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(18)
        self.b1.setFont(font1)

        self.horizontalLayout.addWidget(self.b1)

        self.b2 = QPushButton(Form)
        self.b2.setObjectName(u"b2")
        self.b2.setFont(font1)

        self.horizontalLayout.addWidget(self.b2)

        self.b3 = QPushButton(Form)
        self.b3.setObjectName(u"b3")
        self.b3.setFont(font1)

        self.horizontalLayout.addWidget(self.b3)

        self.bplus = QPushButton(Form)
        self.bplus.setObjectName(u"bplus")
        self.bplus.setFont(font1)

        self.horizontalLayout.addWidget(self.bplus)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.b4 = QPushButton(Form)
        self.b4.setObjectName(u"b4")
        self.b4.setFont(font1)

        self.horizontalLayout_2.addWidget(self.b4)

        self.b5 = QPushButton(Form)
        self.b5.setObjectName(u"b5")
        self.b5.setFont(font1)

        self.horizontalLayout_2.addWidget(self.b5)

        self.b6 = QPushButton(Form)
        self.b6.setObjectName(u"b6")
        self.b6.setFont(font1)

        self.horizontalLayout_2.addWidget(self.b6)

        self.bminus = QPushButton(Form)
        self.bminus.setObjectName(u"bminus")
        self.bminus.setFont(font1)

        self.horizontalLayout_2.addWidget(self.bminus)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.b7 = QPushButton(Form)
        self.b7.setObjectName(u"b7")
        self.b7.setFont(font1)

        self.horizontalLayout_3.addWidget(self.b7)

        self.b8 = QPushButton(Form)
        self.b8.setObjectName(u"b8")
        self.b8.setFont(font1)

        self.horizontalLayout_3.addWidget(self.b8)

        self.b9 = QPushButton(Form)
        self.b9.setObjectName(u"b9")
        self.b9.setFont(font1)

        self.horizontalLayout_3.addWidget(self.b9)

        self.btimes = QPushButton(Form)
        self.btimes.setObjectName(u"btimes")
        self.btimes.setFont(font1)

        self.horizontalLayout_3.addWidget(self.btimes)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.bdot = QPushButton(Form)
        self.bdot.setObjectName(u"bdot")
        self.bdot.setFont(font1)

        self.horizontalLayout_4.addWidget(self.bdot)

        self.b0 = QPushButton(Form)
        self.b0.setObjectName(u"b0")
        self.b0.setFont(font1)

        self.horizontalLayout_4.addWidget(self.b0)

        self.bAC = QPushButton(Form)
        self.bAC.setObjectName(u"bAC")
        self.bAC.setFont(font1)

        self.horizontalLayout_4.addWidget(self.bAC)

        self.bdiv = QPushButton(Form)
        self.bdiv.setObjectName(u"bdiv")
        self.bdiv.setFont(font1)

        self.horizontalLayout_4.addWidget(self.bdiv)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblequ.setText(QCoreApplication.translate("Form", u"Calculation", None))
        self.lblans.setText(QCoreApplication.translate("Form", u"Result", None))
        self.b1.setText(QCoreApplication.translate("Form", u"1", None))
        self.b2.setText(QCoreApplication.translate("Form", u"2", None))
        self.b3.setText(QCoreApplication.translate("Form", u"3", None))
        self.bplus.setText(QCoreApplication.translate("Form", u"+", None))
        self.b4.setText(QCoreApplication.translate("Form", u"4", None))
        self.b5.setText(QCoreApplication.translate("Form", u"5", None))
        self.b6.setText(QCoreApplication.translate("Form", u"6", None))
        self.bminus.setText(QCoreApplication.translate("Form", u"-", None))
        self.b7.setText(QCoreApplication.translate("Form", u"7", None))
        self.b8.setText(QCoreApplication.translate("Form", u"8", None))
        self.b9.setText(QCoreApplication.translate("Form", u"9", None))
        self.btimes.setText(QCoreApplication.translate("Form", u"x", None))
        self.bdot.setText(QCoreApplication.translate("Form", u".", None))
        self.b0.setText(QCoreApplication.translate("Form", u"0", None))
        self.bAC.setText(QCoreApplication.translate("Form", u"AC", None))
        self.bdiv.setText(QCoreApplication.translate("Form", u"/", None))
    # retranslateUi

