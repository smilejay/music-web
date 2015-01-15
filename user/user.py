'''
Created on Jan 15, 2015

@author: Jay <smile665@gmail.com>
'''

from user.models import User
from user.serializers import UserSerializer


def add_update(data):
    '''
    @summary: add (if no) or update a user record.
    @parm data: a dict for the User's serializer.
    @return: None.
    '''
    try:
        ri = User.objects.get(openid=data['openid'])
        ri_se = UserSerializer(ri, data=data, partial=True)
    except User.DoesNotExist:
        ri_se = UserSerializer(data=data)
    if ri_se.is_valid():
        ri_se.save()