# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drawing.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.button = QDialogButtonBox(Dialog)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(150, 270, 81, 241))
        self.button.setOrientation(Qt.Vertical)
        self.button.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 20, 341, 231))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.retranslateUi(Dialog)
        self.button.accepted.connect(Dialog.accept)
        self.button.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
    # retranslateUi


