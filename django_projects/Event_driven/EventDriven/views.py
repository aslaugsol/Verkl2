from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def start(request):
    render(request, 'events/indexx.html')
    #return HttpResponse('EventDriven')