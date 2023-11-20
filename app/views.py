from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'NAME':'CHANDANA'}
    return render(request,'forloop.html',d)
