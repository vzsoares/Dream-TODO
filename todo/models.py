from django.db import models

# Create your models here.


def List():
    list = ['list of obj, index sort']
    obj = {
        'id': 'id',
        'title': 'titleTXT',
        'description': 'descriptionTXT',
        'done': 'boolean',
    }
    user = {
        'id': 'id references user ID',
        'todos': 'json.stringfy(list)'
    }
