from flask import Blueprint, url_for, request, redirect
import datetime
lab1 = Blueprint('lab1', __name__)


# список логов
access_log = []


@lab1.route("/lab1")
def lab():
    return '''
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Лабораторная 1</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                margin: 20px; 
                background: #E8BFC5; 
                color: #333; 
                line-height: 1.6
            }
            a { 
                color: #205C32; 
                font-weight: bold
            }
            a:hover { text-decoration: underline}
        </style>
    </head>
    <body>
        <p>«Чтоб жить честно, надо рваться, путаться, биться, шибаться, начинать и бросать, и опять начинать,
            и опять бросать, и вечно бороться и лишаться. А спокойствие – душевная подлость».</p>
        <p><a href="/">На главную</a></p>

        <h2>Список роутов</h2>
                <ul>
            <li><a href="/index">/index</a></li>
            <li><a href="/">/</a></li>
            <li><a href="/lab1">/lab1</a></li>
            <li><a href="/lab1/web">/lab1/web</a></li>
            <li><a href="/lab1/author">/lab1/author</a></li>
            <li><a href="/lab1/image">/lab1/image</a></li>
            <li><a href="/lab1/image/en">/lab1/image/en</a></li>
            <li><a href="/lab1/image/es">/lab1/image/es</a></li>
            <li><a href="/lab1/counter">/lab1/counter</a></li>
            <li><a href="/lab1/counter/reset">/lab1/counter/reset</a></li>
            <li><a href="/lab1/info">/lab1/info</a></li>
            <li><a href="/lab1/created">/lab1/created</a></li>
            <li><a href="/lab1/error/400">/lab1/error/400</a></li>
            <li><a href="/lab1/error/401">/lab1/error/401</a></li>
            <li><a href="/lab1/error/402">/lab1/error/402</a></li>
            <li><a href="/lab1/error/403">/lab1/error/403</a></li>
            <li><a href="/lab1/error/405">/lab1/error/405</a></li>
            <li><a href="/lab1/error/418">/lab1/error/418</a></li>
            <li><a href="/lab1/cause_error">/lab1/cause_error</a></li>
        </ul>
    </body>
</html>
'''


@lab1.route("/lab1/web")
def web():
    return """<!DOCTYPE html>
        <html>
           <body>
               <h1>web-сервер на flask</h1>
               <a href="l/ab1/author">author</a>
           </body>
        </html>""", 200, {
            'X-server': "sample",
            'Content-Type': 'text/plain; charset=utf-8'}


@lab1.route("/lab1/author")
def author():
    name = "Размахнина Маргарита Михайловна"
    group = "ФБИ-44"
    faculty = "ФБ"

    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href="/lab1/web">web</a>
            </body>
        </html>"""


@lab1.route("/lab1/image")
def image():
    path = url_for("static", filename="lab1/funny_dog.jpg")
    style = url_for("static", filename="lab1/lab1.css")

    return '''
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="''' + style + '''">
        <title>Смешной пёс</title>
    </head>
    <body>
        <h1>Смешной пёс</h1>
        <img src="''' + path + '''" alt="Смешной пёс">
        <p>
            <a href="/lab1/image/en">English</a> |
            <a href="/lab1/image/es">Español</a>
        </p>
    </body>
</html>
''', 200, {
        "Content-Language": "ru",
        "X-Image-Page": "funny-dog",
        "X-Framework": "Flask"
    }


@lab1.route("/lab1/image/en")
def image_en():
    path = url_for("static", filename="funny_dog.jpg")
    style = url_for("static", filename="lab1.css")

    return '''
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="''' + style + '''">
        <title>Funny dog</title>
    </head>
    <body>
        <h1>Funny dog</h1>
        <img src="''' + path + '''" alt="Funny dog">
        <p>
            <a href="/lab1/image">Русский</a> |
            <a href="/lab1/image/es">Español</a>
        </p>
    </body>
</html>
''', 200, {
        "Content-Language": "en",
        "X-Image-Page": "funny-dog-en",
        "X-Framework": "Flask"
    }


@lab1.route("/lab1/image/es")
def image_es():
    path = url_for("static", filename="funny_dog.jpg")
    style = url_for("static", filename="lab1.css")

    return '''
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="''' + style + '''">
        <title>Perro divertido</title>
    </head>
    <body>
        <h1>Perro divertido</h1>
        <img src="''' + path + '''" alt="Perro divertido">
        <p>
            <a href="/lab1/image">Русский</a> |
            <a href="/lab1/image/en">English</a>
        </p>
    </body>
</html>
''', 200, {
        "Content-Language": "es",
        "X-Image-Page": "funny-dog-es",
        "X-Framework": "Flask"
    }

count = 0
@lab1.route('/lab1/counter')
def counter():
    global count
    count+=1
    time = datetime.datetime.today
    url = request.url
    client_ip = request.remote_addr
    return '''
<!doctype html>
<html>
    <body>
        Сколько раз сюда заходили: '''+ str(count) + '''
        <hr>
        Дата и время: ''' + str(time) + '''<br>
        Запрошенный адрес: ''' + str(url) + '''<br>
        Ваш IP-адрес: ''' + str(client_ip) + '''<br>
        <a href="/lab1/counter/reset">Сбросить счётчик</a>
    </body>
</html>'''


@lab1.route('/lab1/info')
def info():
    return redirect('/lab1/author')


@lab1.route('/lab1/created')
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано...</i></div>
    </body>
</html>
''', 201


@lab1.route('/lab1/counter/reset')
def reset_counter():
    global count
    count = 0
    return '''
<!doctype html>
<html>
    <body>
        <p>счётчик был сброшен</p>
        <a href="/lab1/counter">назад к счётчику</a>
    </body>
</html>
'''


@lab1.route("/lab1/error/400")
def error_400():
    return "неверный запрос", 400


@lab1.route("/lab1/error/401")
def error_401():
    return "требуется авторизация", 401


@lab1.route("/lab1/error/402")
def error_402():
    return "требуется оплата", 402


@lab1.route("/lab1/error/403")
def error_403():
    return "доступ запрещён", 403


@lab1.route("/lab1/error/405")
def error_405():
    return "метод не разрешён", 405


@lab1.route("/lab1/error/418")
def error_418():
    return "я чайник", 418


# Роут, который вызывает ошибку
@lab1.route("/lab1/cause_error")
def cause_error():
    # Пример: деление на ноль
    x = 1 / 0
    return str(x)