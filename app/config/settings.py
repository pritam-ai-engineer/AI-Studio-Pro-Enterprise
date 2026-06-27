"""
==========================================================
AI Studio Pro Enterprise
Configuration Module
==========================================================
"""

from pathlib import Path

# --------------------------------------------------------
# Application Information
# --------------------------------------------------------

APP_NAME = "AI Studio Pro Enterprise"

VERSION = "1.0.0"

AUTHOR = "Pritam Kumar"

COMPANY = "AI Media Network"

# --------------------------------------------------------
# Root Directories
# --------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

APP_DIR = ROOT_DIR / "app"

ASSETS_DIR = ROOT_DIR / "assets"

CONTENT_DIR = ROOT_DIR / "content"

DATABASE_DIR = ROOT_DIR / "data"

DOCS_DIR = ROOT_DIR / "docs"

TESTS_DIR = ROOT_DIR / "tests"

LOGS_DIR = ROOT_DIR / "logs"

# --------------------------------------------------------
# Database
# --------------------------------------------------------

DATABASE_NAME = "ai_studio.db"

DATABASE_PATH = DATABASE_DIR / DATABASE_NAME

# --------------------------------------------------------
# Window
# --------------------------------------------------------

WINDOW_WIDTH = 1500

WINDOW_HEIGHT = 900

WINDOW_TITLE = f"{APP_NAME} v{VERSION}"

# --------------------------------------------------------
# Theme
# --------------------------------------------------------

THEME = "Light"

# --------------------------------------------------------
# Character Folder
# --------------------------------------------------------

CHARACTER_DIR = CONTENT_DIR / "characters"

EPISODE_DIR = CONTENT_DIR / "episodes"

PROMPT_DIR = CONTENT_DIR / "prompts"

PROJECT_DIR = CONTENT_DIR / "projects"