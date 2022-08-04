from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
  "apiKey": "AIzaSyASx2vWHHg418m4HX4eKbxOrIqC75zACo8",
  "authDomain": "meet---2022.firebaseapp.com",
  "projectId": "meet---2022",
  "storageBucket": "meet---2022.appspot.com",
  "messagingSenderId": "115400578724",
  "appId": "1:115400578724:web:a8565930f311175a6db831",
  "measurementId": "G-G009ZDNMKG",
  "databaseURL": "https://meet---2022-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#routes

cart = []

@app.route('/', methods = ['GET' , 'POST'])
def home():
  if request.method == 'POST':
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]
    info = {"name" : name , "email" : email , "phone" : phone , "message" : message}
    db.child("Message").push(info)
    return render_template("index.html")
  
  else:
    return render_template("index.html")

@app.route('/snow', methods = ["GET" , "POST"])
def snow():
  if request.method == 'POST':
    try:
      snow = {"Snow" : "Snow"}
      db.child("Users").child("Users").child("username").update(snow)   
      return render_template("index.html")
    except:
      return render_template("signup.html")

  else:
    return render_template("index.html")

@app.route('/grass', methods = ["GET" , "POST"])
def grass():
  if request.method == 'POST':
    try:
      grass = {"Grass" : "Grass"}
      db.child("Users").child("Users").child("username").update(grass) 
      return render_template("index.html")
    except:
      return render_template("signup.html")

  else:
    return render_template("index.html")

@app.route('/cocoa', methods = ["GET" , "POST"])
def cocoa():
  if request.method == 'POST':
    try:
      cocoa = {"Cocoa" : "Cocoa"}
      db.child("Users").child("Users").child("username").update(cocoa) 
      return render_template("index.html")
    except:
      return render_template("signup.html")

  else:
    return render_template("index.html")

@app.route('/mushroom', methods = ["GET" , "POST"])
def mushroom():
  if request.method == 'POST':
    try:
      mush = {"Mushroom" : "Mushroom"}
      db.child("Users").child("Users").child("username").update(mush) 
      return render_template("index.html")
    except:
      return render_template("signup.html")

  else:
    return render_template("index.html")

@app.route('/tree', methods = ["GET" , "POST"])
def tree():
  if request.method == 'POST':
    try:
      tree = {"Tree" : "Tree"}
      db.child("Users").child("Users").child("username").update(tree) 
      return render_template("index.html")
    except:
      return render_template("singup.html")
  else:
    return render_template("index.html")

@app.route('/crystal', methods = ["GET" , "POST"])
def crystal():
  if request.method == 'POST':
    try:
      crystal = {"Crystal" : "Crystal"}
      db.child("Users").child("Users").child("username").update(crystal) 
      return render_template("index.html")
    except:
      return render_template("signup.html")
  else:
    return render_template("index.html")


@app.route('/signup', methods = ["GET" , "POST"])
def signup():
  if request.method == 'POST':
    name = request.form["name"]    
    email = request.form["email"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 == password2:
      users = {name : ""}
      username = {"Username" : users}
      login_session['user'] = auth.create_user_with_email_and_password(email, password1)
      db.child("Users").push(username)
      return redirect(url_for('home'))

      #except:
        #return render_template("signup.html")

    else:
      return render_template("signup.html")

  else:
    return render_template("signup.html")

@app.route('/signin', methods = ["GET" , "POST"])
def signin():
  if request.method == 'POST':
    emails = request.form["email-in"]
    passwords = request.form["password-in"]
    try:
      login_session['user'] = auth.sign_in_with_email_and_password(emails, passwords)
      return redirect(url_for('home'))

    except:
      return render_template("signin.html")

  else:
    return render_template("signin.html")


@app.route('/shop', methods = ["GET" , "POST"])
def shop():
  try:
    cart = db.child("Users").child("Users").child("username").get().val()
    print(cart)
    return render_template("shop.html", cart= cart)
  except:
    return render_template("index.html")



#routes

if __name__ == '__main__':
    app.run(debug=True)