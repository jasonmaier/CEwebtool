
# coding: utf-8

# In[2]:

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views


# In[ ]:



