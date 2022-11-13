from asyncio.windows_events import NULL
from contextlib import nullcontext
from importlib.abc import TraversableResources
import hashlib
from pickle import GET, TRUE
from types import NoneType
from unicodedata import name
from flask import Blueprint, Flask,flash, get_flashed_messages, render_template, g, request, redirect, url_for, session, render_template_string
import sqlite3


# from flask_login import user_logged_in
# # from matplotlib.pyplot import title


# Path to database.
DATABASE = "theplantbox.db"

app=Flask(__name__)
app.secret_key = "hjhsbhibcsa"


 



 
#used to connect to the database in querying functions 
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# def sql_select(selected,table,col,variable):
#     cursor = get_db().cursor()
#     sql = " SELECT " + selected +" FROM "+table+ " WHERE "+col+" = ?"
#     cursor.execute(sql,(variable,))

# function used to close the connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)





@app.get("/")
def index():
    flash("testing testicles")
    flash('Invalid password provided', 'error')
    return render_template("index.html",session=session)


#route for login page
@app.route("/login",methods=['GET','POST'])
def login():
    incorrect_creds = False
    #If the user is submitting data 
    if request.method == 'POST':
        db=get_db()
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        user_email = request.form['email_address']
        user_password = request.form['password']
        #slq selects the user id from a user when the email and passwords are the same
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
    return render_template('login.html', incorrect_creds=incorrect_creds,session=session,)



@app.route("/signup", methods=['GET','POST'])
def signup():
    #if the user is submitting data then
    if request.method == 'POST':
        #saves form data to easier variables
        user_email = request.form['email_address']
        user_password = request.form['password']
        db=get_db()
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        #If the passwords are the same then add the new user profile 
        if request.form['password'] == request.form['password_confirm']:
            session['password'] = request.form['password']
            user_name = '{}'.format(request.form['name_form'])
            user_password = '{}'.format(request.form['password'])
            user_email = '{}'.format(request.form['email_address'])
            db=get_db()
            db.row_factory = sqlite3.Row
            cursor = db.cursor()
            sql = "INSERT INTO user(name, password, email) VALUES(?,?,?)"
            # creates a user with the selected information from the sign up form
            cursor.execute(sql,(user_name, user_password, user_email))
            print(sql,(user_name, user_password, user_email))
            get_db().commit()
            sql = " "
            cursor.execute(sql,(user_email,user_password,))
            result = cursor.fetchall()
            try:
                session['id'] = result[0]['id']
                print("cursor executed")
            except:
                print("No session ID")
            else:
                return redirect(url_for('login'))
        else:
            # because the sign up information wasnt correct it clears the logged in session for the user 
            session.clear()
            return redirect(url_for("signup"))
    return render_template("sign-up.html",session=session,request=request,)


#clears the log in session
@app.route("/logout")
def logout():
    session.clear()
    logged_in = False
    return redirect(url_for('index'))

    

@app.get("/portfolio")
def portfolio():
    try:
        if session['id']:
            logged_in= True
    except:
        logged_in = False
    #if the user is logged in show them their plants 
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
        #Sql shows the plant types as well as the plant tables 
        sql = " SELECT plant.ID, plant.name as nickname, plant_type.name as plant_name, plant_type.slug FROM plant LEFT JOIN plant_type ON plant.plant_type = plant_type.ID;"
    else:
        sql = " SELECT plant.ID, plant.name as nickname, plant_type.name as plant_name, plant_type.slug FROM plant LEFT JOIN plant_type ON plant.plant_type = plant_type.ID;"
   
    cursor.execute(sql)
    plants = cursor.fetchall()
    sql = " SELECT ID,name FROM plant_type "
    cursor.execute(sql)
    plant_type_list = cursor.fetchall()
    print(plant_type_list)

    return render_template("user-portfolio.html", plants=plants, plant_type_list=plant_type_list,logged_in = logged_in,session=session,)


@app.get("/contact")
def contact_page():
    return render_template("contact.html",session=session,)


@app.get("/about")
def about_us():
    return render_template("about.html",session=session,)
 






# adding a slug to the url of each page for plant tables
@app.get("/page/<slug>")
def page(slug):
    print (slug)
    # retrieving relevant informtaion for each page 
    cursor = get_db().cursor()
    sql = " SELECT name FROM plant_type WHERE slug = ?"
    cursor.execute(sql,(slug,))
    plant_name = cursor.fetchone()
    # retrieving relevant informtaion for each page 

    sql = " SELECT content FROM plant_type WHERE slug = ?"
    cursor.execute(sql,(slug,))
    content = cursor.fetchone()
        # retrieving relevant informtaion for each page 

    sql = "SELECT title FROM plant_type WHERE slug = ?"
    cursor.execute(sql,(slug,))
    title = cursor.fetchone()
    # retrieving relevant informtaion for each page 
    sql = "SELECT slug FROM plant_type"
    cursor.execute(sql)
    sql = "SELECT image_location FROM plant_type WHERE slug  = ?;"
    cursor.execute(sql,(slug,))
    return render_template("plant_info.html",content=content,slug=slug,title=title,plant_name=plant_name,)




@app.post('/')
def index_post():
    cursor = get_db().cursor()
    name = request.form['name']
    planted_date = request.form['planted_date']
    if request.form['plants'] == "":
        return redirect(url_for("home"))
    plant = request.form['plants']
    # adds plants into the database with info from the form fields 
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



# when an error 404 happens it redirects to this page
@app.errorhandler(404)
def error_404(error):
    return render_template('error404.html',error=error), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8008,debug=True)
