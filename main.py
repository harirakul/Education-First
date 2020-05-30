from flask import Flask, render_template
import course

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/cs')
def cs():
  text = (course.writeHTML('cs'))
  return (text)

@app.route('/business')
def business():
  text = (course.writeHTML('business'))
  return (text)

@app.route('/humanities')
def humanities():
  text = (course.writeHTML('humanities'))
  return (text)

@app.route('/data-science')
def datascience():
  text = (course.writeHTML('data-science'))
  return (text)

@app.route('/personal-development')
def personaldevelopment():
  text = (course.writeHTML('personal-development'))
  return (text)

@app.route('/art-and-design')
def artanddesign():
  text = (course.writeHTML('art-and-design'))
  return (text)

@app.route('/programming-and-software-development')
def programmingandsoftwaredevelopment():
  text = (course.writeHTML('programming-and-software-development'))
  return (text)
  
@app.route('/engineering')
def engineering():
  text = (course.writeHTML('engineering'))
  return (text)

@app.route('/health')
def health():
  text = (course.writeHTML('health'))
  return (text)

@app.route('/science')
def science():
  text = (course.writeHTML('science'))
  return (text)

@app.route('/social-sciences')
def socialsciences():
  text = (course.writeHTML('social-sciences'))
  return (text)


app.run(host='0.0.0.0', port=8000)


