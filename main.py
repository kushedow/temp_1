from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def page_index():
    return "Привет, все работает"


@app.route("/about/")
def page_about_me():
    return "Эта страничка про меня"


@app.route("/items/page_<int:page_nr>/")
def page_item(page_nr):
    return f"Вы просматриваете страницу {page_nr}"


@app.route("/path/from/<loc_from>/to/<loc_to>/")
def page_travel(loc_from, loc_to):
    return f"Вы отправляетесь из {loc_from} в {loc_to}"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
