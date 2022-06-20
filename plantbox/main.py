from contextlib import nullcontext
from importlib.abc import TraversableResources
import re
from flask import Blueprint, Flask, render_template, g, request, redirect, url_for
import sqlite3
# from matplotlib.pyplot import title


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
    active_link = 0
    return render_template("index.html",active_link = active_link)


@app.get("/signup")
def signup():
    return render_template("signup.html")


@app.get("/portfolio")
def portfolio():
    db = get_db()
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    sql = " SELECT plant.ID, plant.name as nickname, plant_type.name as plant_name, plant_type.slug FROM plant LEFT JOIN plant_type ON plant.plant_type = plant_type.ID;"
    cursor.execute(sql)
    plants = cursor.fetchall()
    sql = " SELECT ID,name FROM plant_type "
    cursor.execute(sql)
    plant_type_list = cursor.fetchall()
    return render_template("user-portfolio.html", plants=plants, plant_type_list=plant_type_list) 



@app.get("/contact")
def contact_page():
    return render_template("contact.html")


@app.get("/about")
def about_us():
    return render_template("about.html")
 


@app.get("/starting-out")
def starting_page():
    return render_template("index.html")



# doesnt work now because of lacking title colllumn in SQLite 
@app.get("/page/<slug>")
def page(slug):
    cursor = get_db().cursor()
    sql = " SELECT content FROM plant_type WHERE slug = ?"
    cursor.execute(sql,(slug,))
    content = cursor.fetchone()
    sql = "SELECT title FROM plant_type WHERE slug = ?"
    cursor.execute(sql,(slug,))
    title = cursor.fetchone()
    sql = "Select slug FROM plant_type"
    cursor.execute(sql)
    sql_slug_list = cursor.fetchall()
    slug_list = [""]

    for i in sql_slug_list:
        print (i)
        print(slug_list)

 #making it append(add) to the slug_list so I can compare sluglist and improper input to fix blackies comment on documentation


    slug_link = "/page" + slug
    # if slug != 
    return render_template("plant_info.html",content=content,slug=slug,title=title)
    # sql shite sql = "SELECT * FROM Page WHERE slug = (slug) VALUES(?,)"  and also feedback = feedback

@app.get("/page/None")
def pageNone():
    return render_template("no-plant.html")



@app.post('/')
def index_post():
    cursor = get_db().cursor()
    name = request.form['name']
    planted_date = request.form['planted_date']
    if request.form['plants'] == "":
        return redirect(url_for("home"))
    plant = request.form['plants']
    sql = " INSERT INTO plant(name, planted_date, plant_type) VALUES(?,?,?)"
    cursor.execute(sql,(name,planted_date,plant))
    get_db().commit()
    return redirect(url_for("portfolio"))



@app.post('/delete')
def delete_item_by_ID():
    ID = request.form['ID']
    cursor = get_db().cursor()
    sql= "DELETE FROM Plant WHERE ID=?"
    cursor.execute(sql,(ID,))
    get_db().commit()
    return redirect(url_for('portfolio'))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8008,debug=True)


