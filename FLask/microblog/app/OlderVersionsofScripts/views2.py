
# coding: utf-8

# In[1]:

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Jason'} #ME
    return render_template('index.html', 
                          title = 'Home',
                          user = user)


# 
