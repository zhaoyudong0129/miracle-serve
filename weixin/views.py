import hashlib

import logging

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

logger = logging.getLogger(__name__)


@api_view(['GET', 'POST'])
def home(request):
    signature = request.query_params.get('signature','none')
    timestamp = request.query_params.get('timestamp','none')
    nonce = request.query_params.get('nonce','none')
    echostr = request.query_params.get('echostr','none')

    logger.info('signature:{},timestamp:{},nonce:{},echostr:{}'.format(signature, timestamp, nonce, echostr))

    token = 'hello123'

    weixin_list = [token, timestamp, nonce]
    weixin_list.sort()
    sha1 = hashlib.sha1()

    map(sha1.update, weixin_list)
    hashcode = sha1.hexdigest()

    if request.method == 'GET':
        if hashcode == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse('error')
