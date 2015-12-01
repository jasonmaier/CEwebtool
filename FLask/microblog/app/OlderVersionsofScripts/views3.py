
# coding: utf-8

# In[1]:

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Jason'} #ME
    posts = [ # Fake array of Posts
        {
            'author': {'nickname': 'Raja'},
            'body': 'This is a great CEtool!'
        },
        {
            'author': {'nickname': 'John'},
            'body': 'Keep Going!'
        }
    ]
    return render_template('index.html', 
                          title = 'Home',
                          user = user,
                          posts=posts)


# 
