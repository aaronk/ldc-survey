'''
@author: Aaron Kitzmiller <aaron.kitzmiller@gmail.com>
@copyright: 2017. All rights reserved.
@license: GPL v2.0
'''

import os, traceback, subprocess, re, socket
import hmac, hashlib
from cgi import parse_qs, escape

html = '''

'''


def application(environ, resp):
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    resp("200 OK", [('Content-Type', 'text/plain')])
    return ['Hello\n']

    # request_body = environ['wsgi.input'].read(request_body_size)
    # d = parse_qs(request_body)

    # age = d.get('age', [''])[0] # Returns the first age value.
    # hobbies = d.get('hobbies', []) # Returns a list of hobbies.

    # # Always escape user input to avoid script injection
    # age = escape(age)
    # hobbies = [escape(hobby) for hobby in hobbies]

    # # Doing the usual environment variable handling in application, cause it's all in environ
   
    # DB_USER     = environ.get('DB_USER')
    # DB_PASSWORD = environ.get('DB_PASSWORD')
    # DB          = environ.et('DB')
 
    # txt = ''
    
    # try:
                 
            
    #     txt = 'OK'
    # except Exception as e:
    #     txt = 'Error: %s\n%s' % (str(e),traceback.format_exc())
    #     logger.error(txt)
    #     resp("500 Internal Server Error", [ ('Content-Type', 'text/plain') ])
    #     return txt

    # return txt + '\n'
