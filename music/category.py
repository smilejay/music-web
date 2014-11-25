# -*- coding: utf-8 -*-
'''
Created on Nov 23, 2014

@author: Jay <smile665@gmail.com>
'''
import django
from music.models import Category
from music.serializers import CategorySerializer
from lib.logger import CarLogger

logger = CarLogger().getLogger()


def get_categories():
    '''
    @summary: get all the categories.
    @return: a dict (key: id, value: name)
    '''
    ret = dict()
    c = Category.objects.all()
    c_s = CategorySerializer(c, many=True)
    if c_s:
        for i in c_s.data:
            ret[i['id']] = i['name']
    return ret


def add(data):
    '''
    @summary: add category record(s).
    @parm data: a dict for the Category's serializer.
    @return: None.
    '''
    ret = False
    a_se = CategorySerializer(data=data, many=True)
    if a_se.is_valid():
        a_se.save()
        ret = True
    else:
        logger.info('invalid data for category table.\n' +
                    'data: %s' % data)
        ret = False
    return ret


if __name__ == '__main__':
    django.setup()
#    add(data=[{'name': '流行音乐'}, {'name': '校园名谣'}, {'name': '欧美经典'}])
    print get_categories()