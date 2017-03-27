from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.

def test(request):
    print 'in feature/featureOne add this line'
    return render(request, 'myapp/test.html')
