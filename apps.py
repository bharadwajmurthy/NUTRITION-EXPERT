from flask import Flask,render_template,request,redirect,url_for
import sqlite3 as sql
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('mainwta.jinja2')
	
@app.route('/bmi/')
def bmi():
    return render_template('bmical.jinja2')
	
@app.route('/weights/')
def weight():
    return render_template('rooms.jinja2')

@app.route('/weights/add/' ,methods =['GET','POST'])
def addweight():
    if request.method == 'POST':
        c_id=request.form['c_id']
        c_date = request.form['c_date']
        c_weight = request.form['c_weight']
        c_age =   request.form['c_age']
        c_bmi = request.form['c_bmi']
        c_height = request.form['c_height']
        if c_date.strip() is "" and c_bmi.strip() is "" and c_weight.strip() is "":
            return render_template('addemp.jinja2', error="Enter all fields properly")
        else:
            try:
                with sql.connect("sqldb.db") as con:
                    cur = con.cursor()
                    cur.execute("create table if not exists weight (c_id INT primary key, c_date TEXT , c_weight TEXT , c_age TEXT , c_bmi INT ,c_height TEXT)")
                    cur.execute("INSERT INTO weight (c_id,c_date,c_weight,c_age,c_bmi,c_height) VALUES (?,?,?,?,?,?)", (c_id,c_date,c_weight,c_age,c_bmi,c_height))
                    con.commit()
                    msg = "Record saved successfully"
            except:
                con.rollback()
                msg = "Error in inserting record"
            finally:
                con.close()
                return render_template("addemp.jinja2", msg=msg)
    return render_template('addemp.jinja2')

@app.route('/weights/list/')
def lstemp():
    with sql.connect("sqldb.db") as con:
        cur = con.cursor()
        cur.execute("select * from weight")
        emplist = cur.fetchall()
    return render_template('mgemp.jinja2',emplist=emplist)

@app.route('/weights/delete/' , methods=['GET','POST'])
def deleteemp():
    if request.method == 'POST':
        c_id=request.form['delbutton']
        print("this is the empid",int(c_id))
        try:
            with sql.connect("sqldb.db") as con:
                cur = con.cursor()
                print("connection established\n\n\n\n")
                cur.execute("delete from weight where c_id=%d"%int(c_id))
                print("sql function worked\n\n\n\n")
                con.commit()
                print("IT IS  commiting\n\n\n")
                con.close()
                print("successfully closed \n\n\n")
                return render_template("deleteemp.jinja2")
        except:
            return render_template("deleteemp.jinja2")
    else :
        return render_template("deleteemp.jinja2")

@app.route('/nutrition/')
def nutrition():
    return render_template('lstemp.jinja2')

@app.route('/nutrition/add/' ,methods =['GET','POST'])
def addfood():
    if request.method == 'POST':
        id=request.form['c_id']
        qty = request.form['c_date']
        chol = request.form['c_weight']
        sugar =   request.form['c_age']
        fat = request.form['c_bmi']
        vit = request.form['c_height']
        if id.strip() is "" and qty.strip() is "" and chol.strip() is "":
            return render_template('addemp1.jinja2', error="Enter all fields properly")
        else:
            try:
                with sql.connect("sqldb.db") as con:
                    cur = con.cursor()
                    cur.execute("create table if not exists nutrition (id INT primary key, qty TEXT , chol TEXT , sugar TEXT , fat TEXT ,vit TEXT)")
                    cur.execute("INSERT INTO nutrition (id,qty,chol,sugar,fat,vit) VALUES (?,?,?,?,?,?)", (id,qty,chol,sugar,fat,vit))
                    con.commit()
                    msg = "Record saved successfully"
            except:
                con.rollback()
                msg = "Error in inserting record"
            finally:
                con.close()
                return render_template("addemp1.jinja2", msg=msg)
    return render_template('addemp1.jinja2')

@app.route('/nutrition/list/')
def lstfood():
    with sql.connect("sqldb.db") as con:
        cur = con.cursor()
        cur.execute("select * from nutrition")
        emplist = cur.fetchall()
    return render_template('mgemp1.jinja2',emplist=emplist)

@app.route('/nutrition/delete/' , methods=['GET','POST'])
def deletefood():
    if request.method == 'POST':
        c_id=request.form['delbutton']
        print("this is the empid",int(c_id))
        try:
            with sql.connect("sqldb.db") as con:
                cur = con.cursor()
                print("connection established\n\n\n\n")
                cur.execute("delete from nutrition where id=%d"%int(c_id))
                print("sql function worked\n\n\n\n")
                con.commit()
                print("IT IS  commiting\n\n\n")
                con.close()
                print("successfully closed \n\n\n")
                return render_template("deleteemp1.jinja2")
        except:
            return render_template("deleteemp1.jinja2")
    else :
        return render_template("deleteemp1.jinja2")

@app.route('/celebrity/taylorswift/')
def celebtaylor():
    return render_template('slide1.html')

@app.route('/celebrity/shawn/')
def celebshawn():
    return render_template('slide2.html')



app.run(debug=True)
