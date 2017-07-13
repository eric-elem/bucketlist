from app import app
from flask import Flask, request, session, g, redirect, url_for, abort,render_template, flash, _app_ctx_stack
from src.modals import TheUser, Bucket, Item
registeredusers = {}
app.secret_key = 'ggtsha6667jshjhsaknks9'

@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        if request.form['username'] in registeredusers:
            if request.form['password'] == registeredusers[request.form['username']].password:
                session['active_user']=request.form['username']
                return redirect('/lists');
            else:
                return redirect('/login')
        else:
            return redirect('/register')
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        if request.form['password']==request.form['rpt_password']:
            registeredusers[request.form['username']]=TheUser(request.form['name'],request.form['username'],request.form['password'])
            return redirect('/login')
        else:
            return 'Passwords dont match'
    else:
        return render_template('register.html')
     
@app.route('/lists', methods=['GET','POST'])
def lists():
    if request.method=='POST':
        registeredusers[session['active_user']].add_bucket(Bucket(request.form['listname']))
        return redirect('/lists')
    else:
        if session['active_user'] is None:
            return redirect('/login')
        else:
            return render_template('lists.html',buckets=registeredusers[session['active_user']].get_buckets())

@app.route('/items/<listname>', methods=['GET','POST'])
def listshandler(listname):
    if request.method=='POST':
        registeredusers[session['active_user']].get_buckets()[listname].add_item(Item(request.form['itemname']))
        return redirect('/items/'+listname)
    else:
        return render_template('items.html',bucket=listname,items=registeredusers[session['active_user']].get_buckets()[listname].get_items())

@app.route('/items', methods=['GET','POST'])
def items():
    if request.method=='POST':
        registeredusers[session['active_user']].get_buckets()[request.form['bucketname']].add_item(Item(request.form['itemname']))
        return redirect('/lists')
    else:
        if session['active_user'] is None:
            return redirect('/login')
        else:
            return render_template('items.html')