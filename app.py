from flask import Flask, render_template, request, redirect, session
""" ----------------------firebase-------------------------------------- """
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("kunci.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
""" ----------------------------------------------------------------- """
"""-------------------------------- json data mahasiswa -----------------"""
""" import json

with open ('data_mahasiswa.json') as (f):
      data = json.load(f) """
data = []
#---------------------------global variabel-------------------------------
""" ------------------------------------------------------------------ """
""" ----------------------------fungsi---------------------------------- """
app = Flask(__name__)
app.secret_key = 'ewfjdefdesfj'
#ini halaman index

@app.route("/")
def index():
   
  dftr_mhs = []
  dokumen = db.collection('mahasiswa').stream()
  for doc in dokumen:
    mhs = doc.to_dict()
    mhs['id'] = doc.id
    dftr_mhs.append(mhs)

  return render_template("index.html",haloo=dftr_mhs)

@app.route("/detail/<uid>")
def detail(uid): 
  mahasiswa = db.collection('mahasiswa').document(uid).get().to_dict()
  return render_template("detail.html",mahasiswa=mahasiswa) 


@app.route("/add",methods=['POST','GET'])
def add_data():
  nama = request.form.get("nama")
  nilai = request.form.get("nilai")
  alamat = request.form.get("alamat")
  email = request.form.get("email")
  no = request.form.get("no")
  foto = request.form.get("foto")

  oii = {
    'alamat': alamat,
    'email': email,
    'foto': foto,
    'nama': nama,
    'nilai':int(nilai),
    'no_hp':no
  }
  db.collection('mahasiswa').document().set(oii)
  dftr_mhs = []
  dokumen = db.collection('mahasiswa').stream()
  for doc in dokumen:
    mhs = doc.to_dict()
    mhs['id'] = doc.id
    dftr_mhs.append(mhs)

  return render_template("index.html",haloo=dftr_mhs)

@app.route("/update/<uid>")
def update(uid): 
  mhs = db.collection('mahasiswa').document(uid).get()
  mahasiswa = mhs.to_dict()
  mahasiswa['id'] = mhs.id
  return render_template("update.html",mahasiswa=mahasiswa)  

@app.route("/updatedata/<uid>")
def updatedata(uid):
  nama = request.form.get("nama")
  nilai = request.form.get("nilai")
  alamat = request.form.get("alamat")
  email = request.form.get("email")
  no = request.form.get("no")
  foto = request.form.get("foto") 

#update ke firebase
  db.collection('mahasiswa').document(uid).update({
    'nama':nama,
    'nilai' : int(nilai),
    'alamat' : alamat,
    'email' : email,
    'no_hp' : no,
    'foto' : foto
  })
  return redirect('/index')
""" ------------------------------------------------------------------ """
@app.route("/delete/<uid>")
def delete(uid):
   
#delete ke firebase
  db.collection('mahasiswa').document(uid).delete()
  return redirect('/index') 
  
""" ------------------------------------------------------------------- """

@app.route("/login")
def login(): 
  return render_template("login.html")

""" -------------------------------------------------------------------- """

@app.route("/proseslogin", methods=["POST"])
def proseslogin(): 
  user = request.form.get('username')
  pas = request.form.get('pass')

  
  admin = db.collection('admin').where("username","==",user).stream()
  for doc in admin :
    adm = doc.to_dict()
    if adm['password'] == pas :
        return redirect('/index')  
    
          

  return render_template("login.html")


  """ cara di backend ke dua""" 
""" @app.route('/detail/<uid>')
def detail(uid):
    mahasiswa = None
    for m in daftar_mahasiswa:
        if m['id'] == int(uid):
            mahasiswa = m
    return render_template('detail.html', mahasiswa=mahasiswa) """
if __name__=="__main__":
  app.run(debug=True)