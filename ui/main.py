# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import os

class UiMainWindow(QtGui.QMainWindow):
    
    def __init__(self, autoConfigure=True):
        """
        Constructs the main window
        """
        super(QtGui.QMainWindow, self).__init__()

        self.iconPath = os.getcwd() + "/icons/"

        self.setWindowTitle("Openbox menu configuration")
        self.setWindowIcon(QtGui.QIcon(self.iconPath + "mnu48.png"))

        if autoConfigure:
            self.initActions()
            self.initMenu()
            self.initToolbar()

        self.statusBar().showMessage("Ready")
        

    def initMenu(self):
        """
        Configures menu
        """	
        menu = self.menuBar()

        # --- File Menu ---

        menuFile = menu.addMenu("&File")
        menuFile.addAction(self.menuActionNew)
        menuFile.addAction(self.menuActionOpen)
        menuFile.addAction(self.menuActionSave)
        menuFile.addAction(self.menuActionSaveAs)
        menuFile.addSeparator()
        menuFile.addAction(self.menuActionQuit)
        
        # --- Edit Menu ---

        menuEdit = menu.addMenu("&Edit")
        menuEdit.addAction(self.menuActionMoveUp)
        menuEdit.addAction(self.menuActionMoveDown)
        menuEdit.addSeparator()
        menuEdit.addAction(self.menuActionDelete)

        # --- Add Menu ---

        menuAdd = menu.addMenu("&Add")
        menuAdd.addAction(self.menuActionMenu)
        menuAdd.addAction(self.menuActionItem)
        menuAdd.addAction(self.menuActionSeparator)
        menuAdd.addAction(self.menuActionPipe)
        menuAdd.addAction(self.menuActionLink)

        # --- Help Menu ---

        menuHelp = menu.addMenu("&Help")
        menuHelp.addAction(self.menuActionAbout)


    def initActions(self):
        """
        Configures main actions
        """
        # New
        self.menuActionNew = QtGui.QAction(QtGui.QIcon(self.iconPath + "document-new.png"), "New", self)
        self.menuActionNew.setShortcut("Ctrl+N")
        self.menuActionNew.setStatusTip("New menu file")

        # Open
        self.menuActionOpen = QtGui.QAction(QtGui.QIcon(self.iconPath + "document-open.png"), "Open...", self)
        self.menuActionOpen.setShortcut("Ctrl+O")
        self.menuActionOpen.setStatusTip("Open menu file...")
        
        # Save
        self.menuActionSave = QtGui.QAction(QtGui.QIcon(self.iconPath + "document-save.png"), "Save", self)
        self.menuActionSave.setShortcut("Ctrl+S")
        self.menuActionSave.setStatusTip("Save current menu")

        # Save As
        self.menuActionSaveAs = QtGui.QAction(QtGui.QIcon(self.iconPath + "document-save-as.png"), "Save As...", self)
        self.menuActionSaveAs.setShortcut("Ctrl+Shift+S")
        self.menuActionSaveAs.setStatusTip("Save menu as...")
        
        # Exit
        self.menuActionQuit = QtGui.QAction(QtGui.QIcon(self.iconPath + "system-shutdown.png"), "Quit", self)
        self.menuActionQuit.setShortcut("Ctrl+Q")
        self.menuActionQuit.setStatusTip("Exits menu editor")

        # Move up
        self.menuActionMoveUp = QtGui.QAction(QtGui.QIcon(self.iconPath + "go-up.png"), "Move up", self)
        self.menuActionMoveUp.setShortcut("Ctrl+Up")
        self.menuActionMoveUp.setStatusTip("Move item up")

        # Move down
        self.menuActionMoveDown = QtGui.QAction(QtGui.QIcon(self.iconPath + "go-down.png"), "Move down", self)
        self.menuActionMoveDown.setShortcut("Ctrl+Down")
        self.menuActionMoveDown.setStatusTip("Move item down")

        # Delete
        self.menuActionDelete = QtGui.QAction(QtGui.QIcon(self.iconPath + "edit-delete.png"), "Delete", self)
        self.menuActionDelete.setStatusTip("Delete selected item")    

        # Menu
        self.menuActionMenu = QtGui.QAction(QtGui.QIcon(self.iconPath + "archive-insert-directory.png"), "Menu", self)
        self.menuActionMenu.setIconText("New menu")
        self.menuActionMenu.setIconVisibleInMenu(False)
        self.menuActionMenu.setStatusTip("Add menu")
        
        # Item
        self.menuActionItem = QtGui.QAction(QtGui.QIcon(self.iconPath + "document-new.png"), "Item", self)
        self.menuActionItem.setIconText("New item")
        self.menuActionItem.setIconVisibleInMenu(False)
        self.menuActionItem.setStatusTip("Add item")
        
        # Separator
        self.menuActionSeparator = QtGui.QAction(QtGui.QIcon(self.iconPath + "zoom-fit-width.png"), "Separator", self)
        self.menuActionSeparator.setIconText("New separator")
        self.menuActionSeparator.setIconVisibleInMenu(False)
        self.menuActionSeparator.setStatusTip("Add separator")

        # Link
        self.menuActionLink = QtGui.QAction("Link", self)
        self.menuActionLink.setStatusTip("Add link")

        # Pipemenu
        self.menuActionPipe = QtGui.QAction("Pipemenu", self)
        self.menuActionPipe.setStatusTip("Add pipemenu")

        # About
        self.menuActionAbout = QtGui.QAction("About", self)
        self.menuActionAbout.setStatusTip("About")      


    def initToolbar(self):
        """
        Configures main toolbar
        """
        toolbar = self.addToolBar('Exit')
        toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        # toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)

        toolbar.addAction(self.menuActionSave)
        toolbar.addSeparator()
        toolbar.addAction(self.menuActionMenu)
        toolbar.addAction(self.menuActionItem)
        toolbar.addAction(self.menuActionSeparator)
        toolbar.addSeparator()
        toolbar.addAction(self.menuActionMoveUp)
        toolbar.addAction(self.menuActionMoveDown)
        toolbar.addSeparator()
        toolbar.addAction(self.menuActionDelete)

        