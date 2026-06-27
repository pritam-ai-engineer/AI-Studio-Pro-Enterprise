"""
============================================================
AI Studio Pro Enterprise

Module      : Main Window
Purpose     : Assemble the desktop shell
Author      : Pritam Kumar
Version     : 0.2.0-beta
============================================================
"""

from PySide6.QtWidgets import QMainWindow

from app.config.settings import (
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    WINDOW_WIDTH,
)

from app.controllers.navigation_controller import NavigationController

from app.gui.ui_builder import UIBuilder

from app.gui.widgets.menu_bar import MenuBarWidget
from app.gui.widgets.status_bar import StatusBarWidget
from app.gui.widgets.toolbar import ToolbarWidget


class MainWindow(QMainWindow):
    """
    Enterprise Main Window.

    Responsible only for assembling UI components.
    """

    def __init__(self):

        super().__init__()

        self.configure_window()

        self.create_menu()

        self.create_toolbar()

        self.create_workspace()

        self.create_statusbar()

        self.connect_navigation()

    # -------------------------------------------------
    # Window
    # -------------------------------------------------

    def configure_window(self):

        self.setWindowTitle(WINDOW_TITLE)

        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

    # -------------------------------------------------
    # Menu
    # -------------------------------------------------

    def create_menu(self):

        self.menu = MenuBarWidget(self)

        self.setMenuBar(self.menu)

    # -------------------------------------------------
    # Toolbar
    # -------------------------------------------------

    def create_toolbar(self):

        self.toolbar = ToolbarWidget(self)

        self.addToolBar(self.toolbar)

    # -------------------------------------------------
    # Central UI
    # -------------------------------------------------

    def create_workspace(self):

        (
            self.sidebar,
            self.workspace,
        ) = UIBuilder.build(self)

    # -------------------------------------------------
    # Status Bar
    # -------------------------------------------------

    def create_statusbar(self):

        self.status = StatusBarWidget()

        self.setStatusBar(self.status)

    # -------------------------------------------------
    # Navigation
    # -------------------------------------------------

    def connect_navigation(self):

        self.navigation = NavigationController(

            self.sidebar,

            self.workspace,

        )