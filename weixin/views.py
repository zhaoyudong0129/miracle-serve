import hashlib

import logging

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from wechat_sdk import WechatBasic

logger = logging.getLogger(__name__)


@api_view(['GET', 'POST'])
def home(request):
    signature = request.query_params.get('signature', 'none')
    timestamp = request.query_params.get('timestamp', 'none')
    nonce = request.query_params.get('nonce', 'none')
    echostr = request.query_params.get('echostr', 'none')

    logger.info('signature:{},timestamp:{},nonce:{},echostr:{}'.format(signature, timestamp, nonce, echostr))

    token = 'hello123'

    wechat = WechatBasic(token=token)

    if request.method == 'GET':
        if wechat.check_signature(signature, timestamp, nonce):
            logger.info('weixin token check success')
            return HttpResponse(echostr)
        else:
            logger.info('weixin token check error')
            return HttpResponse('error')
