from flask import Flask, request, url_for, redirect,render_template
import modelGenerator

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('home_page.html')

@app.route('/home_page', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        if str(request.form.get('Prediction'))=='Prediction':
           return render_template('prediction.html')

        else:
            return redirect(url_for('home_page'))

    elif request.method=='GET':
        return 'hello'


@app.route('/prediction', methods=['POST'])
def prediction():
    error = None

    if str(request.form.get('Home')) == 'Home':
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



if __name__=='__main__':
    app.run(debug=True)