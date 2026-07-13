# core/data_loader.py
import json
from config import LAST_LOADED_DAY_FILE, SLEEP_LOGS_FILE, WEEKLY_SCHEDULE_FILE,TODAYS_TASKS_FILE
from core.utils.logger import logger
from core.models.task import Task

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

def last_loaded_day() -> str | None:
    try:
        return LAST_LOADED_DAY_FILE.read_text(encoding="utf-8").strip()
    except OSError :
        return None

def save_todays_day(day: str) -> None:
    try:
        LAST_LOADED_DAY_FILE.parent.mkdir(parents=True, exist_ok=True)
        LAST_LOADED_DAY_FILE.write_text(day, encoding="utf-8")
    except OSError as e:
        logger.error(f"Failed to write last loaded day: {e}")

def load_todays_tasks(day: str) -> list[Task]:
    """Load today's tasks for the specified day."""
    try:
        schedule = load_schedule()
        
        if day not in schedule:
            logger.warning(f"Day '{day}' not found in schedule")
            return []
        
        if last_loaded_day() != day or not TODAYS_TASKS_FILE.exists():
            daily_tasks = []
            for time, task, prio in schedule[day]:
                daily_tasks.append(Task(
                    time=time,
                    task=task,
                    priority=prio,
                    done=False
                ))
            save_todays_tasks(daily_tasks)
            save_todays_day(day)
        
        with open(TODAYS_TASKS_FILE, "r", encoding="utf-8") as f:
            tasks_data = json.load(f)
            tasks = [Task.from_dict(t) for t in tasks_data]
            logger.info(f"Successfully loaded {len(tasks)} tasks for {day}")
            return tasks
            
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in tasks file: {e}")
        return []
    except (OSError, KeyError) as e:
        logger.error(f"Failed to load today's tasks: {e}")
        return []

def save_todays_tasks(tasks: list[Task]) -> None:
    """ Save today's tasks to JSON file. """
    
    try:
        TODAYS_TASKS_FILE.parent.mkdir(parents=True, exist_ok=True)
        task_data = [task.to_dict() for task in tasks]
        with open(TODAYS_TASKS_FILE, "w", encoding="utf-8") as f:
            json.dump(task_data, f, indent=4, ensure_ascii=False)
        logger.info(f"Successfully saved {len(tasks)} tasks to {TODAYS_TASKS_FILE}")
        
    except OSError as e:
        logger.error(f"Failed to save tasks file: {e}")
        raise


def load_sleep_logs() -> list[dict]:
    """Loads Sleep Logs History From JSON File """

    if not SLEEP_LOGS_FILE.exists():
        logger.error(f"File not found: {SLEEP_LOGS_FILE}")
        raise FileNotFoundError(f"File not found: {SLEEP_LOGS_FILE}")

    try:
        with open(SLEEP_LOGS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info(f"Successfully Loaded {SLEEP_LOGS_FILE}")

            return data
            
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in Logs file: {e}")
        raise

    except OSError as e:
        logger.error(f"Failed to read Logs file: {e}")
        raise

def save_sleep_logs(logs: list[dict]):
    """ Save Sleep Logs to JSON file. """

    try:
        SLEEP_LOGS_FILE.parent.mkdir(parents=True, exist_ok=True)
        
        with open(SLEEP_LOGS_FILE, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=4, ensure_ascii=False)
        logger.info(f"Successfully saved {len(logs)} sleep logs to {SLEEP_LOGS_FILE}")
        
    except OSError as e:
        logger.error(f"Failed to save Logs file: {e}")
        raise