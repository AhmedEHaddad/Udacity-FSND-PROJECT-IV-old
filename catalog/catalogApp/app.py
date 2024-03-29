# Udacity-FSND-ProjectII: building a web App
# anlaysing the data from the news database
#created by: ahmed.e.haddad2.0@gmail.com

#########################################
#Imports
#########################################
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
#from flask_bootstrap import Bootstrap


app = Flask(__name__)
#bootstrap = Bootstrap(app)

APPLICATION_NAME = "Electro Portal Web Application"


####################################################
# Connect to Database and create database session
####################################################
engine = create_engine('sqlite:///electroportal.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()




#########################################
#CRUD functionality
#########################################


#########################################
#Authenication & Authorization
#########################################



#########################################
#JSON API Endpoints
#########################################



#########################################
#Imports
#########################################




#########################################
#Imports
#########################################







###############################################
#Running the server #always at the end of file
###############################################
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)


######################End Of Code#####################################
