from flask import Flask, url_for, request, redirect, abort, render_template
from lab1 import lab1
import datetime
app = Flask(__name__)
app.register_blueprint(lab1)

# список логов
access_log = []


@app.errorhandler(404)
def not_found(err):
    path = url_for("static", filename="404.jpg")
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
            <a href="/lab2">Вторая лабораторная</a>
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


@app.route('/lab2/a')
def a():
    return 'без слэша'


@app.route('/lab2/a/')
def a2():
    return 'со слэшем'


flower_list = ["Роза", "Пион", "Хризантема", "Альстромерия", "Гортензия"]
flowers = [
    {"name": "Роза", "price": 300},
    {"name": "Пион", "price": 310},
    {"name": "Хризантема", "price": 320},
    {"name": "Альстромерия", "price": 330},
    {"name": "Гортензия", "price": 300},
]

@app.route('/lab2/all_flowers/<int:flower_id>')
def id_flowers(flower_id):
    if flower_id >= len(flowers):
        abort(404)
    else:
        flower = list(flowers[flower_id].values())[0]
        return f'''
<!doctype html>
<html>
    <body>
        <h1>Вы выбрали цветы</h1>
        <p>Букет из: <b>{flower}</b></p>
        <a href="/lab2/all_flowers">Посмотреть все цветы</a>
    </body>
</html>
'''

    
@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flowers.append({"name": name, "price": 300})
    return redirect(url_for("all_flowers"))


@app.route('/lab2/add_flower/')
def add_flower_no_name():
    return "Вы не задали имя цветка", 400


@app.route('/lab2/all_flowers')
def all_flowers():
    return render_template("flowers.html", flowers=flowers)


@app.route("/lab2/del_flower/<int:flower_id>")
def del_flower(flower_id):
    if 0 <= flower_id < len(flowers):
        flowers.pop(flower_id)
        return redirect(url_for("all_flowers"))
    else:
        abort(404)


@app.route('/lab2/del_flower/')
def del_flower_no_name():
    return "Вы не задали имя цветка", 400


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
    flowers.clear()
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

f1_drivers = [
    {"name": "Ландо Норрис", "desc": "Британский гонщик McLaren, чемпион мира Формулы-1 2025 года.", "image": "nor.jpg"},
    {"name": "Оскар Пиастри", "desc": "Австралийский гонщик McLaren, один из сильнейших молодых пилотов чемпионата.", "image": "pia.jpg"},
    {"name": "Джордж Расселл", "desc": "Британский гонщик Mercedes, победитель Гран-при и один из лидеров команды.", "image": "rus.jpg"},
    {"name": "Кими Антонелли", "desc": "Итальянский гонщик Mercedes, молодой талант, дебютировавший в Формуле-1 в 2025 году.", "image": "ant.jpg"},
    {"name": "Макс Ферстаппен", "desc": "Нидерландский гонщик Red Bull, четырёхкратный чемпион мира Формулы-1.", "image": "ver.jpg"},
    {"name": "Айзек Хаджар", "desc": "Французский гонщик Red Bull, дебютировавший в Формуле-1 в 2025 году.", "image": "had.jpg"},
    {"name": "Шарль Леклер", "desc": "Монегасский гонщик Ferrari, известный скоростью на квалификационных кругах.", "image": "lec.jpg"},
    {"name": "Льюис Хэмилтон", "desc": "Британский гонщик Ferrari, семикратный чемпион мира Формулы-1.", "image": "ham.jpg"},
    {"name": "Алекс Албон", "desc": "Тайско-британский гонщик Williams, регулярно борющийся за очки.", "image": "alb.jpg"},
    {"name": "Карлос Сайнс", "desc": "Испанский гонщик Williams, победитель нескольких Гран-при Формулы-1.", "image": "sai.jpg"},
    {"name": "Арвид Линдблад", "desc": "Британский гонщик Racing Bulls, дебютант сезона Формулы-1 2026 года.", "image": "lin.jpg"},
    {"name": "Лиам Лоусон", "desc": "Новозеландский гонщик Racing Bulls, выступающий в чемпионате мира Формулы-1.", "image": "law.jpg"},
    {"name": "Лэнс Стролл", "desc": "Канадский гонщик Aston Martin, выступающий в Формуле-1 с 2017 года.", "image": "str.jpg"},
    {"name": "Фернандо Алонсо", "desc": "Испанский гонщик Aston Martin, двукратный чемпион мира Формулы-1.", "image": "alo.jpg"},
    {"name": "Эстебан Окон", "desc": "Французский гонщик Haas, победитель Гран-при Венгрии 2021 года.", "image": "oco.jpg"},
    {"name": "Оливер Берман", "desc": "Британский гонщик Haas, молодой пилот, дебютировавший в Формуле-1 в 2024 году.", "image": "ber.jpg"},
    {"name": "Нико Хюлькенберг", "desc": "Немецкий гонщик Audi, опытный пилот с многолетней карьерой в Формуле-1.", "image": "hul.jpg"},
    {"name": "Габриэль Бортолето", "desc": "Бразильский гонщик Audi, чемпион Формулы-2 2024 года.", "image": "bor.jpg"},
    {"name": "Пьер Гасли", "desc": "Французский гонщик Alpine, победитель Гран-при Италии 2020 года.", "image": "gas.jpg"},
    {"name": "Франко Колапинто","desc": "Аргентинский гонщик Alpine, дебютировавший в Формуле-1 в 2024 году.", "image": "col.jpg"},
    {"name": "Серхио Перес", "desc": "Мексиканский гонщик Cadillac, победитель нескольких Гран-при Формулы-1.", "image": "per.jpg"},
    {"name": "Валттери Боттас", "desc": "Финский гонщик Cadillac, победитель десяти Гран-при Формулы-1.", "image": "bot.jpg"},
]


@app.route('/lab2/drivers')
def drivers():
    return render_template("drivers.html", drivers=f1_drivers)

if __name__ == '__main__':
    app.run(debug=True)
