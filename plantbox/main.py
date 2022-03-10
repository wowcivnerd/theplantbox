from importlib.abc import TraversableResources
from flask import Flask, render_template, g, request, redirect, url_for
import sqlite3


DATABASE = "theplantbox.db"

app=Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)


@app.get("/")
def index():
    cursor = get_db().cursor()
    sql = " SELECT name FROM plant"
    cursor.execute(sql)
    feedback = cursor.fetchall
    return render_template("index.html", feedback=feedback) 
    # change feedback to name that makes more sense depending on sql command seen above 
 
@app.post('/')
def index_post():
    cursor = get_db().cursor()
    username = request.form['name_of_planter']
    plant_name = request.form['plant_name']
    planted_date = request.form['date_planted']
    sql = " INSERT INTO plant(name, planted_date) VALUES(?.?)"
    cursor.execute(sql,(plant_name,planted_date))
    get_db().commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8008,debug=True)