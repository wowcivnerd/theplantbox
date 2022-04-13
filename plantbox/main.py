from importlib.abc import TraversableResources
from flask import Flask, render_template, g, request, redirect, url_for
import sqlite3


# Path to database.
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
    sql = " SELECT ID,name,planted_date FROM plant"
    cursor.execute(sql)
    feedback = cursor.fetchall()
    return render_template("index.html", feedback=feedback) 

 

@app.get("/page/<slug>")
def page(slug):
    cursor = get_db().cursor()
    sql = " SELECT content FROM Plant_page WHERE Slug = ?"
    cursor.execute(sql,(slug,))
    content = cursor.fetchone()
    sql = "SELECT title FROM Plant_page WHERE Slug = ?"
    cursor.execute(sql,(slug,))
    header = cursor.fetchone()
    slug_link = "/page" + slug
    print (slug_link)
    return render_template("plant_info.html",content=content,slug=slug,slug_link=slug_link)
    # sql shite sql = "SELECT * FROM Page WHERE slug = (slug) VALUES(?,)"  and also feedback = feedback



@app.post('/')
def index_post():
    cursor = get_db().cursor()
    name = request.form['name']
    planted_date = request.form['planted_date']
    plant = request.form['plants']
    sql = " INSERT INTO plant(name, planted_date, plant_type) VALUES(?,?,?)"
    cursor.execute(sql,(name,planted_date,plant))
    get_db().commit()
    return redirect(url_for("index"))



@app.post('/delete')
def delete_item_by_ID():
    ID = request.form['ID']
    cursor = get_db().cursor()
    sql= "DELETE FROM Plant WHERE ID=?"
    cursor.execute(sql,(ID,))
    get_db().commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8008,debug=True)