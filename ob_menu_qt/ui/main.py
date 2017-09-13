from PyQt5 import QtGui, QtCore, QtWidgets
from ob_menu_qt.ui.obmenuwidget import ObMenuWidget
from ob_menu_qt.ui.aboutwidget import ObAboutWidget


class UiMainWindow(QtWidgets.QMainWindow):

    def __init__(self,
                 version, auto_configure=True, icon_path=None, file_path=None):
        """
        Constructs the main window
        """
        super(QtWidgets.QMainWindow, self).__init__()

        self.version = version

        # openbox menu widget
        self.frmMenu = ObMenuWidget(icon_path=icon_path)
        self.frmMenu.show()
        self.setCentralWidget(self.frmMenu)

        # window configs
        self.icon_path = icon_path
        self.setWindowTitle("Openbox menu configuration " + self.version)
        self.setWindowIcon(QtGui.QIcon(self.icon_path + "mnu48.png"))

        # about widget
        self.frmAbout = None

        if auto_configure:
            self._prepare_about_widget()
            self.initActions()
            self.initMenu()
            self.initToolbar()

        self.statusBar().showMessage("Ready")

        self.setMinimumSize(740, 580)


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
        menuHelp.addAction(self.menuActionAboutQt)
        menuHelp.addAction(self.menuActionAbout)

    def initActions(self):
        """
        Configures main actions
        """
        # New
        self.menuActionNew = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('document-new'), "New", self)
        self.menuActionNew.setShortcut("Ctrl+N")
        self.menuActionNew.setStatusTip("New menu file")
        self.menuActionNew.triggered.connect(self.frmMenu.new_menu_file)

        # Open
        self.menuActionOpen = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('document-open'), "Open...", self)
        self.menuActionOpen.setShortcut("Ctrl+O")
        self.menuActionOpen.setStatusTip("Open menu file...")
        self.menuActionOpen.triggered.connect(self.frmMenu.open_menu_file)

        # Save
        self.menuActionSave = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('document-save'), "Save", self)
        self.menuActionSave.setShortcut("Ctrl+S")
        self.menuActionSave.setDisabled(True)
        self.menuActionSave.setStatusTip("Save current menu")
        self.menuActionSave.triggered.connect(self.frmMenu.save_changes)

        # Save As
        self.menuActionSaveAs = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('document-save-as'), "Save As...", self)
        self.menuActionSaveAs.setShortcut("Ctrl+Shift+S")
        self.menuActionSaveAs.setStatusTip("Save menu as...")
        self.menuActionSaveAs.triggered.connect(self.frmMenu.save_menu_as)

        # Exit
        self.menuActionQuit = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('system-shutdown'), "Quit", self)
        self.menuActionQuit.setShortcut("Ctrl+Q")
        self.menuActionQuit.setStatusTip("Exits menu editor")
        self.menuActionQuit.triggered.connect(self.close)

        # Move up
        self.menuActionMoveUp = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('go-up'), "Move up", self)
        self.menuActionMoveUp.setDisabled(True)
        self.menuActionMoveUp.setShortcut("Ctrl+Up")
        self.menuActionMoveUp.setStatusTip("Move item up")
        self.menuActionMoveUp.triggered.connect(self.frmMenu.move_item_up)

        # Move down
        self.menuActionMoveDown = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('go-down'), "Move down", self)
        self.menuActionMoveDown.setDisabled(True)
        self.menuActionMoveDown.setShortcut("Ctrl+Down")
        self.menuActionMoveDown.setStatusTip("Move item down")
        self.menuActionMoveDown.triggered.connect(self.frmMenu.move_item_down)

        # Delete
        self.menuActionDelete = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('edit-delete'), "Delete", self)
        self.menuActionDelete.setDisabled(True)
        self.menuActionDelete.setStatusTip("Delete selected item")
        self.menuActionDelete.triggered.connect(self.frmMenu.remove_item)

        # New Menu
        self.menuActionMenu = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('archive-insert-directory'), "Menu", self)
        self.menuActionMenu.setIconText("New menu")
        self.menuActionMenu.setIconVisibleInMenu(False)
        self.menuActionMenu.setDisabled(True)
        self.menuActionMenu.setStatusTip("Add menu")
        self.menuActionMenu.triggered.connect(self.frmMenu.new_submenu)

        # New Item
        self.menuActionItem = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('document-new'), "Item", self)
        self.menuActionItem.setIconText("New item")
        self.menuActionItem.setIconVisibleInMenu(False)
        self.menuActionItem.setDisabled(True)
        self.menuActionItem.setStatusTip("Add item")
        self.menuActionItem.triggered.connect(self.frmMenu.new_item)

        # New Separator
        self.menuActionSeparator = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('zoom-fit-width'), "Separator", self)
        self.menuActionSeparator.setIconText("New separator")
        self.menuActionSeparator.setIconVisibleInMenu(False)
        self.menuActionSeparator.setDisabled(True)
        self.menuActionSeparator.setStatusTip("Add separator")
        self.menuActionSeparator.triggered.connect(self.frmMenu.new_separator)

        # New Link
        self.menuActionLink = QtWidgets.QAction("Link", self)
        self.menuActionLink.setDisabled(True)
        self.menuActionLink.setStatusTip("Add link")

        # New Pipemenu
        self.menuActionPipe = QtWidgets.QAction("Pipemenu", self)
        self.menuActionPipe.setDisabled(True)
        self.menuActionPipe.setStatusTip("Add pipemenu")

        # About Qt
        self.menuActionAboutQt = QtWidgets.QAction("About Qt", self)
        self.menuActionAboutQt.setStatusTip("About Qt")
        self.menuActionAboutQt.triggered.connect(
            lambda: QtWidgets.QMessageBox.aboutQt(self, "About Qt"))

        # About
        self.menuActionAbout = QtWidgets.QAction("About", self)
        self.menuActionAbout.setStatusTip("About")
        self.menuActionAbout.triggered.connect(self.frmAbout.show)

    def _prepare_about_widget(self):
        """
        Configures the default values for about widget
        """
        self.frmAbout = ObAboutWidget(self.icon_path)
        self.frmAbout.set_version(self.version)
        self.frmAbout.setupUi(QtWidgets.QWidget())

    def closeEvent(self, event):
        """
        Close event slot
        """
        self.frmAbout.close()
        event.accept()

    def initToolbar(self):
        """
        Configures main toolbar
        """
        toolbar = self.addToolBar('Exit')
        toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

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
