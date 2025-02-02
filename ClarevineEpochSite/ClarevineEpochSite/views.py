"""
Routes and views for the flask application.
"""

from flask import render_template
from ClarevineEpochSite import app

@app.route("/")
def start():
    return render_template("start.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/player")
def player():
    return render_template("player.html")

#@app.route('/')
#@app.route('/home')
#def home():
    """Renders the home page."""
#    return render_template(
#        'index.html',
#        title='Home Page',
#        year=datetime.now().year,
#    )

#@app.route('/contact')
#def contact():
#    """Renders the contact page."""
#    return render_template(
#        'contact.html',
#        title='Contact',
#        year=datetime.now().year,
#        message='Your contact page.'
#    )

#@app.route('/about')
#def about():
#    """Renders the about page."""
#    return render_template(
#        'about.html',
#        title='About',
#        year=datetime.now().year,
#        message='Your application description page.'
#    )
