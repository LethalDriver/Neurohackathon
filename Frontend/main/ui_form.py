# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QGridLayout, QListView,
    QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.gridLayout_4 = QGridLayout(Widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.dockWidget_2 = QDockWidget(Widget)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.gridLayout_5 = QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.listView_2 = QListView(self.dockWidgetContents_3)
        self.listView_2.setObjectName(u"listView_2")

        self.gridLayout_5.addWidget(self.listView_2, 0, 0, 1, 1)

        self.dockWidget_2.setWidget(self.dockWidgetContents_3)

        self.gridLayout_4.addWidget(self.dockWidget_2, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
    # retranslateUi

