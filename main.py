from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://NAMEOFUSER:USERPASSWORD@localhost:3336/NAMEOFDATABASE'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'INSERTASECRETKEYASASTRING'

@app.route('/', methods=['GET', 'POST'])
def index():
    return ('Hello World')

if __name__ == '__main__':
    app.run()
