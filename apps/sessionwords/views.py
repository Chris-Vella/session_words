from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    if not "word" in request.session:
        request.session["word"] = " "
    print request.session["word"]
    color = ["red", "green", "blue"]
    #WHY WON'T YOU WORK
    if "size" in request.session == None:
        request.session["size"] = "small"
        print size
        return size
    else:
        size = "big"
        print size
        return size

    sessionwords = {
        "word": word,
        "color": color,
        "size": size
    }
    print sessionwords
    return render(request, "sessionwords/index.html", sessionwords)

def sessionwords(request):
    request.session["word"] = str(request.POST["word"])
    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")