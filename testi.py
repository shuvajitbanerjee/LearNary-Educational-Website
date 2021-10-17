import cv2
import numpy as np
from flask import *

import mysql.connector

import os

app = Flask(__name__)
app.config['IMAGE_PATH']="static"
app.secret_key=os.urandom(24)
con=mysql.connector.connect(host='localhost',user='root',password='',database='chacking')
cursor=con.cursor()
non=mysql.connector.connect(host='localhost',user='root',password='',database='tech')
cur=non.cursor()


@app.route('/')
def hello_world():
    return render_template('index.html')



@app.route('/login')
def hello():
    return render_template('smple.html')
@app.route('/playvideo')
def ply():
    return render_template('playvideo.html')

@app.route('/register')
def regis():
    return render_template('smpler.html')
@app.route('/techers')
def tecg():
    return render_template('techer.html')

@app.route('/course')
def cours():
    return render_template('courses.html')
@app.route('/techupload')
def tup():
    return render_template('techersuplods.html')
@app.route('/suss')
def gg():
   return render_template('success.html')




@app.route('/login_valita' , methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')

    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'"""
                   .format(email,password))
    users=cursor.fetchall()
    if len(users)>0:
        return redirect('/course')
    else:
        return redirect('/register')



@app.route('/login_tech' , methods=['POST'])
def login_techer():
    email=request.form.get('yemail')
    password=request.form.get('ypassword')

    cur.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'"""
                   .format(email,password))
    user=cur.fetchall()
    if len(user)>0:
        return redirect('/techers')
    else:
        return redirect('/register')

@app.route('/add_user', methods=['POST'])
def usr():
    name=request.form.get('uname')
    email=request.form.get('uemail')
    password=request.form.get('upassword')
    cursor.execute("""INSERT INTO `users`(`user_id`,`name`,`email`,`password`) VALUES
        (NULL,'{}','{}','{}')""".format(name,email,password))
    con.commit()
    return render_template('smple.html')

@app.route('/add_tech', methods=['POST'])
def tech():
    name=request.form.get('xname')
    email=request.form.get('xemail')
    password=request.form.get('xpassword')
    cur.execute("""INSERT INTO `users`(`user_id`,`name`,`email`,`password`) VALUES
        (NULL,'{}','{}','{}')""".format(name,email,password))
    non.commit()
    return render_template('smple.html')
@app.route('/logout')
def logt():
    # session.pop('user_id')
    return redirect('/')

@app.route('/upload',methods=['GET','POST'])
def upload():
    video=request.files['myfile']
    video.save(os.path.join(app.config["IMAGE_PATH"],video.filename))
    return render_template('techersuplods.html',filename=video.filename)









if __name__=="__main__":
    app.run(debug=True)