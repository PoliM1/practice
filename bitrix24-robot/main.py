import requests
import datetime
import time

# ==================== ТВОЙ ВЕБХУК ====================
WEBHOOK_URL = "https://b24-rvt9hx.bitrix24.ru/rest/1/ipck001nfgsu7mw9/"

def call_method(method, params=None):
    """Универсальная функция вызова методов Bitrix24"""
    if params is None:
        params = {}
    
    url = f"{WEBHOOK_URL}{method}.json"
    
    try:
        response = requests.post(url, json=params, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        if "error" in data:
            print(f"❌ Bitrix24 ошибка: {data.get('error_description', data['error'])}")
            return None
        return data.get("result")
        
    except Exception as e:
        print(f"❌ Ошибка при вызове {method}: {e}")
        return None


def создать_задачу():
    """Создаёт задачу"""
    print("\n→ Создаём новую задачу...")
    
    task_fields = {
        "TITLE": "Тестовая задача от Python-робота (с задержкой)",
        "DESCRIPTION": "Задача создана автоматически.\nБудет завершена через 1 минуту.\nДата создания: " + 
                      datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "RESPONSIBLE_ID": 1,                    # ← Измени, если нужно
        "DEADLINE": (datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d 18:00:00"),
        "PRIORITY": "2",
        "TAGS": ["робот", "тест", "автозавершение"]
    }
    
    result = call_method("tasks.task.add", {"fields": task_fields})
    
    if result and isinstance(result, dict) and "task" in result:
        task_id = result["task"]["id"]
        print(f"✅ Задача создана! ID = {task_id}")
        return task_id
    else:
        print("❌ Не удалось создать задачу")
        return None


def завершить_задачу(task_id):
    """Завершает задачу"""
    if not task_id:
        return False
    
    print(f"→ Завершаем задачу ID {task_id}...")
    
    result = call_method("tasks.task.complete", {"taskId": task_id})
    
    if result:
        print(f"✅ Задача {task_id} успешно завершена!")
        return True
    else:
        print(f"⚠️ Не удалось завершить задачу {task_id}")
        return False


# ==================== ГЛАВНЫЙ ЗАПУСК ====================
if __name__ == "__main__":
    print("🚀 Python-робот Bitrix24 запущен")
    print("Задача будет создана и завершена через 1 минуту\n")

    # 1. Создаём задачу
    task_id = создать_задачу()

    if task_id:
        print(f"\n⏳ Ожидаем 60 секунд (1 минуту) перед завершением задачи...")
        
        # Отсчёт времени с красивым выводом
        for i in range(60, 0, -1):
            print(f"   Осталось {i} секунд...", end="\r")
            time.sleep(1)
        
        print("\n\n⏰ Время вышло! Завершаем задачу...")
        
        # 2. Завершаем задачу
        завершить_задачу(task_id)

    print("\n🎉 Работа робота завершена.")