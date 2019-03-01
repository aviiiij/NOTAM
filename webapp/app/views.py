# views.py
from flask import render_template

from app import app
from app import extract
@app.route('/') #TO-DO : By Aditya and Avi 
def index():
    return render_template("index.html")


@app.route('/visualizer') #TO-DO : By Kiteretsu
def visualizer():
    return render_template("visualizer/visual.html")


@app.route('/listview')  # TO-DO : By Hatel di
def listview():
    return render_template("index.html")

@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/processor', methods=['POST'])  # TO-DO : By Rushang and akshay
def processor():

    return Response(
            json.dumps(
                    extract.extract('NOTAM.pdf')
                ), mimetype='application/json'
            )
