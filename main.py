from flask import Flask, render_template, url_for
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def main():
    db_session.global_init("db//mars_explorer.db")

    db_sess = db_session.create_session()
    actions = db_sess.query(Jobs).all()
    url = url_for('static', filename='css/style.css')
    return render_template("works_log.html", actions=actions, url=url)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
