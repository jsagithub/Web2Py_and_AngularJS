# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

import gluon.contrib.simplejson

def index():
    rows = db(db.task).select()
    return get_all_tasks(rows)

def get_all_tasks(rows):
    """
    cant use this function
            def index():
            rows = db(db.recipe).select().as_list()
            return dict(recipe_list=gluon.contrib.simplejson.dumps(rows))
    at the simple way because im using fields datetime in th database :(
    """
    lista = list()
    for row in rows:
        arr = dict()
        for k,v in row.items():
            arr[k] = str(v)
        lista.append(arr)
    return dict(task_list=gluon.contrib.simplejson.dumps(lista))

def get_task(task_id):
    task= db(db.task.id==task_id).select().first().as_dict()
    return task

def add_task():
    new_task=gluon.contrib.simplejson.loads(request.body.read())
    task_id=db.task.validate_and_insert(name=new_task['name'],
                                        limit_date=new_task['limitdate'],
                                        priority_id=new_task['priority'])
    new_task=get_task(task_id)
    return  gluon.contrib.simplejson.dumps(dict(newTask=new_task))

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
