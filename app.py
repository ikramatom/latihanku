from flask import Flask, render_template

""" ---------fungsi--------------------------------------- """
app = Flask(__name__)
#ini halaman index

@app.route("/index")
def index(): 
  return render_template("index.html") 

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