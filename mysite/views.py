from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals()) 

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    rdict = {"hour_offset": offset, "next_time": dt}
    return render_to_response('hours_ahead.html', rdict)
