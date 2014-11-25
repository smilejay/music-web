'''
Created on Nov 24, 2014

@summary: some utilities in the system.
@author: Jay <smile665@gmail.com>
'''
security_key = 'shuai-music-app'


def key_validation(key):
    '''
    @summary: validate the key used by the clients.
    '''
    ret = False
    if key.lower() == security_key:
        ret = True
    else:
        ret = False
    return ret


if __name__ == '__main__':
    print key_validation('haha')
    print key_validation(security_key)