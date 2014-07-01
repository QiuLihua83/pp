#*_*coding=utf-8

from django.http import HttpResponse
import time

def index(request):
    content = '<h3>hello , welcome here</h3><br> now, it is : '
    content += time.ctime()
    
    return HttpResponse(content)