"""
==================================================
AI Studio Pro Enterprise
Professional Logging System
==================================================
"""

import logging
from pathlib import Path

from app.config.settings import LOGS_DIR

# Create logs directory
LOGS_DIR.mkdir(exist_ok=True)

LOG_FILE = LOGS_DIR / "ai_studio.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("AIStudio")