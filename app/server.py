from flask import Flask
from flask import render_template, request, url_for
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from form import prompt
import call

app=Flask(__name__)
app.secret_key="random key"
@app.route('/', methods=['GET', 'POST'])
#create a function that prompts the user for the location
def angry():
	#userinput=prompt()
	
	if request.method == 'GET':
		return render_template("login.html")
	
	elif request.method=='POST':
		name=request.form['query']
		return render_template("home.html")

#run app when called 
if __name__ =='__main__':
	app.run(debug=True)