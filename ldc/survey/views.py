'''
@author: Aaron Kitzmiller <aaron.kitzmiller@gmail.com>
@copyright: 2017. All rights reserved.
@license: GPL v2.0
'''
import traceback
from django.shortcuts import render
from collections import OrderedDict
from django.core.mail import send_mail

import logging
logger = logging.getLogger('ldc-survey')

titles = OrderedDict()
titles['learn']     = 'Learn (high interest, low expertise)'
titles['mentor']    = 'Mentor (high interest, high expertise)'
titles['forgetit']  = 'Forget it (low interest, low expertise)'
titles['inapinch']  = 'In a pinch (low interest, high expertise)'
titles['name']      = 'Name'
titles['email']     = 'Email'
titles['involved']  = 'Would you like to be more involved?'


def survey(request):
    '''
    The actual survey
    '''
    if request.method == 'POST':
        try:
            lines = []
            for k,v in titles.iteritems():
                lines.append(v)
                lines.append(request.POST.get(k,''))
                lines.append('')

            # logger.info('\n'.join(lines))
            send_mail('stuff','\n'.join(lines),'aaron.kitzmiller@gmail.com',['aaron.kitzmiller@gmail.com'])
            return render(request,'survey/thanks.html')
        except Exception as e:
            logger.error('Error processing survey: %s\n%s' % (str(e),traceback.format_exc()))
            return render(request,'survey/survey.html',{'error_message' : 'Did not work.'})
    else:
        return render(request,'survey/survey.html',{'email_user' : EMAIL_HOST_USER})
