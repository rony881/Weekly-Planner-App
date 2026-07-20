import json
from config import WEEKLY_SCHEDULE_FILE
from core.utils.logger import logger


def load_schedule() -> dict[str, list[list]]:
    """Load weekly schedule from JSON file."""
    
    if not WEEKLY_SCHEDULE_FILE.exists():
        logger.error(f"Schedule file not found: {WEEKLY_SCHEDULE_FILE}")
        raise FileNotFoundError(f"Schedule file not found: {WEEKLY_SCHEDULE_FILE}")
        
    try:
        with open(WEEKLY_SCHEDULE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info(f"Successfully loaded schedule from {WEEKLY_SCHEDULE_FILE}")
            return data
            
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in schedule file: {e}")
        raise
        
    except OSError as e:
        logger.error(f"Failed to read schedule file: {e}")
        raise

def save_schedule(data: dict) -> None:
    """Save weekly schedule to JSON file."""
    
    try:
        WEEKLY_SCHEDULE_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(WEEKLY_SCHEDULE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        logger.info(f"Successfully saved schedule to {WEEKLY_SCHEDULE_FILE}")
        
    except OSError as e:
        logger.error(f"Failed to save schedule file: {e}")
        raise