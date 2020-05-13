from flask import Flask
from flask import render_template
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
 
import time
 
app = Flask(__name__)

#TODO: add the code for the ApScheduler here
scheduler = BackgroundScheduler({'apscheduler.timezone':'America/Los_Angeles'})
scheduler.start()
scheduler.add_job(my_task, tigger= 'interval', minutes=1)
session['taskCount']= 0

@app.route('/')
def welcome():
    return render_template('home.html', content = '')
 
 
def my_task():
    session['taskCount'] = session['taskCount']+1
    return render_template('home.html', content = 'task count' +str(session['taskCount']))
  
if __name__=="__main__":
    app.run(debug=False)
