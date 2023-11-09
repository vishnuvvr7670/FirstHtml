from django.shortcuts import render

# Create your views here.
def FirstHtml(request):
    return render(request,'FirstHtml.html')