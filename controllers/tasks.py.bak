# -*- coding: utf-8 -*-

import gluon.contrib.simplejson

def index():
    rows = db(db.task).select().as_list()
    return dict(task_list=gluon.contrib.simplejson.dumps(rows))
