# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from rest_framework.request import Request
from lib.response import JSONResponse
from lib.utility import key_validation
from music.song import get_songs, get_songs_by_gender
from music.category import get_categories


@csrf_exempt
def get_all_categories(request):
    '''
    @summary: get all the categories.
    '''
    if request.method == 'GET':
        data = get_categories()
        return JSONResponse(data=data, status=200)
    else:
        return JSONResponse({'error': 'It only support HTTP GET method.'},
            status=200)


@csrf_exempt
def get_songs_by_category(request):
    '''
    @summary: get songs by category id.
    '''
    if request.method == 'GET':
        req = Request(request)
        category = int(req.QUERY_PARAMS.get('category', default=1))
        data = get_songs(category=category)
        return JSONResponse(data=data, status=200)
    else:
        return JSONResponse({'error': 'It only support HTTP GET method.'},
            status=200)


@csrf_exempt
def get_songs_by_singer_gender(request):
    '''
    @summary: get songs by category id.
    '''
    if request.method == 'GET':
        req = Request(request)
        gender = req.QUERY_PARAMS.get('gender', default='男')
        data = get_songs_by_gender(gender=gender)
        return JSONResponse(data=data, status=200)
    else:
        return JSONResponse({'error': 'It only support HTTP GET method.'},
            status=200)