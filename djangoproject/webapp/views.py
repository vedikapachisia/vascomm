from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from .models import *

# Create your views here.
def index(request):
    obj = Plans(plan_id='INT600', free_talktime=200, free_sms=1000, free_data=12, call_rate=5, sms_rate=3, data_rate=1, price=600)
    obj.save()
    return render(request, 'index.html')

def text(request):
    content = open('webapp/static/hello.txt', 'r').read()
    response = StreamingHttpResponse(content)
    response['Content-Type'] = 'text/plain; charset=utf8'
    return response