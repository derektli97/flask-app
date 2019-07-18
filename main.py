from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/home')
# @app.route('/templates/home.html')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
# @app.route('/templates/about.html')
def about():
    return render_template('about.html', posts = posts, title='About' )

posts = [
    {
        'author': 'Derek Li',
        'title': 'Blog Post 1',
        'content': 'First Post',
        'date_posted': 'July 17'
    },
    {
        'author': 'Michael Feng',
        'title': 'Blog Post 2',
        'content': 'Post 2',
        'date_posted': 'July 18'
    },  
]

if __name__ == '__main__':
    app.run(debug=True)

