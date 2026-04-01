import requests
import time

# Вставь сюда свой вебхук Bitrix24
WEBHOOK_URL = "https://b24-rvt9hx.bitrix24.ru/rest/1/2gy8vp8qb9efvk9h/"

def create_task(title, description, responsible_id):
    url = WEBHOOK_URL + "tasks.task.add.json"
    data = {
        "fields": {
            "TITLE": title,
            "DESCRIPTION": description,
            "RESPONSIBLE_ID": responsible_id
        }
    }
    response = requests.post(url, json=data, verify=False)
    if response.status_code == 200:
        result = response.json()
        if "result" in result:
            print(f"Задача создана! ID: {result['result']['task']['id']}")
        else:
            print(f"Ошибка: {result}")
    else:
        print(f"Ошибка HTTP {response.status_code}: {response.text}")

# ======== НАСТРОЙКИ ========
INTERVAL = 60  # интервал между задачами в секундах
RESPONSIBLE_ID = 1  # ID пользователя, на которого создаются задачи
# ===========================

counter = 1  # счётчик для уникальности задач

while True:
    title = f"Залачи с ума сходят, я вообще в шоке {counter}"
    description = "Эта задача создана автоматически роботом Python"
    
    create_task(title, description, RESPONSIBLE_ID)
    
    counter += 1
    print(f"Ждём {INTERVAL} секунд до следующей задачи...\n")
    time.sleep(INTERVAL)