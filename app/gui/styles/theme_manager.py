"""
Theme Manager
"""

from PySide6.QtWidgets import QApplication


class ThemeManager:
    """
    Handles application themes.
    """

    @staticmethod
    def apply_light(app: QApplication):

        app.setStyle("Fusion")

    @staticmethod
    def apply_dark(app: QApplication):

        app.setStyle("Fusion")

        app.setStyleSheet("""
            QWidget{
                background:#2b2b2b;
                color:white;
            }

            QListWidget{
                background:#353535;
            }

            QMenuBar{
                background:#2b2b2b;
            }

            QStatusBar{
                background:#2b2b2b;
            }
        """)