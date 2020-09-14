from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect
from django.http import FileResponse, Http404

def home(request, url):    
    try:
        print(settings.MEDIA_ROOT + '/informes/ '+url+'.pdf')
        return FileResponse(open(settings.MEDIA_ROOT + '/informes/ '+url+'.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def viewPng(request, url):    
    try:
        print(settings.MEDIA_ROOT + '/informes/ '+url+'.pdf')
        return FileResponse(open(settings.MEDIA_ROOT + '/informes/ '+url+'.png', 'rb'), content_type='image/png')
    except FileNotFoundError:
        raise Http404()




