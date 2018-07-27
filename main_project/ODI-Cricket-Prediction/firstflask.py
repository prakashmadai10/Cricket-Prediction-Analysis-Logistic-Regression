from flask import Flask, request, url_for, redirect,render_template
from wtforms import Form, TextAreaField, validators
import cgi
import cgitb
import modelGenerator
import graph
import database

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('UI1.html')

@app.route('/UI1', methods=['GET', 'POST'])
def UI1():
    if request.method == 'POST':
        if str(request.form.get('Prediction'))=='Prediction':
           return render_template('prediction.html')
        elif str(request.form.get('Analysis')) == 'Analysis':
            return render_template('analysis.html')
        else:
            return redirect(url_for('UI1'))

    elif request.method=='GET':
        return 'hello world'

@app.route('/prediction', methods=['POST'])
def prediction():
    teamA =str(request.form.get('team1')).title()
    teamB=str(request.form.get('team2')).title()
    venue=str(request.form.get('venue')).capitalize()
    tosswin=str(request.form.get('tosswin')).title()
    toss_decision=str(request.form.get('toss decision'))
    a,b,c,d,e= modelGenerator.startPrediction(teamA, teamB, venue, tosswin, toss_decision)
    if (e=='a'):
        return "please enter valid city"
    return render_template('UI3.html',value=a,value1=b,value2=c,value3=d)

@app.route('/analysis', methods=['GET', 'POST'])
def analysis():
    if request.method == 'POST':
        select = str(request.form.get('role'))
        # print(select)
        player = str(request.form.get('playername'))
        graph.graphofplayer(select, player)
        a, b, c, d, e, f, g = database.readdata(player)
        # a1= ", ".join( repr(e) for e in a )
        a1 = str(a)[2:-3]
        b1 = str(b)[2:-3]
        c1 = str(c)[2:-3]
        d1 = str(d)[2:-3]
        e1 = str(e)[2:-3]
        f1 = str(f)[2:-3]

        return render_template('UI4.html', naam=player, m=a1, i=b1, r=c1, h=d1, avg=e1, sr=f1, p=g)


        return 'her'


    return "helll"

if __name__=='__main__':
    app.run(debug=True)