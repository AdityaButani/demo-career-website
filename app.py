from flask import Flask,render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'location': 'benguluru, India',
        'salary' : 'Rs. 10,00,000'
    },

    {
        'id' : 2,
        'title' : 'Data scientist',
        'location': 'New delhi, India',
        'salary' : 'Rs. 15,00,000'
    },

    {
        'id' : 3,
        'title' : 'backend developer',
        'location': 'Mumbai, India',
        'salary' : 'Rs. 20,00,000'
    },

    {
        'id' : 4,
        'title' : 'frontend developer',
        'location': 'remote',
        'salary': 'Rs.15,00,000'
    }

]
@app.route('/')
def helloworld ():
    return render_template('index.html', jobs = JOBS)
    
@app.route('/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug = True)
  
