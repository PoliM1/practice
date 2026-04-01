from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from bitrix24_client import Bitrix24API

bitrix_api = Bitrix24API()
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


class TaskCreate(BaseModel):
    title: str
    responsible_id: int = 1


@app.post("/api/b24-task/")
async def create_b24_task(task: TaskCreate):
    try:
        result = bitrix_api.call("tasks.task.add", {
            "fields": {
                "TITLE": task.title,
                "RESPONSIBLE_ID": task.responsible_id,
                "DEADLINE": "2026-04-05T18:00:00"
            }
        })
        return {
            "success": True,
            "task_id": result["task"]["id"]
        }
    except Exception as e:
        return {"success": False, "error": str(e)}


@app.get("/")
async def home():
    html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Home</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            background: linear-gradient(45deg, #ecd36e, #ff6b9d, #ff89de, #e7d693);
            position: relative;
            font-family: Arial, sans-serif;
        }

        h1 {
            position: absolute;
            top: 105px;
            left: 50%;
            transform: translateX(-50%);
            color: #bd009a;
            font-size: 3em;
            font-weight: bold;
            text-align: center;
        }

        .main-btn {
            position: absolute;
            bottom: 50px;
            left: 50%;
            transform: translateX(-50%);
            padding: 15px 40px;
            font-size: 1.3em;
            background: linear-gradient(45deg, #ffc664, #ffff9f);
            color: #000;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 10px 30px rgba(255, 107, 157, 0.4);
        }

        .img-center, .img-left, .img-right {
            position: absolute;
            transform: translate(-50%, -50%);
            height: auto;
        }

        .img-center {
            top: 400px;
            left: 50%;
            width: 90px;
        }

        .img-left {
            top: 500px;
            left: 20%;
            width: 200px;
        }

        .img-right {
            top: 300px;
            left: 80%;
            width: 200px;
        }
    </style>
</head>
<body>
    <h1>НУ ВОТ...🌸</h1>

    <img src="/static/images/logo.png" alt="Фото" class="img-center">
    <img src="/static/images/logo.png" alt="Фото" class="img-left">
    <img src="/static/images/logo.png" alt="Фото" class="img-right">

    <button class="main-btn" onclick="window.location.href='/about'">
        А дальше...🌸
    </button>
</body>
</html>
    """
    return HTMLResponse(html)


@app.get("/about")
async def about():
    html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Bitrix24 Task</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            background: linear-gradient(45deg, #ff828a, #ff6fe0);
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: Arial, sans-serif;
            position: relative;
            flex-direction: column;
        }

        h1 {
            color: rgb(0, 0, 0);
            font-size: 3em;
            text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
        }

        .task-box {
            margin-top: 20px;
            text-align: center;
        }

        input {
            padding: 15px;
            width: 250px;
            border-radius: 25px;
            border: 2px solid #C8A2C8;
        }

        .task-btn, .bonus-btn {
            background: linear-gradient(45deg, #C8A2C8, #E0BBE4);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 25px;
            font-size: 16px;
            cursor: pointer;
        }

        .bonus-btn {
            position: absolute;
            bottom: 50px;
            left: 50%;
            transform: translateX(-50%);
            background: linear-gradient(45deg, #ffc664, #ffff9f);
            color: black;
            font-size: 1.3em;
            box-shadow: 0 10px 30px rgba(255,107,157,0.4);
        }

        #status {
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>🌟 ДАЛЬШЕ БОНУС 🌟</h1>

    <div class="task-box">
        <input id="b24task" placeholder="Задача для Bitrix24">
        <br><br>
        <button class="task-btn" onclick="createB24Task()">🚀 Создать в B24</button>
        <div id="status"></div>
    </div>

    <button class="bonus-btn" onclick="window.location.href='/bonus'">
        БОНУС 🌸
    </button>

    <script>
        async function createB24Task() {
            const title = document.getElementById('b24task').value;

            if (!title) {
                alert('Введи название задачи!');
                return;
            }

            document.getElementById('status').innerHTML = '⏳ Создаём задачу...';

            try {
                const res = await fetch('/api/b24-task/', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({title, responsible_id: 1})
                });

                const result = await res.json();

                document.getElementById('status').innerHTML =
                    result.success
                        ? `✅ Задача создана! ID: ${result.task_id}`
                        : `❌ ${result.error}`;
            } catch (e) {
                document.getElementById('status').innerHTML = '❌ Ошибка сети';
            }
        }
    </script>
</body>
</html>
    """
    return HTMLResponse(html)


@app.get("/bonus")
async def bonus():
    html = """
    
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Bonus</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            background: linear-gradient(45deg, #ecd36e, #ff6b9d, #ff89de, #e7d693);
            position: relative;
            font-family: Arial, sans-serif;
        }

        h1 {
            position: absolute;
            top: 115px;
            left: 50%;
            transform: translateX(-50%);
            color: #bd009a;
            font-size: 2.5em;
            font-weight: bold;
            text-align: center;
        }

        .home-btn {
            position: absolute;
            bottom: 50px;
            left: 50%;
            transform: translateX(-50%);
            padding: 15px 40px;
            font-size: 1.3em;
            background: linear-gradient(45deg, #ffc664, #ffff9f);
            color: rgb(0, 0, 0);
            border: none;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 10px 30px rgba(255,107,157,0.4);
        }

        .bonus-img {
            position: absolute;
            top: 400px;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 500px;
            height: auto;
        }
    </style>
</head>
<body>
    <h1>А ВОТ И БОНУС ОТ ТОКСИСА🌸</h1>

    <img src="/static/images/video.gif" alt="Бонус" class="bonus-img">

    <button class="home-btn" onclick="window.location.href='/'">
        ДОМОЙ
    </button>
</body>
</html>
    """
    return HTMLResponse(html)