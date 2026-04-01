import requests

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

    response = requests.post(url, json=data)

    print("Статус:", response.status_code)
    print("Ответ:", response.text)

    


create_task(
    title="Тестовая задача из Python",
    description="Теперь точно сработает 🚀",
    responsible_id=1
)