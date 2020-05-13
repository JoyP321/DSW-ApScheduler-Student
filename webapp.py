from flask import Flask
from flask import render_template
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
 
import time
 
app = Flask(__name__)

#TODO: add the code for the ApScheduler here
scheduler = BackgroundScheduler({'apscheduler.timezone':'America/Los_Angeles'})
scheduler.start()


@app.route('/')
def welcome():
    return render_template('home.html', content = '')
 
 
def my_task():
    return render_template('home.html', content = 'task exacuted')
  
  
scheduler.add_job(my_task, tigger= 'interval', minutes=1)


if __name__=="__main__":
    app.run(debug=False)
