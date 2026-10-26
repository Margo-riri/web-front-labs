from flask import Flask, url_for, request, redirect, abort, render_template
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
import datetime
app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
# список логов
access_log = []

@app.errorhandler(404)
def not_found(err):
    path = url_for("static", filename="lab1/404.jpg")
    user_ip = request.remote_addr
    access_time = str(datetime.datetime.now())
    requested_url = request.url

    # добавляем запись в журнал
    access_log.append(f"[{access_time}] пользователь {user_ip} зашёл на адрес: {requested_url}")

    log_html = "<ul>"
    for entry in reversed(access_log):  # последние записи сверху
        log_html += f"<li>{entry}</li>"
    log_html += "</ul>"

    return '''
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Страница не найдена</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background: #f0f4f8;
                color: #333;
                margin: 0;
                padding: 0;
            }

            h1 {
                margin-top: 50px;
                font-size: 2em;
                color: #c0392b;
            }

            img {
                margin-top: 30px;
                max-width: 50%;
                height: auto;
                border-radius: 10px;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
            }
        </style>
    </head>
    <body>
        <h1>Нет такой страницы...</h1>
        <img src="''' + path + '''" alt="Страница не найдена">
    </body>
</html>
''', 404


@app.route("/index")
@app.route("/")
def index():
    return '''
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background: #F8D7DA;
            }

            header {
                background: #65A30D;
                color: white;
                padding: 20px;
                text-align: center;
            }

            nav {
                margin: 20px;
                text-align: center;
            }

            nav a {
                text-decoration: none;
                color: #388E50;
                font-weight: bold;
                padding: 10px;
            }

            nav a:hover {
                color: #205C32;
                text-decoration: underline;
            }

            footer {
                background: #E8BFC5;
                color: #68434A;
                text-align: center;
                padding: 10px;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
        </header>

        <nav>
            <a href="/lab1">Первая лабораторная</a><br>
            <a href="/lab2">Вторая лабораторная</a><br>
            <a href="/lab3">Третья лабораторная</a>
        </nav>

        <footer>
            Размахнина Маргарита Михайловна, ФБИ-44, 3 курс, 2026
        </footer>
    </body>
</html>
'''


@app.errorhandler(500)
def internal_error(err):
    return '''
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Ошибка сервера</title>
        <style>
            body {
                text-align: center;
                background: #f8d7da;
                color: #721c24;
                margin: 0;
                padding: 50px;
            }
        </style>
    </head>
    <body>
        <h1>Внутренняя ошибка сервера (500)</h1>
        <p>Произошла непредвиденная ошибка на сервере</p>
    </body>
</html>
''', 500, {
        "Content-Language": "ru"
    }

if __name__ == '__main__':
    app.run(debug=True)