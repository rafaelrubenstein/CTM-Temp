from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def construction():
    return render_template('construction.html')

@app.route('/contact')
def resume():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ =='__main__':
    app.run()