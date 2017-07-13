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
@app.route('/lists/<active_bucket>', methods=['GET','POST'])
def lists(active_bucket=None):
    if 'active_user' in session:
        if request.method=='POST':
            if request.form['submit']=='Add':
                registeredusers[session['active_user']].add_bucket(Bucket(request.form['listname']))
            else:
                registeredusers[session['active_user']].get_buckets()[request.form['listname']]=registeredusers[session['active_user']].get_buckets().pop(active_bucket)
            return redirect('/lists')
        else:
            if not 'active_user' in session:
                return redirect('/login')
            else:
                return render_template('lists.html',bucket=active_bucket,buckets=registeredusers[session['active_user']].get_buckets())
    else:
        abort(403)
@app.route('/lists/<listname>/<action>', methods=['GET','POST'])
def modify_lists(listname,action):
    if 'active_user' in session:
        if action=="delete":
            del registeredusers[session['active_user']].get_buckets()[listname]
            return redirect('/lists')
        elif action=="edit":
            return redirect('/lists/'+listname)
    else:
        abort(403)
@app.route('/items/<listname>', methods=['GET','POST'])
@app.route('/items/<listname>/<itemname>', methods=['GET','POST'])
@app.route('/items/<listname>/<itemname>/<action>', methods=['GET','POST'])
def listshandler(listname=None,itemname=None,action=None):
    if 'active_user' in session:
        if request.method=='POST':
            if request.form['submit']=='Add':
                registeredusers[session['active_user']].get_buckets()[listname].add_item(Item(request.form['itemname']))
            else:
                registeredusers[session['active_user']].get_buckets()[listname].get_items()[request.form['itemname']]=registeredusers[session['active_user']].get_buckets()[listname].get_items().pop(itemname)
                registeredusers[session['active_user']].get_buckets()[listname].get_items()[request.form['itemname']].status=request.form['status']
            return redirect('/items/'+listname)
        else:
            if not action is None:
                #return render_template('items.html',bucket=listname,items=registeredusers[session['active_user']].get_buckets()[listname].get_items(),item=None)
                if action=='delete':
                    del registeredusers[session['active_user']].get_buckets()[listname].get_items()[itemname]
                    return redirect('/items/'+listname)
                elif action=='edit':
                    #return redirect('/items/'+listname+'/'+itemname)
                    return render_template('items.html',bucket=listname,items=registeredusers[session['active_user']].get_buckets()[listname].get_items(),item=itemname)
                else:
                    return redirect('/items/'+listname)
            else:
                return render_template('items.html',bucket=listname,items=registeredusers[session['active_user']].get_buckets()[listname].get_items(),item=itemname)
    else:
        abort(403)
@app.route('/logout', methods=['GET','POST'])
def logout():
    if 'active_user' in session:
        session.pop('active_user',None)
    return redirect('/login')

@app.errorhandler(404)
def page_not_found(e):
    return '<h1>Error 404</h1><h3>Page does not exist on this Bucketlist application</h3>'

@app.errorhandler(403)
def page_not_found(e):
    return '<h1>Error 403</h1><h3>You are not authorized to view this page</h3>'