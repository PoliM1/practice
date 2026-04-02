# ==================== НАСТРОЙКИ РОБОТА ====================

WEBHOOK_URL = "https://b24-rvt9hx.bitrix24.ru/rest/1/ipck001nfgsu7mw9/"

TASK_SETTINGS = {
    "TITLE_PREFIX": "Автозадача",
    "DESCRIPTION": "Задача создана автоматически Python-роботом.\n\n",
    "RESPONSIBLE_ID": 1,           # ← ОБЯЗАТЕЛЬНО ИЗМЕНИ НА СВОЙ ID!
    "DEADLINE_DAYS": 3,
    "PRIORITY": "2",
    "TAGS": ["робот", "автоматика"]
}

# Интервал создания новых задач
CREATE_INTERVAL_MINUTES = 181   # каждые 3 часа