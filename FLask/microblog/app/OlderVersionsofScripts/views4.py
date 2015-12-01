
# coding: utf-8

# In[1]:

from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', 
                           title='Sign In',
                           form=form)


# 
