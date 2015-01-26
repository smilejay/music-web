'''
Created on Jan 22, 2015

@author: Jay <smile665@gmail.com>
'''

from rest_framework.request import Request
from lib.response import JSONResponse
from music.song import search_songs, search_songs_by_singer, all_singers
from api.config import STATUS_OK, STATUS_ERROR


def search(request):
    '''
    @summary: search songs by a keyword.
    '''
    if request.method == 'GET':
        req = Request(request)
        keyword = req.QUERY_PARAMS.get('keyword', default=None)
        num = int(req.QUERY_PARAMS.get('num', default=5))
        if keyword:
            detail = search_songs(keyword, num)
            data = {'status': STATUS_OK, 'detail': detail}
        else:
            msg = 'keyword param is needed.'
            data = {'status': STATUS_ERROR, 'msg': msg}
        return JSONResponse(data=data, status=200)
    else:
        msg = 'It only support HTTP GET method.'
        return JSONResponse({'status': STATUS_ERROR, 'msg': msg}, status=200)


def search_by_singer(request):
    '''
    @summary: search songs by a keyword of a singer.
    '''
    if request.method == 'GET':
        req = Request(request)
        keyword = req.QUERY_PARAMS.get('keyword', default=None)
        num = int(req.QUERY_PARAMS.get('num', default=5))
        if keyword:
            detail = search_songs_by_singer(keyword, num)
            data = {'status': STATUS_OK, 'detail': detail}
        else:
            msg = 'keyword param is needed.'
            data = {'status': STATUS_ERROR, 'msg': msg}
        return JSONResponse(data=data, status=200)
    else:
        msg = 'It only support HTTP GET method.'
        return JSONResponse({'status': STATUS_ERROR, 'msg': msg}, status=200)


def get_singers(request):
    '''
    @summary: get all the singers of the songs.
    '''
    if request.method == 'GET':
        detail = all_singers()
        data = {'status': STATUS_OK, 'detail': detail}
        return JSONResponse(data=data, status=200)
    else:
        msg = 'It only support HTTP GET method.'
        return JSONResponse({'status': STATUS_ERROR, 'msg': msg}, status=200)