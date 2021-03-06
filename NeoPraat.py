#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import os
import sys
from PySide import QtCore
from PySide import QtGui
from PySide.QtCore import *
from PySide.QtGui import *
# Every Qt application must have one and only one QApplication object;
# it receives the command line arguments passed to the script, as they
# can be used to customize the application's appearance and behavior


class multiLanguage:
    def __init__(self):
        if os.path.exists("./locale"):
            pass
        else:
            print("Error, Cannot find language settings")
    def languageSelector(self):
        '''Create a selection window based on the LANGUAGE.json file found under locale directory.'''
        localeLIST = [x for x in os.listdir("./locale/") if x.endswith("json")]
    def languageSetting(self):
        return json.loads(open("./NeoPraat.cfg").read())["locale"]


class MainWindow(QWidget):
    ''' An example of PySide absolute positioning; the main window
        inherits from QWidget, a convenient widget for an empty window. '''
    def __init__(self):
        # Initialize the object as a QWidget
        QWidget.__init__(self)

        # We have to set the size of the main window
        # ourselves, since we control the entire layout
        self.setMinimumSize(600, 700)
        self.setWindowTitle('NeoPraat')
        self.createMenu()
        # Create the controls with this object as their parent and set
        # their position individually; each row is a label followed by
        # another control
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.setMenuBar(self.menuBar)
        self.setLayout(mainLayout)
        # Label for the salutation chooser

    def run(self):
        # Show the form
        self.show()
        # Run the Qt application
        qt_app.exec_()

    def createMenu(self):
        multiLang = multiLanguage()
        locale = json.load(open("./locale/{0}.json".format(multiLang.languageSetting())))
        self.menuBar       = QtGui.QMenuBar()
        self.neoPraatMenu  = QtGui.QMenu(locale["NeoPraat"], self)
        self.aboutNeoPraat = self.neoPraatMenu.addAction(locale["About NeoPraat"])
        self.newScript     = self.neoPraatMenu.addAction(locale["New Script"])
        self.openScript    = self.neoPraatMenu.addAction(locale["Open Script"])
        self.calculator    = self.neoPraatMenu.addAction(locale["Calculator"])
        self.preferences   = self.neoPraatMenu.addMenu(locale["Preferences"])
        self.preferences.addAction(locale["Sound Recording Preferences"])
        self.preferences.addAction(locale["Sound Playing Preferences"])
        self.preferences.addAction(locale["NeoPraat Preferences"])
        self.quit = self.neoPraatMenu.addAction(locale["Quit"])
        self.newMenu = QtGui.QMenu(locale["New"])
        self.newMenu.addAction(locale["Record mono track sound"])
        self.newMenu.addAction(locale["Record stereo track sound"])
        self.createMenu = self.newMenu.addMenu(locale["Create sound"])
        self.createMenu.addAction(locale["Create pure tone"])
        self.createMenu.addAction(locale["Create complex tone"])
        self.createMenu.addAction(locale["Create sound from formula"])
        self.createMenu.addAction(locale["Create sound from gamatone"])
        self.createMenu.addAction(locale["Create sound from separd tone"])
        self.createMenu.addAction(locale["Create sound from vowel editor"])
        self.createMenu.addAction(locale["Create sound from speech synthesizer"])
        self.openMenu = QtGui.QMenu(locale["Open"])
        self.saveMenu = QtGui.QMenu(locale["Save"])
        self.helpMenu = QtGui.QMenu(locale["Help"])
        self.menuBar.addMenu(self.neoPraatMenu)
        self.menuBar.addMenu(self.newMenu)
        self.menuBar.addMenu(self.openMenu)
        self.menuBar.addMenu(self.saveMenu)
        self.menuBar.addMenu(self.helpMenu)


if __name__ == '__main__':
    # Create an instance of the application window and run it
    qt_app = QApplication(sys.argv)
    app = MainWindow()
    app.run()