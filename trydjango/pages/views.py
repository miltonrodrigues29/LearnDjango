from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args,**kwargs):
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request,"home.html",{})
    

def contact_view(request,*args,**kwargs):
    return render(request,"contact.html",{})

def about_view(request,*args, **kwargs):
    my_context = {
        "title":"This is milton",
        "this_is_true":True,
        "my_number":1234,
        "my_list":[101,201,301,321,"Abc"],
        "my_html":"<h1>Hello World</h1>"
    
    }
    return render(request,"about.html",my_context)

def social_view(request,*args, **kwargs):
    return render(request,"social.html",{})

    