'''
Created on Jan 15, 2015

@author: Jay <smile665@gmail.com>
'''

from django.views.decorators.csrf import csrf_exempt
from rest_framework.request import Request
from lib.response import JSONResponse
from user.qq_user import get_user, add_update_user


@csrf_exempt
def get_user_by_openid(request):
    '''
    @summary: get a user by QQ openid.
    '''
    if request.method == 'GET':
        req = Request(request)
        openid = req.QUERY_PARAMS.get('openid', default='123abc')
        data = get_user(openid)
        return JSONResponse(data=data, status=200)
    else:
        return JSONResponse({'error': 'It only support HTTP GET method.'},
            status=200)


@csrf_exempt
def add_user(request):
    '''
    @summary: add (update) a user  from QQ login or .
    '''
    if request.method == 'POST':
        req = Request(request)
        data = req.DATA
        force = data.get('force', default=False)
        if force:
            force = True
        openid = add_update_user(data, force=force)
        return JSONResponse(data={'openid': openid}, status=200)
    else:
        return JSONResponse({'error': 'It only support HTTP POST method.'},
            status=200)