from flask import Flask, request, Response, redirect, url_for, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
  return "<a href='/posts'>Posts 1</a>"

@app.route("/posts/<int:id>")
@app.route("/posts")
def posts(id):
  titulo = request.args.get('titulo')
  data = dict(
    path=request.path,
    referrer=request.referrer,
    content_type=request.content_type,
    method=request.method,
    titulo=titulo,
    id=id if id else 0
  )
  return data

@app.route("/response")
def response():
  return render_template("response.html")

@app.route("/redirect2")
def redirect2():
  return redirect('/response')

@app.route("/redirect3")
def redirect3():
  return redirect(url_for('response'))



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5002,debug=True)