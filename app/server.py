from flask import Flask
from flask import render_template, request, url_for
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from form import prompt
import AngryAlarm_pyscript 

app=Flask(__name__)
app.secret_key="random key"
@app.route('/', methods=['GET', 'POST'])

def login():
	userinput=prompt()
	name=''
	phone=''
	tasks=[]

	if request.method == 'GET':
		return render_template("main_page.html", form=userinput)
	
	elif request.method=='POST':
		name=request.form['name']
		phone=request.form['phone']
		task=request.form['task']
		importance=request.form['importance']
		date=request.form['date']
		time=request.form['time']
		
		return render_template("tasks_page.html")


#run app when called 
if __name__ =='__main__':
	app.run(debug=True)