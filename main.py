from flask import Flask, render_template, url_for
app = Flask(__name__, static_url_path='/static')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')
def pro_pic(): 
    return app.send_static_file('home.html')

@app.route('/img/')
def sendpics(path):
    return app.send_static_file('tamuhackpic.png')

@app.route('/about')
def about():
    return render_template('about.html', posts = posts, title='About' )

if __name__ == '__main__':
    app.run(debug=True)



