#multiple routes/URL
from flask import Flask
 
application =Flask (__name__)
 
@application.route('/')
def home() :
    return " This is home page" 

@application.route('/contact')
def contact():
    return "This is contact page"

@application.route('/student')
def student():
    return "My Students page"

@application.route('/about')
def about():
    return "This is the about page"

application.run(debug=True)