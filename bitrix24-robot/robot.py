import requests
import datetime
import time
import logging
import os
from config import WEBHOOK_URL, TASK_SETTINGS, CREATE_INTERVAL_MINUTES

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler("robot.log", encoding="utf-8"),
        logging.StreamHandler()   # вывод в терминал
    ]
)
logger = logging.getLogger(__name__)

logger.info("🚀 Полноценный Bitrix24 Robot запущен")

def call_method(method, params=None):
    """Надёжный вызов методов Bitrix24 с повторными попытками"""
    if params is None:
        params = {}
    
    url = f"{WEBHOOK_URL}{method}.json"
    
    for attempt in range(1, 4):
        try:
            logger.info(f"Попытка {attempt}/3 → {method}")
            response = requests.post(url, json=params, timeout=(10, 45))
            response.raise_for_status()
            data = response.json()
            
            if "error" in data:
                logger.error(f"Bitrix24 ошибка: {data.get('error_description', data['error'])}")
                return None
            
            logger.info(f"Успешно выполнен: {method}")
            return data.get("result")
            
        except requests.exceptions.ReadTimeout:
            logger.warning(f"Таймаут на попытке {attempt}. Ждём 7 секунд...")
            time.sleep(7)
        except Exception as e:
            logger.error(f"Ошибка на попытке {attempt}: {e}")
            if attempt == 3:
                return None
            time.sleep(5)
    
    logger.error(f"Не удалось выполнить {method} после 3 попыток")
    return None


def создать_задачу():
    """Создаёт задачу"""
    now = datetime.datetime.now()
    task_fields = {
        "TITLE": f"{TASK_SETTINGS['TITLE_PREFIX']} — {now.strftime('%Y-%m-%d %H:%M')}",
        "DESCRIPTION": TASK_SETTINGS['DESCRIPTION'] + 
                      f"Дата создания: {now.strftime('%Y-%m-%d %H:%M:%S')}\nСоздано роботом",
        "RESPONSIBLE_ID": TASK_SETTINGS['RESPONSIBLE_ID'],
        "DEADLINE": (now + datetime.timedelta(days=TASK_SETTINGS['DEADLINE_DAYS'])).strftime("%Y-%m-%d 18:00:00"),
        "PRIORITY": TASK_SETTINGS['PRIORITY'],
        "TAGS": TASK_SETTINGS['TAGS']
    }
    
    result = call_method("tasks.task.add", {"fields": task_fields})
    
    if result and isinstance(result, dict) and "task" in result:
        task_id = result["task"]["id"]
        logger.info(f"✅ Задача создана! ID = {task_id} | {task_fields['TITLE']}")
        return task_id
    else:
        logger.error("❌ Не удалось создать задачу")
        return None


def завершить_задачу(task_id, delay_minutes=10):
    """Завершает задачу через delay_minutes минут после создания"""
    if not task_id:
        return
    
    logger.info(f"⏳ Задача {task_id} будет завершена через {delay_minutes} минут...")
    time.sleep(delay_minutes * 60)
    
    result = call_method("tasks.task.complete", {"taskId": task_id})
    if result:
        logger.info(f"✅ Задача {task_id} успешно завершена!")
    else:
        logger.warning(f"⚠️ Не удалось завершить задачу {task_id}")


if __name__ == "__main__":
    logger.info(f"Интервал создания задач: {CREATE_INTERVAL_MINUTES} минут")
    logger.info("Для остановки нажми Ctrl + C\n")

    try:
        while True:
            task_id = создать_задачу()
            
            
            if task_id:
                # Завершаем задачу через 10 минут 
                завершить_задачу(task_id, delay_minutes=10)
            
            logger.info(f"⏳ Следующая задача будет создана через {CREATE_INTERVAL_MINUTES} минут...\n")
            time.sleep(CREATE_INTERVAL_MINUTES * 60)

    except KeyboardInterrupt:
        logger.info("🛑 Робот остановлен вручную (Ctrl + C)")
    except Exception as e:
        logger.error(f"Критическая ошибка: {e}")
    finally:
        logger.info("Робот завершил работу.")