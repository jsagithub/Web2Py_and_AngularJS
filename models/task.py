# -*- coding: utf-8 -*-
db.define_table('task_priority',
    Field('priority', type='string'),
    Field('css_class', type='string'),
    Field('days', type='integer'),
    auth.signature
)    
if db(db.task_priority).count() == 0:
    db.task_priority.insert(priority='Urgent', css_class='label-danger', days='1')  
    db.task_priority.insert(priority='Not Urgent', css_class='label-warning', days='5') 
    db.task_priority.insert(priority='When you feel good', css_class='label-default', days='0')        
pass    
db.define_table('task',
    Field('name', type='text'),       
    Field('limit_date', type='datetime'), 
    Field('activity', type='boolean'), 
    auth.signature
)

db.define_table('task_to',
    Field('task_id', db.task),
    Field('user_id', db.auth_user),   
    auth.signature
)

db.define_table('task_comment',
    Field('task_id', db.task),       
    Field('task_comment', type='text'),  
    auth.signature
)
