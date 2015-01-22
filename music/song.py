# -*- coding: utf-8 -*-
'''
Created on Nov 24, 2014

@author: Jay <smile665@gmail.com>
'''
import django
from music.models import Song
from music.serializers import SongSerializer
from music.category import get_categories
from lib.logger import CarLogger

logger = CarLogger().getLogger()


def get_songs(category=1):
    '''
    @summary: get songs by category.
    @return: a list of songs.
    '''
    ret = []
    categories = get_categories()
    s = Song.objects.filter(category=category)
    s_s = SongSerializer(s, many=True)
    if s:
        for i in s_s.data:
            i['category'] = categories[i['category']]
            ret.append(i)
    return ret


def get_songs_by_gender(gender='男'):
    '''
    @summary: get songs by singer's gender.
    @return: a list of songs.
    '''
    ret = []
    s = Song.objects.filter(gender=gender)
    s_s = SongSerializer(s, many=True)
    if s:
        for i in s_s.data:
            ret.append(i)
    return ret



def add(data):
    '''
    @summary: add song record(s).
    @parm data: a dict for the song's serializer.
    @return: None.
    '''
    ret = False
    a_se = SongSerializer(data=data, many=True)
    if a_se.is_valid():
        a_se.save()
        ret = True
    else:
        logger.info('invalid data for song table.\n' +
                    'data: %s' % data)
        ret = False
    return ret


if __name__ == '__main__':
    django.setup()
#    add(data=[{'name': '十年', 'singer': '陈奕迅', 'category': 1, 'song_file': '/mp3/1.mp3'}])
    print get_songs(category=1)
    print get_songs_by_gender(gender='男')