from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.

def test(request):
    print 11111
    return render(request, 'myapp/test.html')