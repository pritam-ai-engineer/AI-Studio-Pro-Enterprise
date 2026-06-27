"""
============================================================
UI Builder
============================================================
"""

from app.gui.layouts import MainSplitter
from app.gui.widgets.sidebar import SidebarWidget
from app.gui.workspace import Workspace


class UIBuilder:
    """
    Builds the main application UI.
    """

    @staticmethod
    def build(main_window):
        splitter = MainSplitter()

        sidebar = SidebarWidget()

        workspace = Workspace()

        splitter.addWidget(sidebar)

        splitter.addWidget(workspace)

        main_window.setCentralWidget(splitter)

        return sidebar, workspace