from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
   if request.method == 'GET':
       print("We received GET")
       return render_template("contact.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

@app.route('/mypage/me')
def me():
     return render_template("omnie.html")

@app.route('/')
def index():
     return render_template("index.html")