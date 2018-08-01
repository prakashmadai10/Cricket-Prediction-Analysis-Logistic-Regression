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
        elif str(request.form.get('Statistics')) == 'Statistics':
            return render_template('analysis.html')
        elif str(request.form.get('Analysis')) == 'Analysis':
            return render_template('feature_analysis.html')

        else:
            return redirect(url_for('UI1'))

    elif request.method=='GET':
        return 'hello'

@app.route('/prediction', methods=['POST'])
def prediction():
    error = None
    teamA =str(request.form.get('team1')).title()
    teamB=str(request.form.get('team2')).title()
    venue=str(request.form.get('venue')).capitalize()
    tosswin=str(request.form.get('tosswin')).title()
    dec=str(request.form.get('tossdis'))
    if (teamA == teamB):
        error="Please Choose Different Countries"
        return error
    if (tosswin != teamB and tosswin != teamA):
        error="Please Enter valid toss winner"
        return error
    a,b,c,d,e= modelGenerator.startPrediction(teamA, teamB, venue, tosswin, dec)

    if (e=='a'):
        return "please enter valid city"
    return render_template('UI3.html',value=a,value1=b,value2=c,value3=d)
    #return render_template('welcome.php')

@app.route('/analysis', methods=['GET', 'POST'])
def analysis():
    if request.method == 'POST':
        select = str(request.form.get('role'))
        # print(select)
        player = str(request.form.get('playername'))

        a, b, c, d, e, f, g,det,re,nam = database.readdata(player)
        # a1= ", ".join( repr(e) for e in a )
        a1 = str(a)[2:-3]
        b1 = str(b)[2:-3]
        c1 = str(c)[2:-3]
        d1 = str(d)[2:-3]
        e1 = str(e)[2:-3]
        f1 = str(f)[2:-3]
        re1=str(re)[2:-3]
        detail1=str(det)[2:-3]
        nam1 = str(nam)[3:-4]
        print(nam1)
        graph.graphofplayer(select,re1)

        return render_template('UI4.html', naam=nam1, m=a1, i=b1, r=c1, h=d1, avg=e1, sr=f1, p=g,detail=detail1,idd=re1)


        return 'her'


    return "helll"

#@app.route('/CapstoneProject/')
#def CapstoneProject():
  #print 'I got clicked!'

 # return render_template('CapstoneProject.py')

if __name__=='__main__':
    app.run(debug=True)