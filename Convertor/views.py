from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def Currency(request):
    if request.method == "POST":
        r = requests.post('https://apilayer.net/api/convert?from=EUR&to=GBP&amount=100')
        if r.status_code == 200:
            #print(r.json())
            return HttpResponse('Yay, it worked')
        return HttpResponse('Could not save data')
    else:
        return render(request, 'Convertor.html')

def Convert(request):
    r = requests.get('https://apilayer.net/api/convert') #  ?from=EUR&to=GBP&amount=100')
    print(r.json)
    return render(request, 'conversion.html')