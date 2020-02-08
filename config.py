#!/usr/bin/env python
# coding: utf-8

# In[1]:


import configparser
import pathlib


# In[2]:


config = configparser.ConfigParser()
config.read('config.ini')
datadir = pathlib.Path(config['paths']['datadir']).expanduser()

