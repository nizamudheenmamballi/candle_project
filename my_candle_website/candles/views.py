from django.shortcuts import render
from .models import Candles

def candles(request):
    # Query your model if needed
    mymembers = Candles.objects.all()
    context = {'mymembers': mymembers}
    return render(request, 'mode.html', context)

def stick(request):
    return render(request, 'candle.html')
