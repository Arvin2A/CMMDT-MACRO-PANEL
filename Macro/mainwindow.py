# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'macromainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 375)
        MainWindow.setMinimumSize(QSize(450, 375))
        MainWindow.setMaximumSize(QSize(450, 375))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 431, 20))
        font = QFont()
        font.setFamilies([u"Noto Kufi Arabic Black"])
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frameone = QFrame(self.centralwidget)
        self.frameone.setObjectName(u"frameone")
        self.frameone.setGeometry(QRect(20, 40, 201, 301))
        self.frameone.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameone.setFrameShadow(QFrame.Shadow.Raised)
        self.frameone.setLineWidth(1)
        self.verticalLayoutWidget_3 = QWidget(self.frameone)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 201, 301))
        self.mainlayout1 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.mainlayout1.setObjectName(u"mainlayout1")
        self.mainlayout1.setContentsMargins(5, 0, 0, 0)
        self.skipshake = QCheckBox(self.verticalLayoutWidget_3)
        self.skipshake.setObjectName(u"skipshake")

        self.mainlayout1.addWidget(self.skipshake, 0, Qt.AlignmentFlag.AlignTop)

        self.visual_indicators = QCheckBox(self.verticalLayoutWidget_3)
        self.visual_indicators.setObjectName(u"visual_indicators")

        self.mainlayout1.addWidget(self.visual_indicators)

        self.castdataframe = QFrame(self.verticalLayoutWidget_3)
        self.castdataframe.setObjectName(u"castdataframe")
        self.castdataframe.setMinimumSize(QSize(0, 40))
        self.castdataframe.setFrameShape(QFrame.Shape.NoFrame)
        self.castdataframe.setFrameShadow(QFrame.Shadow.Raised)
        self.castdataframe.setLineWidth(0)
        self.horizontalLayoutWidget_4 = QWidget(self.castdataframe)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(-1, 0, 191, 41))
        self.datalayout = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.datalayout.setObjectName(u"datalayout")
        self.datalayout.setContentsMargins(0, 0, 0, 0)
        self.castdurationlabel = QLabel(self.horizontalLayoutWidget_4)
        self.castdurationlabel.setObjectName(u"castdurationlabel")

        self.datalayout.addWidget(self.castdurationlabel)

        self.castduration = QDoubleSpinBox(self.horizontalLayoutWidget_4)
        self.castduration.setObjectName(u"castduration")
        self.castduration.setDecimals(1)
        self.castduration.setMinimum(1.000000000000000)
        self.castduration.setMaximum(69.900000000000006)
        self.castduration.setSingleStep(0.250000000000000)
        self.castduration.setValue(1.500000000000000)

        self.datalayout.addWidget(self.castduration)


        self.mainlayout1.addWidget(self.castdataframe)

        self.latencydataframe = QFrame(self.verticalLayoutWidget_3)
        self.latencydataframe.setObjectName(u"latencydataframe")
        self.latencydataframe.setMinimumSize(QSize(0, 40))
        self.latencydataframe.setFrameShape(QFrame.Shape.NoFrame)
        self.latencydataframe.setFrameShadow(QFrame.Shadow.Raised)
        self.latencydataframe.setLineWidth(0)
        self.horizontalLayoutWidget_5 = QWidget(self.latencydataframe)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(-1, 0, 191, 41))
        self.latencylayout = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.latencylayout.setObjectName(u"latencylayout")
        self.latencylayout.setContentsMargins(0, 0, 0, 0)
        self.latencylabel = QLabel(self.horizontalLayoutWidget_5)
        self.latencylabel.setObjectName(u"latencylabel")

        self.latencylayout.addWidget(self.latencylabel)

        self.latency = QDoubleSpinBox(self.horizontalLayoutWidget_5)
        self.latency.setObjectName(u"latency")
        self.latency.setDecimals(2)
        self.latency.setMinimum(0.100000000000000)
        self.latency.setMaximum(69.900000000000006)
        self.latency.setSingleStep(0.100000000000000)
        self.latency.setValue(0.100000000000000)

        self.latencylayout.addWidget(self.latency)


        self.mainlayout1.addWidget(self.latencydataframe)

        self.controldataframe = QFrame(self.verticalLayoutWidget_3)
        self.controldataframe.setObjectName(u"controldataframe")
        self.controldataframe.setMinimumSize(QSize(0, 40))
        self.controldataframe.setFrameShape(QFrame.Shape.NoFrame)
        self.controldataframe.setFrameShadow(QFrame.Shadow.Raised)
        self.controldataframe.setLineWidth(0)
        self.horizontalLayoutWidget_8 = QWidget(self.controldataframe)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(-1, 0, 191, 41))
        self.controllayout = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.controllayout.setObjectName(u"controllayout")
        self.controllayout.setContentsMargins(0, 0, 0, 0)
        self.controllabel = QLabel(self.horizontalLayoutWidget_8)
        self.controllabel.setObjectName(u"controllabel")

        self.controllayout.addWidget(self.controllabel)

        self.control = QDoubleSpinBox(self.horizontalLayoutWidget_8)
        self.control.setObjectName(u"control")
        self.control.setDecimals(2)
        self.control.setMinimum(0.000000000000000)
        self.control.setMaximum(1.000000000000000)
        self.control.setSingleStep(0.050000000000000)
        self.control.setValue(0.000000000000000)

        self.controllayout.addWidget(self.control)


        self.mainlayout1.addWidget(self.controldataframe)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainlayout1.addItem(self.verticalSpacer)

        self.frametwo = QFrame(self.centralwidget)
        self.frametwo.setObjectName(u"frametwo")
        self.frametwo.setGeometry(QRect(240, 40, 201, 301))
        self.frametwo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frametwo.setFrameShadow(QFrame.Shadow.Raised)
        self.frametwo.setLineWidth(1)
        self.verticalLayoutWidget_4 = QWidget(self.frametwo)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 0, 201, 301))
        self.mainlayout2 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.mainlayout2.setSpacing(5)
        self.mainlayout2.setObjectName(u"mainlayout2")
        self.mainlayout2.setContentsMargins(0, 0, 0, 0)
        self.extend = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainlayout2.addItem(self.extend)

        self.stopbutton = QPushButton(self.verticalLayoutWidget_4)
        self.stopbutton.setObjectName(u"stopbutton")
        self.stopbutton.setEnabled(False)
        font1 = QFont()
        font1.setFamilies([u"Monospace"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.stopbutton.setFont(font1)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStop))
        self.stopbutton.setIcon(icon)
        self.stopbutton.setCheckable(False)

        self.mainlayout2.addWidget(self.stopbutton)

        self.consolebutton = QPushButton(self.verticalLayoutWidget_4)
        self.consolebutton.setObjectName(u"consolebutton")
        self.consolebutton.setEnabled(False)
        self.consolebutton.setFont(font1)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditPaste))
        self.consolebutton.setIcon(icon1)

        self.mainlayout2.addWidget(self.consolebutton)

        self.runbutton = QPushButton(self.verticalLayoutWidget_4)
        self.runbutton.setObjectName(u"runbutton")
        self.runbutton.setFont(font1)
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.runbutton.setIcon(icon2)

        self.mainlayout2.addWidget(self.runbutton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CMMDT Fisch Macro Panel (ALPHA)", None))
        self.skipshake.setText(QCoreApplication.translate("MainWindow", u"Skip Shake", None))
        self.visual_indicators.setText(QCoreApplication.translate("MainWindow", u"Show visual indicators", None))
        self.castdurationlabel.setText(QCoreApplication.translate("MainWindow", u"Cast Duration:", None))
        self.latencylabel.setText(QCoreApplication.translate("MainWindow", u"Shake Speed:", None))
        self.controllabel.setText(QCoreApplication.translate("MainWindow", u"Control:", None))
        self.stopbutton.setText(QCoreApplication.translate("MainWindow", u"Stop (Control + X)", None))
        self.consolebutton.setText(QCoreApplication.translate("MainWindow", u"Console", None))
        self.runbutton.setText(QCoreApplication.translate("MainWindow", u"Start Macro", None))
    # retranslateUi

