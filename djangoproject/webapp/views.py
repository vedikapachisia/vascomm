from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from .models import *

import time
import json
import random
import datetime

# Author: P.R. Ananya, Shayak Banerjee, Vedika Pachisia
# Date: 28 Oct '19
# Version: 1.0

# Create your views here.
def index(request):
    user_details = list(UserDetails.objects.all())
    context = dict()
    context['total_users'] = len(user_details)
    context['users'] = user_details
    
    return render(request, 'index.html', context=context)

def text(request):
    content = open('webapp/static/hello.txt', 'r').read()
    response = StreamingHttpResponse(content)
    response['Content-Type'] = 'text/plain; charset=utf8'
    return response

def read_from_file(request):
    f = open("call_text.txt", "r")
    s = f.read()
    return HttpResponse(s, content_type='text')

def revenue_data(request):
    f = open('revenue.txt', 'r')
    s = f.read()
    return HttpResponse(s, content_type='text')

def read_no_connected(request):
    f = open("no_connected.txt", "r")
    s = f.read()
    return HttpResponse(s, content_type='text')

def read_data_data(request):
    f = open("data_text.txt", "r")
    s = f.read()
    return HttpResponse(s, content_type='text')

def read_sms_data(request):
    f = open("message_text.txt", "r")
    s = f.read()
    return HttpResponse(s, content_type='text')

def simulate_calls(request):
    user_details = list(UserDetails.objects.all())
    f = open('revenue.txt', 'w+')
    f.write('300')
    f.close()
    
    while True:

        time.sleep(random.randint(1,100) * 0.01)

        #calls
        call_text = "<tr>"
        call_text = "<td>" + str(datetime.datetime.now())[0:19] + "</td>"
        call_text = call_text + "<td>" + str(random.choice(user_details).phone) + "</td>"
        call_text = call_text + "<td>" + str(random.choice(user_details).phone) + "</td></tr>"
        f = open("call_text.txt", "a+")
        f.write(call_text)
        f.close()
        f = open("no_connected.txt", "w+")
        f.write(str(random.randint(150, 350)))
        f.close()

        #messages
        message_text = "<tr><td>" + str(datetime.datetime.now())[12:19] + "</td><td>"
        message_text = message_text + str(random.choice(user_details).user_name) + "</td></tr>\n"
        f = open('message_text.txt', 'a+')
        f.write(message_text)
        f.close()

        #data
        data_text = "<tr><td>" + str(random.randint(1, 200)) + "</td><td>"
        data_text = data_text + str(random.choice(user_details).user_name) + "</td></tr>\n"
        f = open('data_text.txt', 'a+')
        f.write(data_text)
        f.close()

        #revenue
        f = open('revenue.txt', 'r')
        value = float(f.read())
        f.close()
        f = open('revenue.txt', 'w')
        value += float(random.randint(10, 1000)) * 0.01
        f.write("%.2f" % (value))
        f.close()


        
    return render(request, 'nothing')