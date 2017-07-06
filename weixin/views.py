import hashlib

from django.shortcuts import render


# Create your views here.

def home(request):
    print(request)
    try:
        signature = request.GET['signature']
        timestamp = request.GET['timestamp']
        nonce = request.GET['nonce']
        echostr = request.GET['echostr']
        token = 'miracle2018'

        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()

        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        if hashcode == signature:
            return echostr
        else:
            return ""
    except Exception as e:
        return e
