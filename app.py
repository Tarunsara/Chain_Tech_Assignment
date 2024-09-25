from flask import Flask, render_template, request
from datetime import datetime
import csv
import os

app = Flask(__name__)

CSV_FILE = 'submissions.csv'

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Email'])  # Headers

@app.route('/', methods=['GET'])
def index():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('web_page.html', time=current_time)

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/form', methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/user/<username>', methods=['GET'])
def user_profile(username):
    return render_template('user.html', username=username)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email])
    
    return render_template('form.html')

@app.route('/submissions', methods=['GET'])
def show_submissions():
    submissions = []
    
    with open(CSV_FILE, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        submissions = list(reader)
    
    return render_template('submissions.html', submissions=submissions)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)