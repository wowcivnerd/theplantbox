from asyncio.windows_events import NULL
from contextlib import nullcontext
from importlib.abc import TraversableResources
import hashlib
from pickle import GET, TRUE
from types import NoneType
from unicodedata import name
from flask import Blueprint, Flask, render_template, g, request, redirect, url_for, session, render_template_string
import sqlite3
from werkzeug.security import check_password_hash
#https://techmonger.github.io/4/secure-passwords-werkzeug/  NEED TO HASH ALL PASSWORDS


from flask_login import user_logged_in
# from matplotlib.pyplot import title


check_password_hash('sha256$lTsEjTVv$c794661e2c734903267fbc39205e53eca607f9ca2f85812c95020fe8afb3bc62',"P1ain-text-user-passw@rd")

# Path to database.
DATABASE = "theplantbox.db"

app=Flask(__name__)
app.secret_key = "boobs"






 

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
    return render_template("index.html")

@app.route("/login",methods=['GET','POST'])
def signin():
    incorrect_creds = False
    if request.method == 'POST':
        db=get_db()
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        user_email = request.form['email_address']
        user_password = request.form['password']
        sql = " SELECT id FROM user WHERE email = ? AND password = ?"
        cursor.execute(sql,(user_email,user_password))
        result = cursor.fetchone()
        try:
            session['id'] = result[0]
            print("Session ID:")
            print (session['id'])
        except:
            incorrect_creds = True
        else:
            return redirect(url_for('portfolio'))
    return render_template('login.html', incorrect_creds=incorrect_creds)

@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        #saves form data
        user_email = request.form['email_address']
        user_password = request.form['password']
        sql = "SELECT * FROM "
        db=get_db()
        db.row_factory = sqlite3.Row
        cursor = db.cursor()

        if request.form['password'] == request.form['password_confirm']:
            session['password'] = request.form['password']
            user_name = '{}'.format(request.form['name_form'])
            user_password = '{}'.format(request.form['password'])
            user_email = '{}'.format(request.form['email_address'])
            db=get_db()
            db.row_factory = sqlite3.Row
            cursor = db.cursor()
            sql = "INSERT INTO user(name, password, email) VALUES(?,?,?)"
            print(user_name,user_password,user_email)
            cursor.execute(sql,(user_name, user_password, user_email))
            print(sql,(user_name, user_password, user_email))
            get_db().commit()
            sql = " SELECT id FROM user WHERE email = ? AND password = ?"
            cursor.execute(sql,(user_email,user_password,))
            result = cursor.fetchall()
            try:
                session['id'] = result[0]
                print("cursor executed")
            except:
                print("No session ID")
            else:
                return redirect(url_for('index'))
        else:
            session.pop('email', default=None)
            session.pop('name', default=None)
            session.pop('password', default=None)
            return redirect(url_for("signup"))
    return render_template("sign-up.html")



@app.get("/portfolio")
def portfolio():
    try:
        if session['id']:
            logged_in= True
    except:
        logged_in = False

    if logged_in:
        print("session id reccognised")
        id = session['id']
        db = get_db()
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        sql = " SELECT name FROM user WHERE id = ?"
        cursor.execute(sql,(id,))
        result = cursor.fetchone()
        session['name'] = result[0]
        print(sql, id)
    else: 
        print("else statement")

    db = get_db()
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    if logged_in:
        print("do be truin")
        sql = " SELECT plant.ID, plant.name as nickname, plant_type.name as plant_name, plant_type.slug FROM plant LEFT JOIN plant_type ON plant.plant_type = plant_type.ID;"
    else:
        print("not signed in ")
        sql = " SELECT plant.ID, plant.name as nickname, plant_type.name as plant_name, plant_type.slug FROM plant LEFT JOIN plant_type ON plant.plant_type = plant_type.ID;"
   
    cursor.execute(sql)
    plants = cursor.fetchall()
    sql = " SELECT ID,name FROM plant_type "
    cursor.execute(sql)
    plant_type_list = cursor.fetchall()
    print(plant_type_list)

    return render_template("user-portfolio.html", plants=plants, plant_type_list=plant_type_list,logged_in = logged_in, ) 



@app.get("/contact")
def contact_page():
    return render_template("contact.html")


@app.get("/about")
def about_us():
    return render_template("about.html")
 






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


    # slug_link = "/page" + slug
    # # if slug != 
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
