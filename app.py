from flask import Flask, make_response, render_template, request, url_for, redirect, session
import tweetfetch 

app = Flask(__name__)
app.config["SECRET_KEY"] = "Prs7IGkqMNcYn7nrSA5i4Q"

# The route to landing page
@app.route('/',methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        session["USERNAME"] = request.form.get('username')
        categorylist, categoryval = tweetfetch.get_tweets(request.form.get('username'))
        session["SAFE"] = categorylist['Safe To Ignore']
        session["CONCERN"] = categorylist['Concerned']
        session["HIGHCONCERN"] = categorylist['Strongly Concerned']
        print(categorylist)
        return redirect(url_for('results', category = categoryval))
        # return render_template('results.html', category = categoryval)
    return render_template('home.html')

# The route to the results
@app.route('/results',methods=['POST', 'GET'])
def results():
    categoryval = request.args.get("category")
    return render_template('results.html', category = categoryval, username = session.get("USERNAME"))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', username = session.get("USERNAME"))

if __name__ == '__main__':
    app.run(debug=True)