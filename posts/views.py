from django.shortcuts import HttpResponse
import datetime

# Create your views here.

def main(request):
    if request.method =='GET':
        return HttpResponse('Hello! Its my project')


def date(request):
    if request.method == 'GET':
        return HttpResponse(datetime.datetime.now().date())


def goodbye(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user!')
