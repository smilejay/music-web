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

if __name__ == '__main__':
    django.setup()
    openid = '123abc'
    print get_user(openid)