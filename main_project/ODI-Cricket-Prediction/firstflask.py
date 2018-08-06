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

    return render_template('home_page.html')

@app.route('/home_page', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        if str(request.form.get('Prediction'))=='Prediction':
           return render_template('prediction.html')
        elif str(request.form.get('Statistics')) == 'Statistics':
            return render_template('statistics.html')
        elif str(request.form.get('Analysis')) == 'Analysis':
            return render_template('feature_analysis.html')

        else:
            return redirect(url_for('home_page'))

    elif request.method=='GET':
        return 'hello'


@app.route('/prediction', methods=['POST'])
def prediction():
    error = None
    if str(request.form.get('Statistics')) == 'Statistics':
        return render_template('statistics.html')
    elif str(request.form.get('Analysis')) == 'Analysis':
        return render_template('feature_analysis.html')
    elif str(request.form.get('Home')) == 'Home':
        return render_template('home_page.html')
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
    return render_template('prediction_result.html',value=a,value1=b,value2=c,value3=d)
    #return render_template('welcome.php')

@app.route('/player_stats', methods=['GET', 'POST'])
def player_stats():
    if request.method == 'POST':
        if str(request.form.get('Statistics')) == 'Statistics':
            return render_template('statistics.html')
        elif str(request.form.get('Prediction')) == 'Prediction':
            return render_template('prediction.html')
        elif str(request.form.get('Home')) == 'Home':
            return render_template('home_page.html')
        elif str(request.form.get('Analysis')) == 'Analysis':
            return render_template('feature_analysis.html')

        if str(request.form.get('psearch')) == 'psearch':
            select = str(request.form.get('role'))
            # print(select)
            player = str(request.form.get('playername'))

            a, b, c, d, e, f, g, det, re, nam = database.readdata(player)
            # a1= ", ".join( repr(e) for e in a )
            a1 = str(a)[2:-3]
            b1 = str(b)[2:-3]
            c1 = str(c)[2:-3]
            d1 = str(d)[2:-3]
            e1 = str(e)[2:-3]
            f1 = str(f)[2:-3]
            re1 = str(re)[2:-3]
            detail1 = str(det)[2:-3]
            nam1 = str(nam)[3:-4]
            graph.graphofplayer(select, re1)
            return render_template('player_stats.html', naam=nam1, m=a1, i=b1, r=c1, h=d1, avg=e1, sr=f1, p=g,detail=detail1,idd=re1)
        elif str(request.form.get('country')) == 'country':
            country = str(request.form.get('countryname'))

            a, b, c, d, e, f, g, det, re,rank,mstwins = database.desh(country)
            # a1= ", ".join( repr(e) for e in a )
            print(a)
            mat = str(a)[2:-3]
            w = str(b)[2:-3]
            los = str(c)[2:-3]
            tie = str(d)[2:-3]
            no = str(e)[2:-3]
            wl = str(f)[2:-3]
            hs = str(g)[2:-3]

            name = str(re)[3:-4]
            ls = str(det)[2:-3]
            rank1 = str(rank)[2:-3]
            mstwins1 = str(mstwins)[3:-4]

            return render_template('countrydisplay.html', naam=hs,rank1=rank1,mstwins1=mstwins1.capitalize(), m=mat, i=w, r=los, h=tie, avg=no, sr=wl,detail=ls,idd=name)


        return 'her'

    return "helll"
@app.route('/feature', methods=['GET', 'POST'])
def feature():
    if request.method == 'POST':
        if str(request.form.get('Statistics')) == 'Statistics':
            return render_template('statistics.html')
        elif str(request.form.get('Prediction')) == 'Prediction':
            return render_template('prediction.html')
        elif str(request.form.get('Analysis')) == 'Analysis':
            return render_template('feature_analysis.html')
        elif str(request.form.get('Home')) == 'Home':
            return render_template('home_page.html')

#@app.route('/CapstoneProject/')
#def CapstoneProject():
  #print 'I got clicked!'

 # return render_template('CapstoneProject.py')

if __name__=='__main__':
    app.run(debug=True)