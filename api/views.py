from django.views.decorators.csrf import csrf_exempt
from rest_framework.request import Request
from lib.response import JSONResponse
from lib.utility import key_validation
from music.song import get_songs


@csrf_exempt
def get_songs_by_category(request):
    '''
    @summary: get songs by category id.
    '''
    if request.method == 'GET':
        req = Request(request)
        raw_data = req.DATA
        category = int(raw_data.get('category', default=1))
        data = get_songs(category=category)
        return JSONResponse(data=data, status=200)
    else:
        return JSONResponse({'error': 'It only support HTTP GET method.'},
            status=200)
