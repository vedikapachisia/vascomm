from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def text(request):
    content = open('webapp/static/hello.txt', 'r').read()
    response = StreamingHttpResponse(content)
    response['Content-Type'] = 'text/plain; charset=utf8'
    return response