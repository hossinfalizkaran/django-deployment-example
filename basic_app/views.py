from django.shortcuts import render

# Create your views here.
def index(request):
    contex={'text':'hello wolrd'}
    return render(request,'basic_app/index.html',contex)

def other(request):
    return render(request,'basic_app/other.html')
def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
