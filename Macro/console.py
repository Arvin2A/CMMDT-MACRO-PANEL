from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QTextEdit,
    QWidget)
class Ui_Console(object):
    def setupUi(self, Console):
        if not Console.objectName():
            Console.setObjectName(u"Console")
        Console.resize(400, 350)
        Console.setMinimumSize(QSize(400, 350))
        self.log = QTextEdit(Console)
        self.log.setObjectName(u"log")
        self.log.setGeometry(QRect(0, 0, 401, 291))
        font = QFont()
        font.setPointSize(9)
        self.log.setFont(font)
        self.log.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.log.setReadOnly(True)
        self.closeconsole = QPushButton(Console)
        self.closeconsole.setObjectName(u"closeconsole")
        self.closeconsole.setGeometry(QRect(150, 300, 88, 34))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.closeconsole.setIcon(icon)

        self.retranslateUi(Console)

        QMetaObject.connectSlotsByName(Console)
    # setupUi

    def retranslateUi(self, Console):
        Console.setWindowTitle(QCoreApplication.translate("Console", u"Form", None))
        self.log.setPlaceholderText("")
        self.closeconsole.setText(QCoreApplication.translate("Console", u"Close", None))
    # retranslateUi

