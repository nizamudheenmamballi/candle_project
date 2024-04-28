# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Candles

# Create your views here.

# def candles(request):
#     return HttpResponse("Hello world!")

def candles(request):
  template = loader.get_template('mode.html')
  return HttpResponse(template.render())
    # mymembers = Candles.objects.all().values()
    # template = loader.get_template('all_members.html')
    # context = {
    #     'mymembers': mymembers,
    # }
    # return HttpResponse(template.render(context, request))