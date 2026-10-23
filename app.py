from flask import Flask, url_for, request, redirect, abort, render_template
import datetime

app = Flask(__name__)


@app.errorhandler(404)
def not_found(err):
    path = url_for("static", filename="404.jpg")

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
            <a href="/lab1">Первая лабораторная</a>
        </nav>

        <footer>
            Размахнина Маргарита Михайловна, ФБИ-44, 3 курс, 2026
        </footer>
    </body>
</html>
'''


@app.route("/lab1")
def lab1():
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
                background: #F8D7DA;
                color: #68434A;
                line-height: 1.6;
            }

            a {
                color: #388E50;
                font-weight: bold;
                text-decoration: none;
            }

            a:hover {
                color: #205C32;
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <p>
            «Чтоб жить честно, надо рваться, путаться, биться,
            ошибаться, начинать и бросать, и опять начинать,
            и опять бросать, и вечно бороться и лишаться.
            А спокойствие – душевная подлость».
        </p>

        <p><a href="/">На главную</a></p>

        <h2>Меню</h2>
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


@app.route("/lab1/web")
def web():
    return '''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Flask</title>
    </head>
    <body>
        <h1>web-сервер на flask</h1>
        <a href="/lab1/author">author</a>
    </body>
</html>
''', 200, {
        "X-Server": "sample",
        "Content-Type": "text/html; charset=utf-8"
    }


@app.route("/lab1/author")
def author():
    name = "Размахнина Маргарита Михайловна"
    group = "ФБИ-44"
    faculty = "ФБ"

    return '''<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Автор</title>
    </head>
    <body>
        <p>Студент: ''' + name + '''</p>
        <p>Группа: ''' + group + '''</p>
        <p>Факультет: ''' + faculty + '''</p>
        <a href="/lab1/web">web</a>
    </body>
</html>
''', 200, {
        "Content-Language": "ru",
        "X-Author": "Razmachnina M.M.",
        "X-Framework": "Flask"
    }


@app.route("/lab1/image")
def image():
    path = url_for("static", filename="funny_dog.jpg")
    style = url_for("static", filename="lab1.css")

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


@app.route("/lab1/image/en")
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


@app.route("/lab1/image/es")
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


@app.route("/lab1/counter")
def counter():
    global count
    count += 1

    time = datetime.datetime.now()
    url = request.url
    client_ip = request.remote_addr

    return '''
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Счётчик посещений</title>
    </head>
    <body>
        Сколько раз сюда заходили: ''' + str(count) + '''
        <hr>
        Дата и время: ''' + str(time) + '''<br>
        Запрошенный адрес: ''' + str(url) + '''<br>
        Ваш IP-адрес: ''' + str(client_ip) + '''<br>
        <a href="/lab1/counter/reset">Сбросить счётчик</a>
    </body>
</html>
'''


@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")


@app.route("/lab1/created")
def created():
    return '''
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Создано</title>
    </head>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано...</i></div>
    </body>
</html>
''', 201


@app.route("/lab1/counter/reset")
def reset_counter():
    global count
    count = 0

    return '''
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Сброс счётчика</title>
    </head>
    <body>
        <p>счётчик был сброшен</p>
        <a href="/lab1/counter">назад к счётчику</a>
    </body>
</html>
'''


@app.route("/lab1/error/400")
def error_400():
    return "неверный запрос", 400


@app.route("/lab1/error/401")
def error_401():
    return "требуется авторизация", 401


@app.route("/lab1/error/402")
def error_402():
    return "требуется оплата", 402


@app.route("/lab1/error/403")
def error_403():
    return "доступ запрещён", 403


@app.route("/lab1/error/405")
def error_405():
    return "метод не разрешён", 405


@app.route("/lab1/error/418")
def error_418():
    return "я чайник", 418


@app.route("/lab1/cause_error")
def cause_error():
    # Пример ошибки сервера: деление на ноль
    x = 1 / 0
    return str(x)


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

@app.route('/lab2/a')
def a():
    return 'без слэша'

@app.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = ["Роза", "Пион", "Хризантема", "Альстромерия", "Гортензия"]

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        abort(404)
    else:
        flower = flower_list[flower_id]
        return f'''
<!doctype html>
<html>
    <body>
        <h1>Вы выбрали цветы</h1>
        <p>Пивной букет из: <b>{flower}</b></p>
        <a href="/lab2/all_flowers">Посмотреть все цветы</a>
    </body>
</html>
'''
@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name}</p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </body>
</html>'''

@app.route('/lab2/add_flower/')
def add_flower_no_name():
    return "Вы не задали имя цветка", 400

@app.route('/lab2/all_flowers')
def all_flowers():
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Список цветов</h1>
        <p>Всего цветов: {len(flower_list)}</p>
        <ul>
            {''.join(f"<li>{flower}</li>" for i, flower in enumerate(flower_list))}
        </ul>
        <a href="/lab2">Назад к лабораторной 2</a>
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    name = 'Размахнина Маргарита'
    number = 2
    group = 'ФБИ-44'
    course = 3

    fruits = [
            {'name':'яблоки', 'price': 100},
            {'name':'груши', 'price': 120},
            {'name':'апельсины', 'price': 80},
            {'name':'мандарины', 'price': 95},
            {'name':'манго', 'price': 321},
        ]
    return render_template('example.html',
                           name=name,
                           number=number,
                           group=group,
                           course=course,
                           fruits=fruits)

@app.route('/lab2')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return '''
<!doctype html>
<html>
    <body>
        <h1>Список очищен</h1>
        <p>Все цветы удалены.</p>
        <a href="/lab2/all_flowers">Посмотреть все цветы</a>
    </body>
</html>
'''
@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    result = f"""
<!doctype html>
<html>
    <body>
        <h1>Калькулятор</h1>
        <p>{a} + {b} = {a + b}</p>
        <p>{a} - {b} = {a - b}</p>
        <p>{a} * {b} = {a * b}</p>
        <p>{a} / {b} = {"нельзя делить на 0" if b == 0 else a / b}</p>
        <p>{a} ** {b} = {a ** b}</p>
        <hr>
        <a href="/lab2">Назад к лабораторной 2</a>
    </body>
</html>
"""
    return result

@app.route('/lab2/calc/')
def calc_default():
    return redirect('/lab2/calc/1/1')

@app.route('/lab2/calc/<int:a>')
def calc_one_arg(a):
    return redirect(f'/lab2/calc/{a}/1')

books = [
    {"author": "Фёдор Достоевский", "title": "Преступление и наказание", "genre": "Роман", "pages": 672},
    {"author": "Лев Толстой", "title": "Война и мир", "genre": "Исторический роман", "pages": 1225},
    {"author": "Александр Пушкин", "title": "Евгений Онегин", "genre": "Роман в стихах", "pages": 384},
    {"author": "Михаил Булгаков", "title": "Мастер и Маргарита", "genre": "Роман", "pages": 480},
    {"author": "Иван Тургенев", "title": "Отцы и дети", "genre": "Роман", "pages": 320},
    {"author": "Антон Чехов", "title": "Вишнёвый сад", "genre": "Пьеса", "pages": 120},
    {"author": "Николай Гоголь", "title": "Мёртвые души", "genre": "Роман", "pages": 432},
    {"author": "Владимир Набоков", "title": "Лолита", "genre": "Роман", "pages": 368},
    {"author": "Рэй Брэдбери", "title": "451° по Фаренгейту", "genre": "Фантастика", "pages": 249},
    {"author": "Джордж Оруэлл", "title": "1984", "genre": "Антиутопия", "pages": 328}
]

@app.route('/lab2/books')
def show_books():
    return render_template('books.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
