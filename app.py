from flask import Flask, redirect, url_for, request,created
import datetime
app = Flask(__name__) 

@app.route('/')
@app.route('/web')
def web():
    return """<!doctype  html>
        <html>
            <body> 
                <h1>web-сервер на flask</h1>
                <a href="/author">author</a>
            </body> 
        </html>"""

@app.route("/author")
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
            </body>
        </html>"""

@app.route("/image")
def image():
    path = url_for("static", filename = "funny_dog.jpg")
    return '''<!doctype html>
    <html>
        <body>
            <h1>Смешной пес<h1>
            <img src="''' + path +'''">
        </body>
    </html>'''

count = 0
@app.route('/counter')
def counter():
    global count
    count += 1
    time = str(datetime.datetime.today())
    url = request.url
    client_ip = request.remote_addr
    return '''
<!doctype html>
<html>
    <body>
       Сколько раз вы сюда заходили: ''' + str(count) + '''<br>
       <hr>
       Дата и время: ''' + time + '''<br>
       Запрошенный адрес: ''' + url + '''<br>
       Ваш IP-адрес: ''' + client_ip + '''<br> 
       <hr>
    </body>
</html>
'''

@app.route('/info')
def info():
    return redirect("/author")

@lab1.route("/created")
def created():
    return '''
<!doctype html>
<html>
    <body>
       <h1> Создано успешно </h1>
       <div><i>что-то создано...</i></div>
    </body>
</html>
''', 201
