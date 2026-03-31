from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def home():
    html = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
  margin: 0; height: 100vh;
  background: linear-gradient(45deg,#ecd36e, #ff6b9d, #ff89de, #e7d693);
  position: relative;
  font-family: Arial;
}
</style>
</head>
<body>
 

<button onclick="window.location.href='/about'" 
        style="
  /* 📍 ПОЗИЦИЯ */
  position: absolute; 
  bottom: 50px;      /* ↑ снизу: 20px=выше, 100px=ниже */
  left: 50%;         /* ← влево/вправо: 20%=влево, 80%=вправо */
  transform: translateX(-50%);  /* центр по горизонтали */
  
  /* 📏 РАЗМЕР */
  padding: 15px 40px;    /* высота x ширина: 20px 60px = больше */
  font-size: 1.3em;      /* текст: 1em=маленький, 2em=большой */
  
  /* 🎨 СТИЛИ */
  background: linear-gradient(45deg, #ffc664, #ffff9f); 
  color: rgb(0, 0, 0); border: none; border-radius: 50px; cursor: pointer;
  box-shadow: 0 10px 30px rgba(255,107,157,0.4);
">
  А дальше...🌸
</button>

<!-- 🌸 ТЕКСТ — МЕНЯЙ top/left/РАЗМЕР 🌸 -->
<h1 style="
  position: absolute; 
  top: 105px;        /* ↑ВВЕРХ/НИЗ */
  left: 50%;         /* ←ВЛЕВО/ВПРАВО */
  transform: translateX(-50%);
  color: #bd009a; 
  font-size: 3em;  /* ← РАЗМЕР ТЕКСТА: 2em=большой, 1.5em=маленький */
  font-weight: bold;
  text-align: center;
">
  НУ ВОТ...🌸
</h1>

<!-- 🖼️ КАРТИНКА — МЕНЯЙ top/left/РАЗМЕР 🖼️ -->
<img src="/static/images/logo.png" alt="Фото" style="
  position: absolute; 
  top: 400px;        /* ↑ВВЕРХ/НИЗ */
  left: 50%;         /* ←ВЛЕВО/ВПРАВО */
  transform: translate(-50%, -50%);
  width: 370px;      /* ← РАЗМЕР ФОТО: 300px=меньше, 500px=больше */
  height: auto;      /* сохраняет пропорции */
">


<img src="/static/images/logo.png" alt="Фото" style="
  position: absolute; 
  top: 500px;        /* ↑ВВЕРХ/НИЗ */
  left: 20%;         /* ←ВЛЕВО/ВПРАВО */
  transform: translate(-50%, -50%);
  width: 370px;      /* ← РАЗМЕР ФОТО: 300px=меньше, 500px=больше */
  height: auto;      /* сохраняет пропорции */
">


<img src="/static/images/logo.png" alt="Фото" style="
  position: absolute; 
  top: 300px;        /* ↑ВВЕРХ/НИЗ */
  left: 80%;         /* ←ВЛЕВО/ВПРАВО */
  transform: translate(-50%, -50%);
  width: 370px;      /* ← РАЗМЕР ФОТО: 300px=меньше, 500px=больше */
  height: auto;      /* сохраняет пропорции */
">


</style>
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
<style>
body {
  margin: 0; height: 100vh;
  background: linear-gradient(45deg, #ff828a, #ff6fe0);
  display: flex; align-items: center; justify-content: center;
  font-family: Arial;
}
h1 { color: rgb(0, 0, 0); font-size: 3em; text-shadow: 2px 2px 10px rgba(0,0,0,0.3); }
</style>
</head>
<body>
  <h1>🌟 ДАЛЬШЕ БОНУС 🌟</h1>
<button onclick="window.location.href='/bonus'"
        style="
  /* 📍 ПОЗИЦИЯ */
  position: absolute; 
  bottom: 50px;      /* ↑ снизу: 20px=выше, 100px=ниже */
  left: 50%;         /* ← влево/вправо: 20%=влево, 80%=вправо */
  transform: translateX(-50%);  /* центр по горизонтали */
  
  /* 📏 РАЗМЕР */
  padding: 15px 40px;    /* высота x ширина: 20px 60px = больше */
  font-size: 1.3em;      /* текст: 1em=маленький, 2em=большой */
  
  /* 🎨 СТИЛИ */
  background: linear-gradient(45deg, #ffc664, #ffff9f); 
  color: rgb(0, 0, 0); border: none; border-radius: 50px; cursor: pointer;
  box-shadow: 0 10px 30px rgba(255,107,157,0.4);
">
  БОНУС 🌸 
</button>
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
<style>
body {
  margin: 0; height: 100vh;
  background: linear-gradient(45deg,#ecd36e, #ff6b9d, #ff89de, #e7d693);
  position: relative;
  font-family: Arial;
}
</style>
</head>
<body>
 

<button onclick="window.location.href='/'" 
        style="
  /* 📍 ПОЗИЦИЯ */
  position: absolute; 
  bottom: 50px;      /* ↑ снизу: 20px=выше, 100px=ниже */
  left: 50%;         /* ← влево/вправо: 20%=влево, 80%=вправо */
  transform: translateX(-50%);  /* центр по горизонтали */
  
  /* 📏 РАЗМЕР */
  padding: 15px 40px;    /* высота x ширина: 20px 60px = больше */
  font-size: 1.3em;      /* текст: 1em=маленький, 2em=большой */
  
  /* 🎨 СТИЛИ */
  background: linear-gradient(45deg, #ffc664, #ffff9f); 
  color: rgb(0, 0, 0); border: none; border-radius: 50px; cursor: pointer;
  box-shadow: 0 10px 30px rgba(255,107,157,0.4);
">
  ДОМОЙ
</button>

<!-- 🌸 ТЕКСТ — МЕНЯЙ top/left/РАЗМЕР 🌸 -->
<h1 style="
  position: absolute; 
  top: 115px;        /* ↑ВВЕРХ/НИЗ */
  left: 50%;         /* ←ВЛЕВО/ВПРАВО */
  transform: translateX(-50%);
  color: #bd009a; 
  font-size: 2.5em;  /* ← РАЗМЕР ТЕКСТА: 2em=большой, 1.5em=маленький */
  font-weight: bold;
  text-align: center;
">
  А ВОТ И БОНУС ОТ ТОКСИСА🌸
</h1>

<!-- 🖼️ ВИДЕО — МЕНЯЙ top/left/РАЗМЕР 🖼️ -->
<img
  src="/static/images/video.gif"
  alt="Бонус"
  style="
    position: absolute;
    top: 400px;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 500px;
    height: auto;
  ">

</style>
</body>
</html>
    """
    return HTMLResponse(html)