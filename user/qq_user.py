# -*- coding: utf-8 -*-
'''
Created on Jan 15, 2015

@author: Jay <smile665@gmail.com>
'''

import django
from user.models import User
from user.serializers import UserSerializer


def add_update(data):
    '''
    @summary: add (if no) or update a user record.
    @parm data: a dict for the User's serializer.
    @return: None.
    '''
    try:
        user = User.objects.get(openid=data['openid'])
        user_se = UserSerializer(user, data=data, partial=True)
    except User.DoesNotExist:
        user_se = UserSerializer(data=data)
    if user_se.is_valid():
        user_se.save()


def get_user(openid):
    '''
    @summary: get user info by openid.
    @param openid: the OpenID of the QQ login info.
    '''
    ret = None
    try:
        user = User.objects.get(openid=openid)
        user_se = UserSerializer(user)
        ret = user_se.data
    except User.DoesNotExist:
        pass
    return ret


def add_update_user(data, force=False):
    '''
    @summary: add or update a user's profile.
    @param data: a user's dict data.
    @param force: if True, update all the profile from data;
                  else only update 'figureurl' field.
    @return: the openid or None.
    '''
    ret = None
    if not 'openid' in data:
        pass
    else:
        user = get_user(data['openid'])
        if user and not force:
            if 'figureurl' in data:
                user['figureurl'] = data['figureurl']
            add_update(user)
        else:
            add_update(data)
        ret = data['openid']
    return ret


if __name__ == '__main__':
    django.setup()
    openid = '123abc'
    print get_user(openid)
    data = {'openid': '123abc', 'nickname': '笑遍世界', 'city': '杭州',
            'figureurl': 'http://smilejay.b0.upaiyun.com/wp-content/uploads/2013/09/kvm_principals_and_practices1.jpg'}
    add_update_user(data, force=False)